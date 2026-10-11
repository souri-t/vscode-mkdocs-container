"""Export embedded diagram SVGs and add links to their static files."""

from base64 import b64decode
from hashlib import sha256
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import posixpath


DIAGRAM_DIR = "assets/diagrams"
SVG_PREFIX = "data:image/svg+xml;base64,"
_diagrams = {}


def on_pre_build(config):
    _diagrams.clear()


class DiagramParser(HTMLParser):
    def __init__(self, source, page_url):
        super().__init__(convert_charrefs=True)
        self.source = source
        self.page_url = page_url
        self.replacements = []
        self.line_offsets = [0]
        for line in source.splitlines(keepends=True):
            self.line_offsets.append(self.line_offsets[-1] + len(line))

    def handle_starttag(self, tag, attrs):
        if tag != "img":
            return
        attributes = dict(attrs)
        classes = set((attributes.get("class") or "").split())
        if not classes.intersection({"mermaid", "plantuml"}):
            return
        src = attributes.get("src") or ""
        if not src.startswith(SVG_PREFIX):
            return

        svg = b64decode(src[len(SVG_PREFIX):], validate=True)
        filename = sha256(svg).hexdigest() + ".svg"
        _diagrams[filename] = svg
        # A trailing slash denotes a directory-style page URL.
        parent = posixpath.dirname(self.page_url)
        url = posixpath.relpath(f"{DIAGRAM_DIR}/{filename}", parent or ".")
        attributes["src"] = url
        rendered_attrs = " ".join(
            escape(key, quote=True) if value is None else
            f'{escape(key, quote=True)}="{escape(value, quote=True)}"'
            for key, value in attributes.items()
        )
        replacement = (
            f"<img {rendered_attrs} />"
            '<span class="diagram-link" style="display: block;">'
            f'<a href="{escape(url, quote=True)}" target="_blank" '
            'rel="noopener noreferrer">図を別タブで開く</a></span>'
        )
        line, column = self.getpos()
        start = self.line_offsets[line - 1] + column
        self.replacements.append((start, start + len(self.get_starttag_text()), replacement))

    handle_startendtag = handle_starttag


def on_page_content(html, page, config, files):
    parser = DiagramParser(html, page.url)
    parser.feed(html)
    parser.close()
    for start, end, replacement in reversed(parser.replacements):
        html = html[:start] + replacement + html[end:]
    return html


def on_post_build(config):
    output_dir = Path(config["site_dir"]) / DIAGRAM_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, svg in _diagrams.items():
        (output_dir / filename).write_bytes(svg)

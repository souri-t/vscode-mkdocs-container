"""Verify diagram extraction, page-relative links, and rebuild behavior."""

import base64
from hashlib import sha256
from html.parser import HTMLParser
import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "diagram_links", ROOT / "mkdocs-hooks/diagram_links.py"
)
hook = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook)


class Elements(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.images = []
        self.links = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))
        elif tag == "a":
            self.links.append(dict(attrs))


class DiagramLinksTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.config = {"site_dir": self.directory.name}
        hook.on_pre_build(self.config)
        self.svg = '<svg xmlns="http://www.w3.org/2000/svg" width="4000" height="3000"><text>日本語</text></svg>'.encode()

    def image(self, kind, svg=None):
        encoded = base64.b64encode(svg or self.svg).decode()
        return f'<img class="extra {kind}" alt="図 &amp; 説明" src="{hook.SVG_PREFIX}{encoded}" />'

    def render(self, html, url):
        return hook.on_page_content(html, SimpleNamespace(url=url), self.config, [])

    def test_relative_urls_and_identical_images(self):
        for url, prefix in [
            ("index.html", ""), ("design/index.html", "../"),
            ("ja/design/large.html", "../../"), ("design/large/", "../../"),
            ("", ""),
        ]:
            with self.subTest(url=url):
                output = self.render(
                    '<p>説明</p>\n<p>' + self.image("mermaid") + '\n' + self.image("plantuml") + '</p>', url
                )
                elements = Elements(output)
                expected = prefix + "assets/diagrams/" + sha256(self.svg).hexdigest() + ".svg"
                self.assertEqual([image["src"] for image in elements.images], [expected] * 2)
                self.assertEqual([link["href"] for link in elements.links], [expected] * 2)
                for link in elements.links:
                    self.assertEqual(link["target"], "_blank")
                    self.assertEqual(link["rel"], "noopener noreferrer")
                self.assertEqual(elements.images[0]["alt"], "図 & 説明")
                self.assertIn('<p>説明</p>', output)
        hook.on_post_build(self.config)
        files = list((Path(self.directory.name) / hook.DIAGRAM_DIR).glob("*.svg"))
        self.assertEqual(len(files), 1)
        self.assertEqual(files[0].read_bytes(), self.svg)

    def test_regular_images_are_unchanged(self):
        html = '<img src="photo.png">' + self.image("ordinary")
        self.assertEqual(self.render(html, "index.html"), html)
        self.assertFalse(hook._diagrams)

    def test_multiple_diagrams_and_rebuild(self):
        changed = self.svg.replace('日本語'.encode(), '更新した図'.encode())
        first = Elements(self.render(self.image("mermaid"), "index.html")).images[0]["src"]
        hook.on_post_build(self.config)
        hook.on_pre_build(self.config)
        output = self.render(self.image("mermaid", changed) + self.image("plantuml"), "index.html")
        elements = Elements(output)
        self.assertNotEqual(elements.images[0]["src"], first)
        self.assertEqual(elements.images[1]["src"], first)
        hook.on_post_build(self.config)
        for image, svg in zip(elements.images, [changed, self.svg]):
            self.assertEqual((Path(self.directory.name) / image["src"]).read_bytes(), svg)


if __name__ == "__main__":
    unittest.main()

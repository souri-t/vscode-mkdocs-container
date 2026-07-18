"""Render Mermaid fenced code blocks through the local Kroki service."""

from base64 import b64encode
from html import escape
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


KROKI_MERMAID_URL = "http://kroki:8000/mermaid/svg"
REQUEST_TIMEOUT_SECONDS = 30


def format_mermaid(source, language, class_name, options, md, **kwargs):
    """Return a self-contained SVG image for a ``mermaid`` SuperFences block."""
    del language, md, kwargs

    try:
        request = Request(
            KROKI_MERMAID_URL,
            data=source.encode("utf-8"),
            headers={"Content-Type": "text/plain; charset=utf-8"},
            method="POST",
        )
        with urlopen(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            svg = response.read()
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace").strip()
        raise RuntimeError(
            f"Mermaid の描画に失敗しました ({error.code}): {detail}"
        ) from error
    except URLError as error:
        raise RuntimeError(
            "ローカル Kroki サービスへ接続できません。"
            "docker compose で kroki と mermaid を起動してください。"
        ) from error

    image = b64encode(svg).decode("ascii")
    attributes = {key: value for key, value in options.items() if key != "class"}
    attributes.setdefault("alt", "Mermaid diagram")
    attributes["src"] = f"data:image/svg+xml;base64,{image}"
    attributes["class"] = class_name
    rendered_attributes = " ".join(
        f'{escape(str(key), quote=True)}="{escape(str(value), quote=True)}"'
        for key, value in attributes.items()
    )
    return f"<img {rendered_attributes} />"

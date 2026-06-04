from pathlib import Path
from shutil import copytree, rmtree


MATHJAX_SOURCE_DIR = Path("/opt/mathjax/es5")
MATHJAX_SITE_DIR = Path("assets/mathjax")
MATHJAX_CONFIG_PATH = "assets/mathjax/mathjax-config.js"
MATHJAX_CSS_PATH = "assets/mathjax/mathjax-left.css"
MATHJAX_RUNTIME_PATH = "assets/mathjax/es5/tex-mml-chtml.js"

MATHJAX_CONFIG = r'''window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
  chtml: {
    displayAlign: "left",
    displayIndent: "0"
  }
};

document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
'''

MATHJAX_CSS = '''.arithmatex {
  overflow-x: auto;
}

.arithmatex mjx-container[jax="CHTML"][display="true"] {
  display: block;
  margin: 1em 0;
  text-align: left !important;
}
'''


def _append_once(items, value):
    if value not in items:
        items.append(value)


def on_config(config):
    extra_javascript = config.setdefault("extra_javascript", [])
    _append_once(extra_javascript, MATHJAX_CONFIG_PATH)
    _append_once(extra_javascript, MATHJAX_RUNTIME_PATH)

    extra_css = config.setdefault("extra_css", [])
    _append_once(extra_css, MATHJAX_CSS_PATH)

    return config


def on_post_build(config):
    output_dir = Path(config["site_dir"]) / MATHJAX_SITE_DIR
    runtime_dir = output_dir / "es5"

    if runtime_dir.exists():
        rmtree(runtime_dir)

    if not MATHJAX_SOURCE_DIR.exists():
        raise RuntimeError(
            f"MathJax source directory was not found: {MATHJAX_SOURCE_DIR}. "
            "Rebuild the MkDocs container image so mathjax@3.2.2 is installed."
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    copytree(MATHJAX_SOURCE_DIR, runtime_dir)

    (output_dir / "mathjax-config.js").write_text(MATHJAX_CONFIG, encoding="utf-8")
    (output_dir / "mathjax-left.css").write_text(MATHJAX_CSS, encoding="utf-8")

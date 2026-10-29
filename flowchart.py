from pathlib import Path

import streamlit.components.v1 as components

html = (Path(__file__).parent.parent / "html" / "flowchart.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)

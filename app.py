import streamlit as st

st.set_page_config(
    page_title="Sustainable Mulki Solutions",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Full-window look: dark background, no footer or deploy button, no padding,
# and the embedded page fills the whole viewport height.
st.markdown(
    """
    <style>
      .stApp {background: #061923;}
      footer, #MainMenu, [data-testid="stMainMenu"], [data-testid="stAppDeployButton"],
      [data-testid="stToolbarActions"] {display: none !important;}
      [data-testid="stExpandSidebarButton"] {color: #9fc0c9;}
      header[data-testid="stHeader"] {background: transparent;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: 0; display: block; height: 100vh !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

pages = [
    st.Page("views/flowchart.py", title="Business Flowchart", icon="🏙️", default=True),
    st.Page("views/model_3d.py", title="3D Model", icon="🏠"),
]
st.navigation(pages).run()

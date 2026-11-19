"""
앱 진입점 (엔트리포인트)
실행: streamlit run streamlit_app.py
"""

import streamlit as st

# ── 페이지 기본 설정 (가장 먼저 호출) ─────────────────────
st.set_page_config(
    page_title="PACS Team App",
    page_icon="🩻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── 내부 모듈 ──────────────────────────────────────────────
from app.components.sidebar import render_sidebar
from app.pages.home import render_home
from app.pages.dashboard import render_dashboard


def main():
    render_sidebar()

    page = st.session_state.get("page", "홈")

    if page == "홈":
        render_home()
    elif page == "대시보드":
        render_dashboard()


if __name__ == "__main__":
    main()

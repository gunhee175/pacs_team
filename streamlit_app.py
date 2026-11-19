"""
앱 진입점 (엔트리포인트)
실행: streamlit run streamlit_app.py
"""

# st.set_page_config 은 반드시 첫 번째 Streamlit 호출이어야 하므로
# 내부 모듈 import 보다 먼저 실행합니다. (flake8 E402 noqa 처리)
import streamlit as st
from app.components.sidebar import render_sidebar  # noqa: E402
from app.pages.dashboard import render_dashboard  # noqa: E402
from app.pages.home import render_home  # noqa: E402

st.set_page_config(
    page_title="PACS Team App",
    page_icon="🩻",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    render_sidebar()

    page = st.session_state.get("page", "홈")

    if page == "홈":
        render_home()
    elif page == "대시보드":
        render_dashboard()


if __name__ == "__main__":
    main()


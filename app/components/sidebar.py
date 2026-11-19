"""
사이드바 컴포넌트 — 네비게이션 메뉴
"""

import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=40)
        st.title("PACS Team")
        st.divider()

        pages = ["홈", "대시보드"]
        selected = st.radio("메뉴", pages, label_visibility="collapsed")
        st.session_state["page"] = selected

        st.divider()
        st.caption("v0.1.0 · PACS Team")

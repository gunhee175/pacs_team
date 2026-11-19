"""
Streamlit 메인 앱 — 테스트 가능한 구조로 로직을 분리합니다.
"""

import streamlit as st
from app.logic import add, greet


def run():
    st.title("🩻 PACS Team App")
    st.write(greet("PACS"))

    a = st.number_input("A", value=0)
    b = st.number_input("B", value=0)
    if st.button("합산"):
        st.success(f"결과: {add(a, b)}")


if __name__ == "__main__":
    run()

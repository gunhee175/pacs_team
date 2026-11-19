"""
홈 페이지
"""

import streamlit as st


def render_home():
    st.title("🩻 PACS Team")
    st.markdown(
        """
        PACS(Picture Archiving and Communication System) 팀 프로젝트에 오신 것을 환영합니다.

        왼쪽 메뉴에서 원하는 페이지를 선택하세요.
        """
    )

    st.info("📌 **대시보드**에서 현황을 확인하세요.", icon="ℹ️")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="총 이미지", value="1,234", delta="+12")
    with col2:
        st.metric(label="금일 처리", value="56", delta="+5")
    with col3:
        st.metric(label="대기 중", value="8", delta="-3")

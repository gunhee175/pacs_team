"""
대시보드 페이지
"""

import streamlit as st
import pandas as pd


def render_dashboard():
    st.title("📊 대시보드")
    st.caption("샘플 데이터 — 실제 데이터 소스로 교체하세요.")

    # 샘플 데이터
    df = pd.DataFrame(
        {
            "날짜": pd.date_range("2024-01-01", periods=7, freq="D"),
            "처리 건수": [45, 52, 38, 61, 49, 55, 43],
            "대기 건수": [10, 8, 12, 5, 9, 7, 11],
        }
    )

    tab1, tab2 = st.tabs(["📈 차트", "📋 테이블"])

    with tab1:
        st.line_chart(df.set_index("날짜")[["처리 건수", "대기 건수"]])

    with tab2:
        st.dataframe(df, use_container_width=True)

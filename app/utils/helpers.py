"""
공통 유틸리티 — 세션 상태 초기화, 캐시 헬퍼 등
"""

import streamlit as st


def init_session_state(defaults: dict):
    """
    session_state에 기본값이 없을 때만 초기화합니다.

    Usage:
        init_session_state({"page": "홈", "user": None})
    """
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


@st.cache_data(ttl=60)
def load_sample_data():
    """
    데이터를 1분 단위로 캐싱합니다.
    실제 DB/API 호출로 교체하세요.
    """
    import pandas as pd

    return pd.DataFrame(
        {
            "id": range(1, 6),
            "name": ["이미지A", "이미지B", "이미지C", "이미지D", "이미지E"],
            "status": ["완료", "대기", "완료", "처리중", "완료"],
        }
    )

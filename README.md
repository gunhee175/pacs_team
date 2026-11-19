# PACS Team — Streamlit App

## 프로젝트 구조

```
pacs_team/
├── streamlit_app.py          ← 앱 진입점 (엔트리포인트)
├── app/
│   ├── components/
│   │   └── sidebar.py        ← 사이드바 (네비게이션)
│   ├── pages/
│   │   ├── home.py           ← 홈 페이지
│   │   └── dashboard.py      ← 대시보드 페이지
│   ├── utils/
│   │   └── helpers.py        ← 세션 상태, 캐시 헬퍼
│   └── logic.py              ← 비즈니스 로직 (테스트 대상)
├── tests/
│   └── test_logic.py         ← pytest 단위 테스트
├── .streamlit/
│   ├── config.toml           ← 테마 / 서버 설정
│   └── secrets.toml.example  ← 환경변수 예시 (커밋 금지)
├── .github/workflows/
│   ├── ci.yml                ← 테스트 + 린트
│   └── deploy.yml            ← main 머지 시 배포
├── requirements.txt
└── requirements-dev.txt
```

## 로컬 실행

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt

# 앱 실행
streamlit run streamlit_app.py

# 테스트
pytest tests/ -v --cov=app
```

## Streamlit Community Cloud 배포

1. [share.streamlit.io](https://share.streamlit.io) → New app
2. Repository 선택 → Branch: `main` → **Main file: `streamlit_app.py`**
3. Advanced settings → Secrets에 `.streamlit/secrets.toml.example` 내용 붙여넣기

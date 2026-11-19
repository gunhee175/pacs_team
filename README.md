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

## GitHub Pages 배포 (stlite 기반 정적 호스팅)

Streamlit은 본래 Python 서버가 필요하지만, **stlite (WebAssembly / Pyodide)** 기술을 통해 브라우저에서 직접 실행되는 정적 웹사이트로 변환하여 GitHub Pages에 무료 호스팅할 수 있습니다.

### 설정 방법 (최초 1회)
1. GitHub 저장소의 **Settings** → **Pages** 이동
2. **Build and deployment** > **Source** 항목을 `Deploy from a branch` 대신 **`GitHub Actions`** 로 선택
3. 코드를 푸시하면 `.github/workflows/deploy-gh-pages.yml` 워크플로우가 자동으로 실행되어 배포 완료됩니다.

## Streamlit Community Cloud 배포 (공식 대안)

1. [share.streamlit.io](https://share.streamlit.io) → New app
2. Repository 선택 → Branch: `main` → **Main file: `streamlit_app.py`**
3. Advanced settings → Secrets에 `.streamlit/secrets.toml.example` 내용 붙여넣기

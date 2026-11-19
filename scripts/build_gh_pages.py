"""GitHub Pages 배포를 위한 stlite 정적 HTML 번들 생성 스크립트"""

import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = BASE_DIR / "dist"

def build():
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    # 번들링할 파일 목록 수집
    files_to_bundle = {}

    # 1. 메인 엔트리포인트
    entrypoint_path = BASE_DIR / "streamlit_app.py"
    files_to_bundle["streamlit_app.py"] = entrypoint_path.read_text(encoding="utf-8")

    # 2. app 디렉토리 하위의 모든 py 파일
    app_dir = BASE_DIR / "app"
    for py_file in app_dir.rglob("*.py"):
        rel_path = py_file.relative_to(BASE_DIR).as_posix()
        files_to_bundle[rel_path] = py_file.read_text(encoding="utf-8")

    # 3. requirements.txt에서 핵심 패키지 추출 (버전 제약 제거 및 정리)
    requirements = ["pandas", "numpy", "plotly"]

    files_json = json.dumps(files_to_bundle, ensure_ascii=False)
    requirements_json = json.dumps(requirements)

    html_content = f"""<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <title>PACS Team - 의료영상 모니터링 대시보드</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏥</text></svg>">
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/@stlite/mountable@0.73.1/build/stlite.css"
    />
    <style>
      body, html {{
        margin: 0;
        padding: 0;
        height: 100%;
        overflow: hidden;
      }}
      #root {{
        height: 100vh;
        width: 100vw;
      }}
    </style>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://cdn.jsdelivr.net/npm/@stlite/mountable@0.73.1/build/stlite.js"></script>
    <script>
      stlite.mount(
        {{
          requirements: {requirements_json},
          entrypoint: "streamlit_app.py",
          files: {files_json},
        }},
        document.getElementById("root")
      );
    </script>
  </body>
</html>
"""

    output_path = DIST_DIR / "index.html"
    output_path.write_text(html_content, encoding="utf-8")
    print(f"✅ Build success! Output: {output_path} ({len(files_to_bundle)} files bundled)")

if __name__ == "__main__":
    build()

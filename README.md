# 코스피200 · 나스닥100 · S&P500 · 금 — 50일 이격도 트래커

이격도(= 종가 ÷ 50일 이동평균 × 100)를 매 거래일 자동 갱신하여 보여주는 정적 웹페이지입니다.
GitHub Pages + GitHub Actions로 무료 운영됩니다.

## 설치 방법 (최초 1회, 약 5분)

1. **저장소 만들기**
   [github.com/new](https://github.com/new)에서 새 저장소 생성.
   이름 예: `ma-disparity-tracker` · 공개(Public) 선택 · Create repository.

2. **파일 업로드**
   저장소 페이지에서 "uploading an existing file" 링크 클릭 →
   이 압축을 푼 폴더 안의 **모든 파일과 폴더**(`index.html`, `update_data.py`, `README.md`, `.github` 폴더 포함)를
   드래그해서 업로드 → Commit changes.
   ※ `.github` 폴더가 안 올라가면: Add file → Create new file → 파일명에
   `.github/workflows/update-data.yml` 입력 후 내용 붙여넣기.

3. **GitHub Pages 켜기**
   저장소 Settings → Pages → Source: `Deploy from a branch`,
   Branch: `main` / `(root)` → Save.

4. **데이터 최초 생성**
   저장소 Actions 탭 → 왼쪽 "Update data" → Run workflow 버튼 클릭.
   1~2분 후 `data.json`이 생성됩니다.

5. **접속**
   `https://<내아이디>.github.io/<저장소이름>/`
   예: `https://alphong.github.io/ma-disparity-tracker/`

## 자동 갱신 스케줄

- 매주 월–금 15:40 KST (국장 마감 후)
- 매주 화–토 07:10 KST (미장 마감 후)

스케줄 변경은 `.github/workflows/update-data.yml`의 cron(UTC 기준)을 수정하세요.

## 구성

| 파일 | 역할 |
|---|---|
| `index.html` | 웹페이지 (Chart.js, data.json을 읽어 렌더링) |
| `update_data.py` | Yahoo Finance 5년 일봉 수집 → `data.json` 생성 |
| `.github/workflows/update-data.yml` | 자동 갱신 스케줄 |

구간 기준선(과열/경계/해소)은 각 자산의 최근 5년 이격도 분포에서
상위 5% / 상위 15% / 하위 10% 백분위로 자동 산출됩니다.

※ 정보 제공용이며 투자 권유가 아닙니다.

"""Yahoo Finance에서 5년 일봉을 받아 data.json을 생성한다. GitHub Actions에서 실행."""
import json
from datetime import datetime, timezone, timedelta

import yfinance as yf

TICKERS = {
    "ks200": "^KS200",   # 코스피200
    "ndx": "^NDX",       # 나스닥100
    "spx": "^GSPC",      # S&P500
    "gold": "GC=F",      # 금 선물
}

series = {}
for key, ticker in TICKERS.items():
    df = yf.Ticker(ticker).history(period="5y", interval="1d", auto_adjust=False)
    df = df.dropna(subset=["Close"])
    rows = [
        [int(idx.timestamp() * 1000), round(float(close), 4)]
        for idx, close in zip(df.index, df["Close"])
    ]
    rows.sort(key=lambda r: r[0])
    if len(rows) < 60:
        raise SystemExit(f"{ticker}: 데이터가 부족합니다 ({len(rows)}행)")
    series[key] = rows
    print(f"{ticker}: {len(rows)} rows, last close {rows[-1][1]}")

kst = timezone(timedelta(hours=9))
out = {
    "updated_kst": datetime.now(kst).strftime("%Y-%m-%d %H:%M KST"),
    "series": series,
}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(out, f, separators=(",", ":"))
print("data.json 저장 완료")

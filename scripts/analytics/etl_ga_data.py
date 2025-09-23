import os
import csv
import datetime as dt
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric

# === パス設定 ===
BASE_DIR = os.path.dirname(__file__)  # /Users/xxx/GitHub Pages/Kyo.github.io/scripts/analytics/
OUT = f"metrics/ga4_daily_{dt.date.today().isoformat()}.csv"

# === GA4プロパティ設定 ===
# GA4管理画面 → 管理 → プロパティ設定 で確認したプロパティID（数字）
PROPERTY_ID = os.getenv("GA4_PROPERTY_ID", "316926808")  # 実際のプロパティIDに変更

# === 認証・クライアント作成 ===
# GOOGLE_APPLICATION_CREDENTIALS 環境変数を使用（より安全）
client = BetaAnalyticsDataClient()

# === レポートリクエスト定義 ===
request = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    date_ranges=[DateRange(start_date="30daysAgo", end_date="yesterday")],
    dimensions=[
        Dimension(name="date"),
        Dimension(name="pagePath"),
        Dimension(name="eventName"),
        Dimension(name="sessionSource"),
        Dimension(name="sessionMedium"),
    ],
    metrics=[Metric(name="eventCount"), Metric(name="totalUsers"), Metric(name="sessions")],
)

# === レポート取得とCSV出力 ===
response = client.run_report(request)

os.makedirs("metrics", exist_ok=True)
with open(OUT, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow([d.name for d in request.dimensions] + [m.name for m in request.metrics])
    for row in response.rows:
        dims = [v.value for v in row.dimension_values]
        mets = [v.value for v in row.metric_values]
        w.writerow(dims + mets)

print(f"✅ Wrote {OUT}")
print(f"Total rows: {len(response.rows)}")

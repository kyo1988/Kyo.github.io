---
layout: post
title: "EDINET XBRLで作る投資家級データベース"
description: "スキーマ設計、ETL、欠損対処、ダッシュボード例。"投資家が使える粒度"にするための設計と運用の実際。"
tags: [EDINET, Finance, ETL, Case-Study, XBRL, Database]
og_image: /images/edinet-db.png
last_modified_at: 2025-01-19
---

{% include tldr.html text="投資家が使える粒度"にするための設計と運用の実際。EDINET XBRLから投資家級データベースを構築する完全ガイド。" %}

## スキーマ設計

### 1. 基本テーブル構造
```sql
-- 企業マスタ
CREATE TABLE companies (
    company_id VARCHAR(20) PRIMARY KEY,
    company_name VARCHAR(200) NOT NULL,
    industry_code VARCHAR(10),
    listing_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 財務データ
CREATE TABLE financial_data (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    company_id VARCHAR(20),
    fiscal_year INT,
    fiscal_period VARCHAR(10),
    account_code VARCHAR(50),
    account_name VARCHAR(200),
    amount DECIMAL(20,2),
    unit VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);
```

### 2. インデックス設計
- **複合インデックス**: (company_id, fiscal_year, account_code)
- **パーティション**: fiscal_yearでパーティション分割
- **圧縮**: InnoDB圧縮でストレージ効率化

## ETLパイプライン

### 1. データ取得
```python
import requests
import zipfile
import xml.etree.ElementTree as ET

class EDINETDownloader:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://disclosure.edinet-fsa.go.jp/api/v1"
    
    def download_xbrl(self, doc_id):
        """XBRLファイルをダウンロード"""
        url = f"{self.base_url}/documents/{doc_id}"
        params = {"type": 1}  # XBRL形式
        headers = {"X-API-KEY": self.api_key}
        
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.content
        return None
```

### 2. データ変換
```python
class XBRLParser:
    def parse_financial_data(self, xbrl_content):
        """XBRLから財務データを抽出"""
        root = ET.fromstring(xbrl_content)
        financial_data = []
        
        # 勘定科目の抽出
        for context in root.findall(".//{http://www.xbrl.org/2003/instance}context"):
            context_id = context.get("id")
            period = self.extract_period(context)
            
            for item in root.findall(".//{http://www.xbrl.org/2003/instance}item"):
                if item.get("contextRef") == context_id:
                    account_code = item.get("name")
                    amount = float(item.text) if item.text else 0
                    
                    financial_data.append({
                        "context_id": context_id,
                        "period": period,
                        "account_code": account_code,
                        "amount": amount
                    })
        
        return financial_data
```

## 欠損対処

### 1. データクリーニング
{% include key-takeaways.html points="欠損値の特定: 勘定科目の存在確認||補完方法: 前年同期値または業界平均値||異常値検出: 統計的異常値の特定と除外||データ整合性: 貸借対照表のバランス確認" %}

### 2. 品質管理
```python
class DataQualityChecker:
    def check_balance_sheet_balance(self, data):
        """貸借対照表のバランス確認"""
        assets = data[data['account_type'] == 'Assets']['amount'].sum()
        liabilities = data[data['account_type'] == 'Liabilities']['amount'].sum()
        equity = data[data['account_type'] == 'Equity']['amount'].sum()
        
        balance = abs(assets - (liabilities + equity))
        return balance < 0.01  # 1円未満の差は許容
    
    def detect_outliers(self, data, column='amount'):
        """異常値の検出"""
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        return data[(data[column] < lower_bound) | (data[column] > upper_bound)]
```

## ダッシュボード例

### 1. 財務指標ダッシュボード
- **収益性**: ROE, ROA, 営業利益率
- **安全性**: 自己資本比率, 流動比率
- **効率性**: 総資産回転率, 売上高成長率
- **市場評価**: PER, PBR, EV/EBITDA

### 2. 業界比較分析
```python
def create_industry_comparison(company_id, industry_code):
    """業界比較分析"""
    query = """
    SELECT 
        company_id,
        AVG(ROE) as avg_roe,
        AVG(ROA) as avg_roa,
        AVG(営業利益率) as avg_operating_margin
    FROM financial_metrics 
    WHERE industry_code = %s
    GROUP BY company_id
    ORDER BY avg_roe DESC
    """
    return execute_query(query, (industry_code,))
```

## 運用監視

{% include qa.html items="データ更新頻度は？::四半期ごと（3月・6月・9月・12月）の決算発表後||監視すべき指標は？::データ取得成功率・処理時間・データ品質スコア||障害時の対応は？::アラート通知・自動再試行・手動復旧手順" %}

## 成果物

- **データベース**: MySQL/PostgreSQLで構築
- **ETLパイプライン**: Python + Airflowで自動化
- **ダッシュボード**: Grafana + InfluxDBで可視化
- **API**: RESTful APIでデータ提供

## 参考資料

- [EDINET API Documentation](https://disclosure.edinet-fsa.go.jp/api/v1/)
- [XBRL Specification](https://www.xbrl.org/)
- [Financial Data Analysis](https://pandas.pydata.org/)

{% include cta.html %}
{% include related-by-tags.html %}

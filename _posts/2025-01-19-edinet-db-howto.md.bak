---
layout: post
title: "EDINET XBRLで作る投資家級データベース"
description: "スキーマ設計、ETL、欠損対処、ダッシュボード例。"
tags: [EDINET, Finance, ETL, Case-Study]
og_image: /images/edinet-db.png
last_modified_at: 2025-01-19
---

{% include tldr.html text=""投資家が使える粒度"にするための設計と運用の実際。" %}

## 背景
EDINET XBRLデータを活用した投資分析の課題：
- データの非構造化（XML形式）
- 欠損値の多さ
- 時系列データの整合性
- リアルタイム性の要求

## スキーマ設計

### 1. 基本テーブル構造
```sql
-- 企業マスタ
CREATE TABLE companies (
    company_id VARCHAR(20) PRIMARY KEY,
    company_name VARCHAR(200),
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

-- 時価総額データ
CREATE TABLE market_data (
    company_id VARCHAR(20),
    date DATE,
    market_cap BIGINT,
    stock_price DECIMAL(10,2),
    volume BIGINT,
    PRIMARY KEY (company_id, date),
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);
```

### 2. インデックス設計
```sql
-- 検索性能向上
CREATE INDEX idx_financial_company_year ON financial_data(company_id, fiscal_year);
CREATE INDEX idx_financial_account ON financial_data(account_code);
CREATE INDEX idx_market_date ON market_data(date);
```

## ETLパイプライン

### 1. データ取得
```python
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def fetch_edinet_data(company_id, year):
    """EDINETからXBRLデータを取得"""
    url = f"https://disclosure.edinet-fsa.go.jp/api/v1/documents/{company_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return parse_xbrl(response.content)
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def parse_xbrl(xml_content):
    """XBRL XMLをパースして構造化データに変換"""
    root = ET.fromstring(xml_content)
    # XBRLタグの解析ロジック
    return extract_financial_data(root)
```

### 2. データクリーニング
```python
def clean_financial_data(df):
    """財務データのクリーニング"""
    # 欠損値処理
    df = df.dropna(subset=['amount'])
    
    # 異常値検出
    df = remove_outliers(df, 'amount')
    
    # 単位統一
    df = standardize_units(df)
    
    return df

def remove_outliers(df, column):
    """IQR法による異常値除去"""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
```

### 3. データ検証
```python
def validate_data_quality(df):
    """データ品質の検証"""
    checks = {
        'completeness': df.isnull().sum() / len(df),
        'consistency': check_consistency(df),
        'accuracy': check_accuracy(df)
    }
    
    return checks

def check_consistency(df):
    """データの一貫性チェック"""
    # 四半期データの合計が年次データと一致するか
    # 前年同期比の異常値検出
    # 業界平均からの乖離度
    pass
```

## 欠損値対処戦略

### 1. 欠損パターン分析
```python
import missingno as msno
import matplotlib.pyplot as plt

def analyze_missing_patterns(df):
    """欠損パターンの可視化"""
    msno.matrix(df)
    msno.heatmap(df)
    plt.show()
```

### 2. 補完手法
- **前値保持**: 四半期データの連続性
- **業界平均**: 同業他社との比較
- **時系列補間**: 線形/スプライン補間
- **機械学習**: 他の財務指標から予測

## ダッシュボード例

### 1. 企業比較ダッシュボード
```python
import streamlit as st
import plotly.express as px

def create_company_comparison():
    st.title("企業財務比較")
    
    # 企業選択
    companies = st.multiselect("比較企業", get_company_list())
    
    # 指標選択
    metrics = st.selectbox("財務指標", ["売上高", "営業利益", "純利益"])
    
    # 可視化
    fig = px.line(get_financial_data(companies, metrics))
    st.plotly_chart(fig)
```

### 2. 業界分析ダッシュボード
```python
def create_industry_analysis():
    st.title("業界分析")
    
    # 業界選択
    industry = st.selectbox("業界", get_industry_list())
    
    # 指標分布
    fig = px.histogram(get_industry_data(industry), x="ROE")
    st.plotly_chart(fig)
    
    # 相関分析
    corr_matrix = get_correlation_matrix(industry)
    st.heatmap(corr_matrix)
```

## 運用監視

### 1. データ品質監視
```python
def monitor_data_quality():
    """データ品質の継続監視"""
    alerts = []
    
    # 欠損率チェック
    if get_missing_rate() > 0.1:
        alerts.append("欠損率が10%を超過")
    
    # 更新遅延チェック
    if get_update_delay() > 7:
        alerts.append("データ更新が7日以上遅延")
    
    return alerts
```

### 2. パフォーマンス監視
```python
def monitor_performance():
    """システム性能の監視"""
    metrics = {
        'query_time': get_avg_query_time(),
        'memory_usage': get_memory_usage(),
        'disk_usage': get_disk_usage()
    }
    
    return metrics
```

## 成果物

1. **データベーススキーマ** (SQL)
2. **ETLパイプライン** (Python)
3. **ダッシュボード** (Streamlit)
4. **運用監視システム** (Python)

## Q&A
{% include qa.html q1="データ更新頻度は？" a1="四半期決算後1週間以内、リアルタイム監視" q2="欠損値はどう対処？" a2="パターン分析→適切な補完手法選択" q3="スケーラビリティは？" a3="MySQL + Redis + バッチ処理で対応" %}

{% include cta.html %}
{% include related-by-tags.html %}

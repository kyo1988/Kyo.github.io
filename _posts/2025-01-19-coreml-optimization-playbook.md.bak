---
layout: post
title: "CoreML最適化プレイブック（受託）"
description: "量子化/蒸留/アーキ設計の意思決定、評価指標、落とし穴。"
tags: [CoreML, On-device, Case-Study]
og_image: /images/coreml-playbook.png
last_modified_at: 2025-01-19
---

{% include tldr.html text="オンデバイスで品質を落とさず軽量化する設計判断の要点を3分で。" %}

## 背景
iOSアプリで機械学習モデルを動かす際の課題：
- モデルサイズの制約（App Store 100MB制限）
- 推論速度の要求（リアルタイム処理）
- 精度の維持（ビジネス要件）

## 設計判断フレームワーク

### 1. 量子化（Quantization）
- **INT8量子化**: 4倍軽量化、精度劣化1-3%
- **Dynamic Range**: より柔軟、精度劣化0.5-1%
- **選択基準**: 精度要求 > 95%ならDynamic Range

### 2. 蒸留（Knowledge Distillation）
- **Teacher-Student**: 大規模→軽量モデル
- **Self-Distillation**: 同一アーキテクチャ内
- **選択基準**: データ量と計算リソース次第

### 3. アーキテクチャ最適化
- **MobileNet**: 軽量、精度良好
- **EfficientNet**: スケーラブル
- **選択基準**: タスクの複雑さと制約

## 評価指標

```python
# 推論速度測定
import time
start = time.time()
prediction = model.predict(input_data)
inference_time = time.time() - start

# メモリ使用量
import psutil
memory_usage = psutil.Process().memory_info().rss / 1024 / 1024  # MB

# 精度評価
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_true, y_pred)
```

## 落とし穴と対策

### 1. 量子化後の精度劣化
- **対策**: キャリブレーションデータの品質向上
- **検証**: 代表的なエッジケースでのテスト

### 2. 推論速度の予測誤差
- **対策**: 実機でのベンチマーク必須
- **検証**: 複数デバイスでの性能確認

### 3. メモリリーク
- **対策**: ARC設定とメモリプール管理
- **検証**: 長時間実行テスト

## 成果物セット

1. **最適化済みCoreMLモデル** (.mlmodel)
2. **性能評価レポート** (PDF)
3. **実装ガイド** (Markdown)
4. **ベンチマークスクリプト** (Python)

## Q&A
{% include qa.html q1="どの手法をどう選ぶ？" a1="精度要求と制約から逆算して選択" q2="評価指標は？" a2="推論速度、メモリ使用量、精度の3軸" q3="納品物とスケジュールは？" a3="2-6週間、成果物4点セット" %}

{% include cta.html %}
{% include related-by-tags.html %}

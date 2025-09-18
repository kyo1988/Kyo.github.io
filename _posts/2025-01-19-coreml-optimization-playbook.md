---
layout: post
title: "CoreML最適化プレイブック（受託）"
description: "量子化/蒸留/アーキ設計の意思決定、評価指標、落とし穴。オンデバイスで品質を落とさず軽量化する設計判断の要点を3分で。"
tags: [CoreML, On-device, Case-Study, iOS, Machine-Learning]
og_image: /images/coreml-playbook.png
last_modified_at: 2025-01-19
lang: ja
---

{% include tldr.html text="オンデバイスで品質を落とさず軽量化する設計判断の要点を3分で。量子化→蒸留→アーキ設計の順序で最適化。" %}

## 設計判断のフレームワーク

### 1. 量子化（Quantization）
- **INT8量子化**: 精度損失5%以内でモデルサイズ75%削減
- **動的量子化**: 推論時のみ量子化、学習時はFP32維持
- **静的量子化**: 事前キャリブレーション、より高い圧縮率

### 2. 蒸留（Knowledge Distillation）
- **Teacher-Student**: 大規模モデル→軽量モデルへの知識転移
- **温度パラメータ**: T=3-5でソフトラベル生成
- **損失関数**: ハードラベル + ソフトラベル + 特徴マップ

### 3. アーキテクチャ設計
- **MobileNet**: 深度分離畳み込みで計算量削減
- **EfficientNet**: 複合スケーリングで効率最大化
- **SqueezeNet**: Fire Moduleでパラメータ数削減

## 評価指標

{% include key-takeaways.html points="精度: Top-1/Top-5 Accuracy||推論速度: FPS (Frames Per Second)||モデルサイズ: MB単位||メモリ使用量: RAM/VRAM||バッテリー消費: mAh/推論" %}

## 落とし穴と対策

### よくある失敗パターン
1. **過度な量子化**: 精度大幅低下
2. **不適切な蒸留**: 温度設定ミス
3. **アーキ選択ミス**: タスクとモデルの不適合

### 対策
- **段階的最適化**: 1つずつ適用して効果測定
- **A/Bテスト**: 複数手法の並行比較
- **実機検証**: シミュレータではなく実デバイスでテスト

## 成果物セット

{% include qa.html items="どの手法をどう選ぶ？::精度要求と制約から逆算して選択。精度優先→蒸留、サイズ優先→量子化||評価指標は？::精度・速度・サイズ・メモリ・バッテリーの5軸で総合評価||納品物とスケジュールは？::最適化モデル・実装ガイド・性能レポート（2-6週間）" %}

## 実装例

```swift
// CoreML最適化の実装例
import CoreML

class OptimizedModelManager {
    func loadOptimizedModel() -> MLModel? {
        guard let modelURL = Bundle.main.url(forResource: "optimized_model", withExtension: "mlmodelc") else {
            return nil
        }
        return try? MLModel(contentsOf: modelURL)
    }
    
    func predict(input: MLFeatureProvider) -> MLFeatureValue? {
        guard let model = loadOptimizedModel() else { return nil }
        return try? model.prediction(from: input).featureValue(for: "output")
    }
}
```

## 参考資料

- [CoreML Documentation](https://developer.apple.com/documentation/coreml)
- [Model Optimization Guide](https://developer.apple.com/machine-learning/models/)
- [WWDC Sessions](https://developer.apple.com/videos/)

{% include cta.html %}
{% include related-by-tags.html %}

---
layout: post
title: "CoreML Optimization Playbook (Consulting)"
description: "Decision-making for quantization/distillation/architecture design, evaluation metrics, and pitfalls. Key design decisions for on-device optimization without quality loss in 3 minutes."
tags: [CoreML, On-device, Case-Study, iOS, Machine-Learning]
og_image: /images/coreml-playbook.png
last_modified_at: 2025-01-19
lang: en
---

{% include tldr.html text="Key design decisions for on-device optimization without quality loss in 3 minutes. Optimization sequence: quantization → distillation → architecture design." %}

## Design Decision Framework

### 1. Quantization
- **INT8 Quantization**: 75% model size reduction with <5% accuracy loss
- **Dynamic Quantization**: Quantize only during inference, maintain FP32 during training
- **Static Quantization**: Pre-calibration for higher compression rates

### 2. Knowledge Distillation
- **Teacher-Student**: Knowledge transfer from large to lightweight models
- **Temperature Parameter**: Soft label generation with T=3-5
- **Loss Function**: Hard labels + soft labels + feature maps

### 3. Architecture Design
- **MobileNet**: Depthwise separable convolutions for computational reduction
- **EfficientNet**: Compound scaling for efficiency maximization
- **SqueezeNet**: Fire Module for parameter count reduction

## Evaluation Metrics

{% include key-takeaways.html points="Accuracy: Top-1/Top-5 Accuracy||Inference Speed: FPS (Frames Per Second)||Model Size: MB units||Memory Usage: RAM/VRAM||Battery Consumption: mAh/inference" %}

## Common Pitfalls and Solutions

### Typical Failure Patterns
1. **Excessive Quantization**: Significant accuracy degradation
2. **Improper Distillation**: Temperature setting errors
3. **Architecture Mismatch**: Task and model incompatibility

### Solutions
- **Incremental Optimization**: Apply one method at a time and measure effects
- **A/B Testing**: Parallel comparison of multiple approaches
- **Real Device Validation**: Test on actual devices, not simulators

## Deliverables

{% include qa.html items="How to choose methods?::Select based on accuracy requirements and constraints. Accuracy priority → distillation, size priority → quantization||What are the evaluation metrics?::Comprehensive evaluation across 5 axes: accuracy, speed, size, memory, battery||What are the deliverables and timeline?::Optimized model, implementation guide, performance report (2-6 weeks)" %}

## Implementation Example

```swift
// CoreML optimization implementation example
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

## References

- [CoreML Documentation](https://developer.apple.com/documentation/coreml)
- [Model Optimization Guide](https://developer.apple.com/machine-learning/models/)
- [WWDC Sessions](https://developer.apple.com/videos/)

{% include cta.html %}
{% include related-by-tags.html %}

---
layout: post
title: "Founder's Log #01 — 週報"
description: "今週のBuilt / Learned / One-chart / One-link。Jekyll 3互換パッチ適用とビルド安定化の成果をまとめ。"
tags: [Log, Founder, Jekyll, GitHub-Pages]
og_image: /images/log-01.png
last_modified_at: 2025-01-19
---

{% include tldr.html text="今週の決定：Jekyll 3互換パッチでビルド安定化。数字の動き：20回連続失敗→成功。次週は新機能段階的復活。" %}

## Built

- **Jekyll 3互換パッチ**: 配列引数includeを区切り文字方式に変更
- **ビルド安定化**: 20回連続失敗を解決、GitHub Pagesで正常動作
- **Liquid構文最適化**: `absolute_url`、`strip_newlines`フィルターを削除
- **JSON-LD実装**: Jekyll 3.10.0互換の構造化データ

## Learned

- **Jekyll 3.10.0の制限**: GitHub Pagesの制約を事前調査の重要性
- **段階的アプローチ**: 最小構成→機能復活の順序が重要
- **Liquid互換性**: 配列引数は不安定、区切り文字が確実

## One-chart

<figure>
  {% include img-cloudinary.html path="/charts/build-success.png" w="1200" alt="ビルド成功の推移" %}
  <figcaption>20回連続失敗から安定ビルドへの改善。Jekyll 3互換パッチの効果。</figcaption>
</figure>

## Q&A

{% include qa.html items="目的は？::20回連続ビルド失敗の根本解決||どう評価？::ローカルビルド成功＋GitHub Pages自動ビルド成功||次の一手は？::新機能の段階的復活とコンテンツ拡充" %}

## Sources

- [Jekyll 3.10.0 Documentation](https://jekyllrb.com/docs/3.10.0/)
- [GitHub Pages Jekyll Version](https://pages.github.com/versions/)
- [Liquid Template Language](https://shopify.github.io/liquid/)

{% include cta.html %}
{% include related-by-tags.html %}

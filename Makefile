.PHONY: site-qa site-assets-qa
site-qa:
	python scripts/site_qa/check_posts.py --base https://kyo1988.github.io

site-assets-qa:
	python scripts/site_qa/check_assets_200.py

.PHONY: site-qa
site-qa:
	python scripts/site_qa/check_posts.py --base https://kyo1988.github.io

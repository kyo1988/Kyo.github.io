# Analytics Implementation Guide

## Overview

This blog implements a comprehensive analytics system using Google Analytics 4 (GA4) with automatic event tracking, cross-domain session continuity, and daily data export capabilities.

## Architecture

### Frontend Tracking
- **GA4 Measurement ID**: Configured in `_config.yml`
- **Cross-domain tracking**: Blog ↔ Web App session continuity
- **Automatic event tracking**: CTA clicks, outbound links, page views
- **Placement tracking**: Hero, Core Capabilities, Latest Posts sections

### Backend Data Export
- **GA4 Data API**: Daily CSV export via `scripts/analytics/etl_ga_data.py`
- **Service Account**: Secure authentication with Viewer permissions
- **Automated**: Ready for GitHub Actions or cron job scheduling

## Configuration

### 1. GA4 Setup

#### Measurement ID
```yaml
# _config.yml
google_analytics:
  ga4_measurement_id: "G-XXXXXXXXXX"   # Your GA4 Measurement ID
  cross_domains:
    - "kyo1988.github.io"
    - "www.visageaiconsulting.com"
```

#### Property ID
```python
# scripts/analytics/etl_ga_data.py
PROPERTY_ID = "316926808"  # Verified and working
```

### 2. Event Tracking

#### Automatic Events
- `click_webapp` - Web App CTA clicks
- `click_ios_app` - iOS App CTA clicks  
- `click_read_more` - Article "Read more" clicks
- `click_view_all_playbooks` - Archive page clicks
- `click_outbound` - External link clicks

#### Placement Tracking
- `hero_cta_playbooks` - Hero section playbooks CTA
- `hero_cta_webapp` - Hero section web app CTA
- `hero_cta_ios` - Hero section iOS app CTA
- `core_capabilities` - Core capabilities section
- `latest_posts` - Latest posts section

### 3. Cross-Domain Tracking

```javascript
// _includes/head.html
gtag('config', 'G-XXXXXXXXXX', {
  'send_page_view': true,
  'linker': {
    'domains': ['kyo1988.github.io', 'www.visageaiconsulting.com']
  }
});
```

## Data Schema

### Dimensions
- `date` - Event date (YYYYMMDD)
- `pagePath` - Page path (e.g., `/Kyo.github.io/`)
- `eventName` - Event type (page_view, click_webapp, etc.)
- `sessionSource` - Traffic source (direct, google, facebook, etc.)
- `sessionMedium` - Traffic medium (none, referral, organic, etc.)

### Metrics
- `eventCount` - Number of events
- `totalUsers` - Unique users
- `sessions` - Number of sessions

## Key Performance Indicators (KPIs)

### Primary KPIs
1. **Hero→Web App CTR** = `click_webapp` / トップページPV
2. **Hero→iOS CTR** = `click_ios_app` / トップページPV
3. **Playbooks→Read more CTR** = `click_read_more` / 全記事PV合計
4. **Session Conversion Rate** = (click_webapp + click_ios_app) / sessions
5. **Article Engagement** = Time spent on article pages with new ToC system
6. **Component Usage** = Callout and figure component interaction rates

### Secondary KPIs
- **Average session duration**
- **Bounce rate**
- **Traffic source distribution**
- **Page performance by placement**

## Daily Operations

### 1. Data Export
```bash
cd scripts/analytics
export GOOGLE_APPLICATION_CREDENTIALS="ga4-fix.json"
python etl_ga_data.py
```

### 2. Data Analysis
- Review daily CSV files in `metrics/` directory
- Check for significant changes in KPIs
- Identify high-performing content and placements

### 3. Optimization
- A/B test CTA placements and copy
- Optimize underperforming pages
- Adjust UTM parameters for better attribution

## Automation

### GitHub Actions (Recommended)
```yaml
# .github/workflows/analytics.yml
name: Daily Analytics Export
on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight UTC
jobs:
  export:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install google-analytics-data
      - name: Export data
        env:
          GOOGLE_APPLICATION_CREDENTIALS: ${{ secrets.GA4_CREDENTIALS }}
        run: |
          cd scripts/analytics
          python etl_ga_data.py
      - name: Upload results
        uses: actions/upload-artifact@v3
        with:
          name: analytics-data
          path: scripts/analytics/metrics/
```

### Cron Job (Alternative)
```bash
# Add to crontab
0 0 * * * cd /path/to/blog/scripts/analytics && export GOOGLE_APPLICATION_CREDENTIALS="ga4-fix.json" && python etl_ga_data.py
```

## Troubleshooting

### Common Issues

1. **No data in GA4**
   - Check Measurement ID in `_config.yml`
   - Verify GA4 is properly loaded in browser
   - Check for JavaScript errors in console

2. **ETL script fails**
   - Verify service account permissions
   - Check property ID is correct
   - Ensure credentials file is valid

3. **Cross-domain tracking not working**
   - Verify linker configuration
   - Check domain names match exactly
   - Test with GA4 DebugView

### Debugging

#### Frontend
```javascript
// Check if GA4 is loaded
console.log(typeof gtag); // Should return 'function'

// Check dataLayer
console.log(window.dataLayer);
```

#### Backend
```bash
# Test ETL script
cd scripts/analytics
export GOOGLE_APPLICATION_CREDENTIALS="ga4-fix.json"
python etl_ga_data.py
```

## Security

### Credentials Management
- Service account keys are excluded from version control
- Use environment variables for sensitive data
- Rotate credentials regularly
- Monitor API usage and access logs

### Data Privacy
- GA4 is configured for privacy compliance
- No personally identifiable information (PII) is collected
- Data retention follows GA4 default policies

## Future Enhancements

### Planned Features
1. **Real-time dashboard** - Live KPI monitoring
2. **Automated alerts** - KPI threshold notifications
3. **Advanced segmentation** - User behavior analysis
4. **Conversion optimization** - A/B testing framework

### Integration Opportunities
- **BigQuery** - Advanced data analysis
- **Looker Studio** - Custom dashboards
- **Slack/Email** - Automated reporting
- **CRM** - Lead attribution and scoring

## Support

For technical issues or questions:
1. Check this guide and troubleshooting section
2. Review GA4 documentation
3. Check GitHub Issues for known problems
4. Contact the development team

---

*Last updated: January 19, 2025*
*Version: 2.0 - Article Kit Integration*

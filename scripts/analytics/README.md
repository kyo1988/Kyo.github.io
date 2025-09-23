# Analytics Scripts

This directory contains private analytics scripts and configuration files for the blog project.

## Files

- `etl_ga_data.py` - Google Analytics 4 data extraction script
- `ga4-fix.json` - Service account credentials for GA4 API access
- `README.md` - This documentation

## Usage

### Basic Usage

```bash
cd scripts/analytics
export GOOGLE_APPLICATION_CREDENTIALS="ga4-fix.json"
python etl_ga_data.py
```

### Output

The script generates daily CSV files in the `metrics/` directory:
- `ga4_daily_YYYY-MM-DD.csv` - Daily analytics data export
- Contains: date, pagePath, eventName, sessionSource, sessionMedium, eventCount, totalUsers, sessions

## Configuration

### GA4 Property ID
- **Current**: `316926808` (verified and working)
- **Location**: `etl_ga_data.py` line 13
- **Override**: Set `GA4_PROPERTY_ID` environment variable

### Service Account Setup
1. Create service account in Google Cloud Console
2. Download JSON key file as `ga4-fix.json`
3. Add service account to GA4 property with **Viewer** role
4. Set `GOOGLE_APPLICATION_CREDENTIALS` environment variable

## Data Schema

### Dimensions
- `date` - Date of the event
- `pagePath` - Page path (e.g., `/Kyo.github.io/`)
- `eventName` - Event type (page_view, session_start, etc.)
- `sessionSource` - Traffic source
- `sessionMedium` - Traffic medium

### Metrics
- `eventCount` - Number of events
- `totalUsers` - Unique users
- `sessions` - Number of sessions

## Security

⚠️ **IMPORTANT**: These files contain sensitive credentials and are excluded from version control via `.gitignore`.

- Never commit credentials to the repository
- Keep service account keys secure
- Rotate credentials regularly
- Use environment variables for sensitive data

## Dependencies

```bash
pip install google-analytics-data
```

## Troubleshooting

### Common Issues

1. **Permission Denied**: Ensure service account has Viewer role in GA4
2. **Invalid Property ID**: Verify property ID in GA4 admin panel
3. **No Data**: Check if GA4 is properly configured on the website

### Verification

```bash
# Test connection
export GOOGLE_APPLICATION_CREDENTIALS="ga4-fix.json"
python etl_ga_data.py

# Expected output:
# ✅ Wrote metrics/ga4_daily_YYYY-MM-DD.csv
# Total rows: [number]
```

## Integration

This script is designed to work with:
- **GA4 Measurement ID**: `G-VRYRGVBM3W` (configured and verified)
- **Cross-domain tracking**: Blog ↔ Web App session continuity
- **Event tracking**: Automatic CTA and outbound link tracking
- **Article Kit Integration**: Enhanced tracking for new ToC and component system
- **Daily automation**: GitHub Actions or cron job ready

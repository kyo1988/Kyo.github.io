# Operational Guidelines
## Kyo's Blog - GitHub Pages Repository

**Last Updated:** January 19, 2025 (Version 5 - Article Kit & ToC System Implementation)  
**Repository:** https://github.com/kyo1988/Kyo.github.io  
**Live Site:** https://kyo1988.github.io/Kyo.github.io/  
**Web App:** https://www.visageaiconsulting.com/en  
**Mobile App:** https://apps.apple.com/app/visage-ai-skin-advisor/id6748892785

---

## Repository Management Policy

### Public vs Private Content

This repository follows a strict separation between public blog content and private internal documentation:

#### ✅ **PUBLIC CONTENT** (Committed to Repository)
- Blog posts (`_posts/`)
- Static pages (`about.md`, `work-with-me.md`, etc.)
- Jekyll configuration (`_config.yml`)
- Templates and layouts (`_layouts/`, `_includes/`)
- Assets (`assets/`, `images/`)
- Theme files (`_sass/`, `css/`)
- Configuration files (`Gemfile`, `robots.txt`)
- Hero section and product features (`index.html`)
- Production Web App integration (https://www.visageaiconsulting.com/en)
- Mobile App integration (Visage AI: Skin Advisor)
- Structured data for both platforms
- Article Kit CSS system (`assets/css/article-kit.css`)
- Automatic ToC system (`_includes/toc.html`)
- Reusable components (`_includes/figure.html`, `_includes/callout.html`)
- GA4 Analytics system (`assets/js/analytics.js`, `scripts/analytics/`)

#### ❌ **PRIVATE CONTENT** (Excluded via .gitignore)
- Internal documentation and reports
- Project analysis and completion reports
- SOW (Statement of Work) documents
- Runbooks and operational guides
- Draft content and notes
- Confidential business information
- Google verification files
- System and IDE files

### File Naming Conventions

#### Internal Documentation Patterns (Auto-excluded)
```
*_ANALYSIS_REPORT.md
*_COMPLETION_REPORT.md
*_REPORT.md
*_SOW.md
*_RUNBOOK.md
*_GUIDE.md
*_MANUAL.md
*_DOCUMENTATION.md
*_NOTES.md
*_TODO.md
*_CHECKLIST.md
*_TEMPLATE.md
*_DRAFT.md
*_INTERNAL.md
*_PRIVATE.md
*_CONFIDENTIAL.md
```

#### Public Content Patterns
```
_posts/YYYY-MM-DD-title.md
about.md
work-with-me.md
newsletter.md
case-studies.md
press-kit.md
```

## Content Management Workflow

### 1. Content Creation
1. **Blog Posts**: Create in `_posts/` with proper front matter
2. **Static Pages**: Create in root directory with appropriate layout
3. **Assets**: Store in `assets/` or `images/` directories
4. **Multi-Platform Integration**: Include UTM tracking and structured data for both Web App and Mobile App
5. **Internal Docs**: Use excluded naming patterns (see above)

### 2. Quality Assurance
1. **Local Testing**: Always run `bundle exec jekyll build --trace`
2. **Content Review**: Ensure English consistency and academic style
3. **SEO Check**: Verify meta descriptions and structured data
4. **Mobile Testing**: Test responsive design on various devices
5. **Multi-Platform Integration**: Verify UTM tracking and conversion paths for both Web App and Mobile App
6. **Hero Section**: Test triple CTAs and product feature cards

### 3. Deployment Process
1. **Commit Changes**: Use descriptive commit messages
2. **Push to Master**: Changes auto-deploy to GitHub Pages
3. **Verify Deployment**: Check live site after 5-10 minutes
4. **Monitor Build**: Watch GitHub Actions for any failures

## Technical Standards

### Jekyll Configuration
- **Version**: Jekyll 3.10.0 (GitHub Pages compatible)
- **Plugins**: Only GitHub Pages allowed plugins
- **Liquid**: Jekyll 3.10.0 compatible syntax only
- **Ruby**: Use `github-pages` gem for local development

### Content Standards
- **Language**: English only
- **Style**: Academic writing style (consistent with existing articles)
- **Structure**: Introduction → Technical Analysis → Results → Reference
- **SEO**: JSON-LD structured data for both Web App and Mobile App, meta descriptions, canonical URLs
- **Article Layout**: 72ch max-width with automatic ToC generation
- **Components**: Use figure.html and callout.html for enhanced content
- **Typography**: Article Kit CSS system for consistent reading experience

### Code Quality
- **Liquid Syntax**: Jekyll 3.10.0 compatible
- **CSS**: Responsive design with dark mode support
- **JavaScript**: Minimal, performance-focused
- **Images**: Cloudinary optimization with lazy loading

## Security and Privacy

### Sensitive Information
- **Never commit**: API keys, passwords, personal information
- **Use .env files**: For local development secrets (excluded from repo)
- **Google Verification**: Files automatically excluded
- **Internal Reports**: All analysis and project documents excluded

### Access Control
- **Repository**: Public (content only)
- **Internal Docs**: Local storage only
- **Business Info**: Separate private repositories if needed

## Maintenance Schedule

### Daily
- Monitor build status
- Check for broken links
- Review content performance

### Weekly
- Content updates and new posts
- SEO performance review
- Technical maintenance

### Monthly
- Full site audit
- Performance optimization
- Content strategy review

## Troubleshooting

### Common Issues
1. **Build Failures**: Check Jekyll 3.10.0 compatibility
2. **Liquid Errors**: Verify syntax compatibility
3. **Deployment Delays**: Wait 5-10 minutes for GitHub Pages
4. **Content Issues**: Verify English consistency

### Emergency Procedures
1. **Rollback**: Use git to revert to last working commit
2. **Quick Fix**: Disable problematic features temporarily
3. **Full Rebuild**: Clear `_site/` and rebuild locally

## Contact and Support

- **Repository Owner**: Kyo Harada
- **Technical Issues**: Check GitHub Issues
- **Content Questions**: Review existing documentation
- **Emergency**: Use git rollback procedures

---

## Compliance Notes

This operational guideline ensures:
- **Privacy**: Internal documentation remains private
- **Security**: Sensitive information is protected
- **Quality**: Consistent content and technical standards
- **Maintainability**: Clear procedures for ongoing management
- **Multi-Platform Integration**: Seamless connection between blog, Web App, and Mobile App
- **Conversion Optimization**: UTM tracking and clear conversion paths across all platforms

**Remember**: When in doubt, keep it private. Only blog content, technical assets, and Web App integration should be committed to this public repository.

---

*This document is for internal use only and should not be committed to the public repository.*

(function(){
  if (typeof gtag === 'undefined') return;

  const siteHost = location.host;

  // 共通ヘルパ
  const track = (name, params={}) => {
    try { gtag('event', name, params); } catch(e){}
  };

  // 外部リンクのアウトバウンド計測（汎用）
  document.addEventListener('click', function(e){
    const a = e.target.closest('a[href]');
    if(!a) return;

    const url = new URL(a.href, location.href);
    const isHttp = url.protocol === 'http:' || url.protocol === 'https:';
    const isExternal = isHttp && url.host !== siteHost;

    // 配置ヒント（data-placement があれば優先）
    const placement = a.dataset.placement || inferPlacement(a);
    const linkText = (a.textContent || '').trim().slice(0, 100);

    if(isExternal){
      track('click_outbound', {
        link_url: url.href,
        link_domain: url.host,
        link_text: linkText,
        placement: placement,
        outbound: true
      });
    }

    // 研究成果への遷移を、一般の外部クリックから分けて測る。
    const researchAssetType = classifyResearchAsset(url);
    if(researchAssetType){
      track('research_asset_click', {
        asset_type: researchAssetType,
        link_url: url.href,
        link_domain: url.host,
        link_text: linkText,
        placement: placement
      });
    }

    if(url.protocol === 'mailto:'){
      track('contact_click', {
        contact_method: 'email',
        placement: placement
      });
    }

    // 代表的CTAの個別イベント（集計を見やすく）
    if (url.href.includes('visageaiconsulting.com')){
      track('click_webapp', { link_url: url.href, placement });
    }
    if (url.href.includes('apps.apple.com')){
      track('click_ios_app', { link_url: url.href, placement });
    }
    if ((a.textContent || '').trim().toLowerCase().startsWith('read more')){
      track('click_read_more', { post_url: url.href, placement });
    }
    if (url.pathname.endsWith('/archives/') || (a.textContent || '').includes('View all playbooks')){
      track('click_view_all_playbooks', { link_url: url.href, placement });
    }
  }, {capture:true});

  // 配置推定（クラスや親要素から推測）
  function inferPlacement(a){
    if(a.closest('.cta')) return 'post_footer';
    if(a.closest('.post-content, .article')) return 'article_body';
    const sec = a.closest('section');
    if(!sec) return 'unknown';
    if(sec.querySelector('.hero, .hero h1')) return 'hero';
    if(sec.querySelector('.grid, .card')) return 'core_capabilities';
    if(sec.querySelector('.post-grid')) return 'latest_posts';
    return sec.className || 'section';
  }

  function classifyResearchAsset(url){
    if(url.protocol !== 'http:' && url.protocol !== 'https:') return null;
    if(url.hostname === 'doi.org' || url.hostname.endsWith('.zenodo.org') || url.hostname === 'zenodo.org') return 'doi';
    if(url.hostname === 'github.com' || url.hostname.endsWith('.github.com')) return 'github';
    if(url.pathname.toLowerCase().endsWith('.pdf')) return 'pdf';
    return null;
  }
})();

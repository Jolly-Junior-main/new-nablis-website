
$replacement = @"
<div class="nav-right" style="display:flex; align-items:center; gap: 12px;">
    <!-- Language Dropdown -->
    <div class="lang-dropdown" style="position: relative;">
        <button class="lang-btn" style="background: transparent; border: 1px solid rgba(255,255,255,0.2); color: white; padding: 6px 12px; border-radius: 20px; display: flex; align-items: center; gap: 6px; cursor: pointer; font-size: 13px; font-weight: 600;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
            <span id="current-lang-text">EN</span>
        </button>
        <div class="lang-menu" style="display: none; position: absolute; top: 100%; right: 0; margin-top: 8px; background: rgba(40,40,45,0.95); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 20px rgba(0,0,0,0.3); z-index: 1000; min-width: 120px;">
            <a href="#" onclick="changeLanguage('en'); return false;" style="display: block; padding: 10px 16px; color: white; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.05); font-size: 14px; text-align: left;">English</a>
            <a href="#" onclick="changeLanguage('ar'); return false;" style="display: block; padding: 10px 16px; color: white; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.05); font-family: 'Cairo', sans-serif; font-size: 14px; text-align: left;">???????</a>
            <a href="#" onclick="changeLanguage('am'); return false;" style="display: block; padding: 10px 16px; color: white; text-decoration: none; font-family: 'Noto Sans Ethiopic', sans-serif; font-size: 14px; text-align: left;">????</a>
        </div>
    </div>
    
    <a href="quote.html" class="btn-brand">Request a Quote</a>
"@

$htmls = Get-ChildItem -Filter *.html
foreach ($file in $htmls) {
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    $content = $content -replace '(?s)<div class="nav-right" style="display:flex; align-items:center; gap: 12px;">.*?<a href="quote\.html" class="btn-brand">Request a Quote</a>', $replacement
    [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
}


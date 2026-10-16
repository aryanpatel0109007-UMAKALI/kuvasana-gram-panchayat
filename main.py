import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="કુવાસણા ગ્રામ પંચાયત | Kuvasana Gram Panchayat",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep Streamlit's own page chrome out of the visual design.
st.markdown(
    """
    <style>
      #MainMenu, footer, header[data-testid="stHeader"],
      [data-testid="stToolbar"], .stAppDeployButton,
      [data-testid="stDecoration"] { display: none !important; }
      .stApp, [data-testid="stAppViewContainer"],
      [data-testid="stMain"], .main, .block-container {
          background: #f7f7f1 !important;
      }
      .block-container { padding: 0 !important; max-width: 100% !important; }
      iframe { border: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

PAGE = r'''<!DOCTYPE html>
<html lang="gu">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>કુવાસણા ગ્રામ પંચાયત</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Gujarati:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');
:root {
  --green:#0e4b34; --leaf:#18823b; --orange:#f58220; --navy:#173f7a;
  --ink:#17392b; --cream:#fffaf0; --border:#e7e4d8;
}
* { box-sizing:border-box; }
html,body { margin:0; padding:0; background:#f7f7f1; color:var(--ink); font-family:'Noto Sans Gujarati','Inter',sans-serif; }
body { overflow-x:hidden; }
button { font-family:inherit; cursor:pointer; }
.site { max-width:1600px; margin:0 auto; padding:0 20px 18px; }
.top-stripe { height:7px; border-radius:0 0 5px 5px; background:linear-gradient(90deg,#ff9933 0 33.333%,#fff 33.333% 66.666%,#138808 66.666% 100%); }
.header { display:grid; grid-template-columns:72px minmax(240px,1.2fr) minmax(430px,2.1fr) 82px; align-items:center; gap:17px; min-height:105px; padding:9px 10px 10px; background:#fbfaf5; }
.emblem-small { width:62px; height:77px; object-fit:contain; }
.brand-gu { color:var(--green); font-size:clamp(20px,2vw,30px); font-weight:800; line-height:1.25; white-space:nowrap; }
.brand-en { font-family:Inter,sans-serif; font-size:15px; font-weight:800; color:#234234; margin-top:3px; }
.brand-tag { font-family:Inter,sans-serif; font-size:11px; color:#68766d; margin-top:4px; }
.nav { display:flex; justify-content:space-between; gap:6px; align-items:center; }
.nav button { border:0; border-bottom:3px solid transparent; background:transparent; color:#214936; padding:10px 5px 8px; font-size:clamp(11px,.95vw,14px); font-weight:700; white-space:nowrap; }
.nav button:hover,.nav button.active { border-bottom-color:#f58220; color:#d56a10; }
.language { text-align:center; font-size:12px; color:#234737; font-weight:700; line-height:1.6; }
.hero { position:relative; min-height:390px; border:1px solid #eadfca; border-radius:17px; overflow:hidden; isolation:isolate; background:linear-gradient(115deg,#fff5df 0%,#fffdf5 46%,#eaf4dc 100%); box-shadow:0 5px 18px #163d2d0b; }
.hero-art { position:absolute; inset:0; width:100%; height:100%; z-index:-1; }
.hero-content { position:relative; display:grid; grid-template-columns:18% 54% 28%; align-items:center; min-height:390px; padding:24px 21px 22px; }
.anniversary { text-align:center; color:#94703e; padding:10px 4px; align-self:center; }
.anniv-row { display:flex; align-items:center; justify-content:center; gap:4px; }
.anniv-number { font-family:Georgia,serif; font-size:clamp(55px,5vw,76px); line-height:.9; color:#9e7843; }
.anniv-ribbon { display:flex; flex-direction:column; gap:4px; transform:skewY(-15deg); }
.anniv-ribbon span { display:block; width:44px; height:7px; border-radius:0 12px 12px 0; }
.anniv-ribbon span:nth-child(1){background:#ff9933}.anniv-ribbon span:nth-child(2){background:#fff;border:1px solid #eee}.anniv-ribbon span:nth-child(3){background:#138808}
.anniv-copy { font-size:clamp(13px,1.2vw,18px); line-height:1.48; font-weight:800; margin-top:12px; }
.hero-copy { text-align:center; padding:5px 8px 0; min-width:0; }
.eyebrow { font-size:13px; color:#16743a; font-weight:800; letter-spacing:.1px; margin-bottom:9px; }
.hero-title { color:#0d5138; font-size:clamp(29px,3.15vw,47px); font-weight:800; line-height:1.25; margin:0 0 7px; }
.hero-title .orange { color:#e87517; }
.hero-subtitle { color:#234e39; font-size:clamp(17px,1.65vw,25px); font-weight:750; line-height:1.45; margin-bottom:9px; }
.green-line { color:#247a3a; font-size:clamp(11px,1.02vw,15px); line-height:1.8; font-weight:800; }
.motto { color:#124b34; font-size:clamp(21px,1.9vw,28px); font-weight:800; margin-top:7px; }
.vande { margin-top:3px; font-family:Inter,sans-serif; font-size:clamp(16px,1.45vw,21px); font-weight:800; }
.vande .orange { color:#ef7817; }.vande .green { color:#16813c; }
.hero-right { min-width:0; height:100%; display:flex; align-items:center; justify-content:center; gap:8px; padding:8px 3px 22px; }
.emblem-large { max-width:65%; width:auto; height:clamp(155px,17vw,224px); object-fit:contain; filter:sepia(.3) saturate(.65); }
.chakra { width:clamp(66px,7.6vw,105px); height:clamp(66px,7.6vw,105px); flex:0 0 auto; }
.village-art { position:absolute; left:0; bottom:0; width:58%; height:38%; z-index:-1; opacity:.82; }
.india-gate { position:absolute; right:3.3%; bottom:5px; width:7%; min-width:52px; max-width:100px; opacity:.58; z-index:0; }
.portal-heading { display:flex; align-items:center; justify-content:center; gap:13px; color:var(--green); font-size:clamp(21px,2vw,29px); font-weight:800; text-align:center; margin:18px 0 13px; }
.rule { width:58px; height:5px; border-top:2px solid #ff9933; border-bottom:2px solid #138808; flex-shrink:0; }
.portals { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:17px; }
.portal { text-align:center; min-height:205px; border-radius:15px; border:1px solid #e9e7df; padding:14px 14px 12px; display:flex; flex-direction:column; align-items:center; }
.portal.public { background:linear-gradient(145deg,#f4fbf0,#e0f3db); }
.portal.citizen { background:linear-gradient(145deg,#fff8ed,#ffecd7); }
.portal.admin { background:linear-gradient(145deg,#f1f7ff,#e0efff); }
.portal.officer { background:linear-gradient(145deg,#fbf5ff,#eee2fb); }
.portal-icon { display:flex; align-items:center; justify-content:center; width:53px; height:53px; border-radius:50%; color:#fff; font-size:26px; margin-bottom:6px; box-shadow:0 4px 9px #163d2d12; }
.public .portal-icon,.public .portal-button{background:#07852f}.citizen .portal-icon,.citizen .portal-button{background:#f06c0a}.admin .portal-icon,.admin .portal-button{background:#0755ab}.officer .portal-icon,.officer .portal-button{background:#6425a1}
.portal h3 { font-size:clamp(16px,1.35vw,20px); line-height:1.35; margin:0 0 4px; font-weight:800; }
.public h3{color:#08752c}.citizen h3{color:#d65f08}.admin h3{color:#064d9e}.officer h3{color:#5b2494}
.portal p { color:#284439; font-size:12px; line-height:1.5; min-height:37px; margin:0 0 9px; }
.portal-button { border:0; border-radius:8px; color:white; padding:9px 12px; font-size:13px; font-weight:800; width:min(100%,180px); margin-top:auto; }
.portal-button:hover { filter:brightness(.93); transform:translateY(-1px); }
.features-panel { border:1px solid #e6e7df; border-radius:15px; background:#fffefa; margin-top:14px; padding:8px 9px 10px; box-shadow:0 3px 13px #153c2d08; }
.feature-heading { display:flex; align-items:center; justify-content:center; gap:12px; color:var(--green); font-size:22px; font-weight:800; text-align:center; margin:1px 0 7px; }
.feature-grid { display:grid; grid-template-columns:repeat(8,minmax(0,1fr)); }
.feature { text-align:center; min-width:0; padding:5px 4px 3px; border-right:1px solid #dde2d9; }
.feature:last-child{border-right:0}
.feature-icon { height:46px; width:46px; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 5px; font-size:22px; }
.feature-label { color:#183c2c; font-size:11px; line-height:1.35; font-weight:750; }
.pink{background:#ffdade}.amber{background:#ffedc9}.mint{background:#d9f1d3}.sky{background:#d9efff}.leaf{background:#def1d0}.lilac{background:#ecdfff}.aqua{background:#d3f0f2}.rose{background:#ffe0e6}
.footer { display:grid; grid-template-columns:1fr 1fr 1fr; align-items:center; gap:8px; background:#073f2e; color:#fff; border-radius:11px; margin-top:14px; padding:13px 18px; }
.footer-brand { font-size:13px; font-weight:800; line-height:1.45; }.footer-brand small {display:block;font-size:10px;font-weight:500;opacity:.85;font-family:Inter,sans-serif}
.footer-motto { text-align:center; font-weight:800; font-size:14px; }.footer-right { text-align:right; font-size:11px; line-height:1.5; opacity:.9; }
.info-panel { margin-top:12px; background:white; border:1px solid var(--border); border-radius:13px; padding:19px; display:none; }
.info-panel h2 { color:var(--green); margin:0 0 8px; font-size:24px; }.info-panel p {margin:0 0 8px;line-height:1.7}
.home-only.hidden { display:none; }
@media(max-width:1050px) {
 .site{padding-left:12px;padding-right:12px}.header{grid-template-columns:55px 1.2fr 2fr 58px;gap:8px;padding-left:3px;padding-right:3px}.emblem-small{height:65px;width:50px}.brand-gu{font-size:clamp(17px,2vw,23px)}.brand-en{font-size:12px}.brand-tag{font-size:9px}.nav button{font-size:10px;padding-left:2px;padding-right:2px}.hero-content{grid-template-columns:15% 57% 28%;padding-left:10px;padding-right:10px}.emblem-large{height:165px}.chakra{width:63px;height:63px}.portal{padding:12px 8px;min-height:207px}.portal p{font-size:11px}
}
@media(max-width:720px) {
 .site{padding:0 9px 12px}.header{grid-template-columns:45px 1fr 50px;gap:8px;min-height:auto;padding:10px 2px}.emblem-small{height:58px;width:43px}.brand-gu{font-size:18px;white-space:normal}.brand-en{font-size:11px}.brand-tag{font-size:9px}.nav{grid-column:1 / -1;grid-row:2;overflow-x:auto;justify-content:flex-start}.nav button{font-size:11px;padding:7px 9px}.language{grid-column:3;grid-row:1}.hero{min-height:0}.hero-content{grid-template-columns:1fr;gap:3px;padding:15px 10px 18px;min-height:0}.anniversary{display:none}.hero-copy{padding:8px 3px}.hero-title{font-size:29px}.hero-subtitle{font-size:17px}.green-line{font-size:11px}.motto{font-size:22px}.hero-right{gap:18px;padding:7px 0 12px;height:auto}.emblem-large{height:105px;max-width:40%}.chakra{width:65px;height:65px}.village-art{width:100%;height:22%;opacity:.36}.india-gate{display:none}.portal-heading{font-size:20px;gap:8px}.rule{width:24px}.portals{grid-template-columns:repeat(2,minmax(0,1fr));gap:9px}.portal{min-height:200px;padding:12px 9px}.portal h3{font-size:15px}.portal p{font-size:11px;min-height:44px}.feature-heading{font-size:19px}.feature-grid{grid-template-columns:repeat(4,minmax(0,1fr));row-gap:9px}.feature{border-right:1px solid #dde2d9}.feature:nth-child(4n){border-right:0}.feature-label{font-size:10px}.footer{grid-template-columns:1fr;justify-items:center;text-align:center;padding:14px}.footer-motto{text-align:center}.footer-right{text-align:center}
}
</style>
</head>
<body>
<div class="site">
  <div class="top-stripe"></div>
  <header class="header">
    <img class="emblem-small" src="https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg" alt="ભારતનું રાષ્ટ્રીય ચિહ્ન">
    <div class="brand">
      <div class="brand-gu">કુવાસણા ગ્રામ પંચાયત</div>
      <div class="brand-en">Kuvasana Gram Panchayat</div>
      <div class="brand-tag">Digital Village | Smart Governance | Better Tomorrow</div>
    </div>
    <nav class="nav" aria-label="મુખ્ય મેનુ">
      <button class="active" onclick="showPage('home',this)">⌂ મુખ્ય પેજ</button>
      <button onclick="showPage('village',this)">▣ ગામની માહિતી</button>
      <button onclick="showPage('development',this)">▧ વિકાસકાર્યો</button>
      <button onclick="showPage('news',this)">▤ સમાચાર</button>
      <button onclick="showPage('contact',this)">☎ સંપર્ક</button>
    </nav>
    <div class="language">🇮🇳<br>ગુજરાતી</div>
  </header>

  <main id="homePage" class="home-only">
    <section class="hero">
      <svg class="hero-art" viewBox="0 0 1500 390" preserveAspectRatio="none" aria-hidden="true">
        <defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9edf0"/><stop offset=".58" stop-color="#fff3d4"/><stop offset="1" stop-color="#fbe9ba"/></linearGradient><linearGradient id="ribbonO" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffb14b"/><stop offset="1" stop-color="#ff8100"/></linearGradient><linearGradient id="ribbonG" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#44a64a"/><stop offset="1" stop-color="#087c2d"/></linearGradient></defs>
        <rect width="1500" height="390" fill="url(#sky)"/>
        <circle cx="980" cy="225" r="51" fill="#fff7ca" opacity=".82"/>
        <path d="M650 0 C850 55 1080 78 1500 0 L1500 90 C1190 165 945 118 690 91 Z" fill="url(#ribbonO)" opacity=".94"/>
        <path d="M670 91 C920 150 1130 175 1500 95 L1500 155 C1210 230 970 185 695 147 Z" fill="#fffdf8" opacity=".98"/>
        <path d="M700 150 C950 205 1200 228 1500 153 L1500 280 C1220 337 960 284 710 253 Z" fill="url(#ribbonG)" opacity=".95"/>
        <path d="M0 270 C170 240 290 265 420 290 C520 308 610 294 760 278 L850 390 L0 390Z" fill="#a4c98a" opacity=".55"/>
        <path d="M0 315 C160 285 300 318 430 328 C570 340 690 317 820 300 L900 390 L0 390Z" fill="#7eac65" opacity=".55"/>
        <path d="M0 353 C185 324 320 354 455 359 C600 363 730 339 870 336 L930 390 L0 390Z" fill="#438b4b" opacity=".52"/>
        <g fill="#fff4d7" stroke="#ceb98b" stroke-width="2" opacity=".95">
          <path d="M30 310 L76 276 L122 310Z"/><rect x="40" y="310" width="72" height="42"/><rect x="64" y="326" width="17" height="26" fill="#a8865a"/>
          <path d="M132 325 L170 294 L208 325Z"/><rect x="143" y="325" width="54" height="31"/><rect x="163" y="337" width="13" height="19" fill="#a8865a"/>
          <path d="M237 311 L282 277 L327 311Z"/><rect x="247" y="311" width="70" height="42"/><rect x="273" y="325" width="16" height="28" fill="#a8865a"/>
          <path d="M340 330 L380 299 L420 330Z"/><rect x="350" y="330" width="60" height="31"/><rect x="372" y="340" width="14" height="21" fill="#a8865a"/>
        </g>
        <g fill="#3a8748" opacity=".82"><circle cx="224" cy="309" r="22"/><rect x="220" y="308" width="8" height="44" fill="#856b43"/><circle cx="431" cy="319" r="25"/><rect x="426" y="318" width="9" height="43" fill="#856b43"/><circle cx="501" cy="322" r="18"/><rect x="497" y="321" width="8" height="35" fill="#856b43"/></g>
      </svg>
      <svg class="village-art" viewBox="0 0 880 165" preserveAspectRatio="none" aria-hidden="true"><path d="M0 125 C150 85 250 130 385 120 C520 107 655 70 880 107 L880 165 L0 165Z" fill="#bdd7a5" opacity=".65"/><path d="M0 143 C180 118 300 147 460 137 C620 126 720 105 880 130 L880 165 L0 165Z" fill="#75aa65" opacity=".55"/><g fill="#fff4dc" stroke="#cdb88b" stroke-width="1.5"><path d="M24 123 L64 90 L105 123Z"/><rect x="34" y="123" width="60" height="29"/><path d="M124 132 L154 105 L184 132Z"/><rect x="132" y="132" width="45" height="23"/><path d="M212 122 L255 89 L298 122Z"/><rect x="222" y="122" width="65" height="31"/><path d="M318 135 L351 108 L384 135Z"/><rect x="326" y="135" width="50" height="20"/></g><g fill="#368349"><circle cx="112" cy="120" r="18"/><circle cx="198" cy="126" r="14"/><circle cx="304" cy="122" r="19"/><circle cx="398" cy="128" r="17"/></g><g fill="#7d6949"><rect x="108" y="119" width="7" height="35"/><rect x="195" y="125" width="6" height="28"/><rect x="300" y="121" width="7" height="33"/><rect x="395" y="127" width="6" height="27"/></g></svg>
      <div class="hero-content">
        <div class="anniversary">
          <div class="anniv-row"><div class="anniv-number">75</div><div class="anniv-ribbon"><span></span><span></span><span></span></div></div>
          <div class="anniv-copy">આઝાદી કા<br>અમૃત મહોત્સવ</div>
        </div>
        <div class="hero-copy">
          <div class="eyebrow">🇮🇳 ભારત • ગુજરાત • કુવાસણા 🇮🇳</div>
          <h1 class="hero-title">કુવાસણા <span class="orange">ગ્રામ પંચાયત</span></h1>
          <div class="hero-subtitle">ડિજિટલ ગ્રામ વિકાસ અને નાગરિક સેવા પોર્ટલ</div>
          <div class="green-line">🌿 સ્વચ્છ કુવાસણા &nbsp; • &nbsp; 🌱 હરિયાળું કુવાસણા &nbsp; • &nbsp; 🏡 ડિજિટલ કુવાસણા</div>
          <div class="motto">“સત્યમેવ જયતે”</div>
          <div class="vande"><span class="orange">Vande</span> <span class="green">Mataram</span></div>
        </div>
        <div class="hero-right">
          <img class="emblem-large" src="https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg" alt="ભારતનું રાષ્ટ્રીય ચિહ્ન">
          <svg class="chakra" viewBox="0 0 120 120" role="img" aria-label="અશોક ચક્ર"><circle cx="60" cy="60" r="53" fill="#fff" fill-opacity=".87" stroke="#183f7b" stroke-width="6"/><circle cx="60" cy="60" r="7" fill="#183f7b"/><circle cx="60" cy="60" r="40" fill="none" stroke="#183f7b" stroke-width="2"/><g stroke="#183f7b" stroke-width="3" transform="translate(60 60)"><line x1="0" y1="-40" x2="0" y2="40"/><line x1="-40" y1="0" x2="40" y2="0"/><line x1="-28" y1="-28" x2="28" y2="28"/><line x1="-28" y1="28" x2="28" y2="-28"/><line x1="-15" y1="-37" x2="15" y2="37"/><line x1="-15" y1="37" x2="15" y2="-37"/><line x1="-37" y1="-15" x2="37" y2="15"/><line x1="-37" y1="15" x2="37" y2="-15"/><line x1="-8" y1="-39" x2="8" y2="39"/><line x1="-39" y1="-8" x2="39" y2="8"/></g></svg>
        </div>
      </div>
      <svg class="india-gate" viewBox="0 0 110 145" aria-hidden="true"><g fill="#a77d4b"><path d="M20 45 L55 12 L90 45Z"/><rect x="18" y="45" width="74" height="12"/><rect x="24" y="57" width="12" height="77"/><rect x="74" y="57" width="12" height="77"/><rect x="15" y="134" width="80" height="8"/><rect x="38" y="62" width="34" height="72" fill="#c09b69"/><path d="M38 134 V97 A17 17 0 0 1 72 97 V134Z" fill="#88623b"/><rect x="12" y="53" width="86" height="5"/></g></svg>
    </section>

    <div class="portal-heading"><span class="rule"></span>અમારા ચાર મુખ્ય પોર્ટલ<span class="rule"></span></div>
    <section class="portals">
      <article class="portal public"><div class="portal-icon">🌐</div><h3>જાહેર માહિતી પોર્ટલ</h3><p>ગામની માહિતી, સમાચાર, નોટિસ અને વિકાસકાર્યો</p><button class="portal-button" onclick="showPage('public',null)">→ જાહેર માહિતી જુઓ</button></article>
      <article class="portal citizen"><div class="portal-icon">👥</div><h3>ગ્રામજન પોર્ટલ</h3><p>ફરિયાદો, પાણીની માહિતી, સ્ટ્રીટલાઇટ અને સૂચનો</p><button class="portal-button" onclick="showPage('citizen',null)">→ ગ્રામજન પોર્ટલ</button></article>
      <article class="portal admin"><div class="portal-icon">🛡️</div><h3>Admin પોર્ટલ</h3><p>ફરિયાદો, નોટિસ અને વિકાસકાર્યોનું સંચાલન</p><button class="portal-button" onclick="showPage('admin',null)">→ Admin પોર્ટલ</button></article>
      <article class="portal officer"><div class="portal-icon">👨‍💼</div><h3>અધિકારી પોર્ટલ</h3><p>સરપંચ, તલાટી અને અધિકૃત કર્મચારીઓ માટે</p><button class="portal-button" onclick="showPage('officer',null)">→ Officer પોર્ટલ</button></article>
    </section>

    <section class="features-panel">
      <div class="feature-heading"><span class="rule"></span>અમારી મુખ્ય સુવિધાઓ<span class="rule"></span></div>
      <div class="feature-grid">
        <div class="feature"><div class="feature-icon pink">📝</div><div class="feature-label">ફરિયાદ વ્યવસ્થાપન</div></div>
        <div class="feature"><div class="feature-icon amber">🏗️</div><div class="feature-label">વિકાસકાર્યો</div></div>
        <div class="feature"><div class="feature-icon mint">💰</div><div class="feature-label">બજેટ અને ખર્ચ</div></div>
        <div class="feature"><div class="feature-icon sky">🗳️</div><div class="feature-label">ડિજિટલ Polls</div></div>
        <div class="feature"><div class="feature-icon leaf">🌱</div><div class="feature-label">Green Kuvasana</div></div>
        <div class="feature"><div class="feature-icon lilac">🤖</div><div class="feature-label">AI Chatbot</div></div>
        <div class="feature"><div class="feature-icon aqua">📊</div><div class="feature-label">Analytics Dashboard</div></div>
        <div class="feature"><div class="feature-icon rose">📱</div><div class="feature-label">મોબાઇલ સુવિધા</div></div>
      </div>
    </section>
  </main>

  <section id="infoPage" class="info-panel" aria-live="polite"><h2 id="infoTitle"></h2><p id="infoText"></p><button class="portal-button" style="background:#0e4b34" onclick="showPage('home',null)">← મુખ્ય પેજ પર પાછા જાઓ</button></section>

  <footer class="footer"><div class="footer-brand">🇮🇳 કુવાસણા ગ્રામ પંચાયત<small>Kuvasana Gram Panchayat</small></div><div class="footer-motto">સત્યમેવ જયતે &nbsp; | &nbsp; વંદે માતરમ્</div><div class="footer-right">ડિજિટલ ગામ &nbsp; | &nbsp; સમૃદ્ધ ભારત<br>આ પ્રોજેક્ટનો ડેમો છે</div></footer>
</div>
<script>
const pages = {
  home: ['મુખ્ય પેજ',''],
  village: ['ગામની માહિતી','કુવાસણા ગામનો પરિચય, જાહેર સુવિધાઓ, મહત્વનાં સ્થળો અને ગામની પ્રમાણિત માહિતી અહીં દર્શાવવામાં આવશે.'],
  development: ['વિકાસકાર્યો','ચાલુ અને પૂર્ણ થયેલાં વિકાસકાર્યો, પ્રગતિ અને પહેલાં-પછીના ફોટા માટે આ વિભાગ છે.'],
  news: ['સમાચાર અને સૂચનાઓ','ગ્રામ પંચાયતની જાહેર નોટિસ, સૂચનાઓ અને સમાચાર અહીં દર્શાવવામાં આવશે.'],
  contact: ['મહત્વનાં સંપર્કો','અહીં પંચાયત કચેરી અને અધિકૃત સંપર્કોની ચકાસેલી માહિતી ઉમેરવામાં આવશે.'],
  public: ['જાહેર માહિતી પોર્ટલ','ગામની માહિતી, જાહેર નોટિસ, સમાચાર અને વિકાસકાર્યો માટેનું પાનું.'],
  citizen: ['ગ્રામજન પોર્ટલ','આ ડેમોમાં માત્ર design ઉપલબ્ધ છે. ફરિયાદ સાચવવી, Complaint ID અને status જોવા માટે database અને સુરક્ષિત login હજી ઉમેરવાના છે.'],
  admin: ['Admin પોર્ટલ','આ ફક્ત demo page છે. સુરક્ષિત authentication ઉમેરાય ત્યાં સુધી અહીં વાસ્તવિક નાગરિકોનો data દાખલ ન કરવો.'],
  officer: ['અધિકારી પોર્ટલ','અધિકારીઓ માટેનું demo page. Login અને permissions આગળના તબક્કામાં ઉમેરવાના છે.']
};
function showPage(key, button) {
  const home = document.getElementById('homePage');
  const info = document.getElementById('infoPage');
  if (key === 'home') { home.classList.remove('hidden'); info.style.display='none'; }
  else { home.classList.add('hidden'); info.style.display='block'; document.getElementById('infoTitle').textContent=pages[key][0]; document.getElementById('infoText').textContent=pages[key][1]; }
  document.querySelectorAll('.nav button').forEach(b=>b.classList.remove('active'));
  if (button) button.classList.add('active');
  window.scrollTo({top:0,behavior:'smooth'});
}
</script>
</body>
</html>'''

components.html(PAGE, height=1170, scrolling=True)

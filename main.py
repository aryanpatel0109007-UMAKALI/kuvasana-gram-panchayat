import streamlit as st

st.set_page_config(
    page_title="કુવાસણા ગ્રામ પંચાયત | Kuvasana Gram Panchayat",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# This is a visual prototype. The emblem image is linked from Wikimedia Commons.
EMBLEM_URL = "https://commons.wikimedia.org/wiki/Special:Redirect/file/Emblem_of_India.svg"
GOLD_EMBLEM_URL = "https://commons.wikimedia.org/wiki/Special:Redirect/file/Emblem_of_India_(gold).svg"

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Gujarati:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --deep-green: #073f2e;
        --leaf-green: #17863b;
        --saffron: #f58220;
        --navy: #173c79;
        --soft-bg: #f7f7f1;
        --ink: #18372b;
    }

    html, body, [class*="css"], .stApp {
        font-family: 'Noto Sans Gujarati', 'Inter', sans-serif;
    }
    .stApp {
        background: var(--soft-bg);
        color: var(--ink);
    }
    header[data-testid="stHeader"] {
        background: transparent;
        height: 0.4rem;
    }
    #MainMenu, footer {visibility: hidden;}
    .block-container {
        max-width: 1540px;
        padding-top: 0.5rem;
        padding-bottom: 1rem;
        padding-left: 1.2rem;
        padding-right: 1.2rem;
    }

    /* Header */
    .site-header {
        min-height: 106px;
        display: flex;
        align-items: center;
        gap: 17px;
        padding: 12px 14px 15px;
        background: rgba(255,255,255,.95);
        border-bottom: 1px solid #e3e5d9;
        border-radius: 0 0 13px 13px;
        position: relative;
        overflow: hidden;
    }
    .header-mark {
        height: 78px;
        width: 66px;
        object-fit: contain;
        flex: 0 0 66px;
        filter: contrast(1.1);
    }
    .brand-copy { min-width: 275px; flex: 1; }
    .brand-copy .guj-brand {
        color: var(--deep-green);
        font-weight: 800;
        font-size: clamp(21px, 2vw, 31px);
        line-height: 1.22;
        margin: 0;
    }
    .brand-copy .eng-brand {font-weight: 750; font-size: 17px; margin-top: 1px;}
    .brand-copy .tagline {font-size: 12px; color: #4b5b50; margin-top: 3px;}
    .header-mini-tricolor {
        position:absolute; top:0; left:0; width:100%; height:6px;
        background:linear-gradient(90deg,#ff9933 0 33.333%,#fff 33.333% 66.666%,#138808 66.666% 100%);
    }
    .st-key-nav_home button, .st-key-nav_village button,
    .st-key-nav_development button, .st-key-nav_news button,
    .st-key-nav_contact button, .st-key-nav_language button {
        background:transparent !important;
        color:#173d30 !important;
        border:0 !important;
        border-radius:0 !important;
        min-height:42px !important;
        padding:5px 4px !important;
        font-weight:650 !important;
        white-space:nowrap !important;
        box-shadow:none !important;
        font-size:13px !important;
    }
    .st-key-nav_home button:hover, .st-key-nav_village button:hover,
    .st-key-nav_development button:hover, .st-key-nav_news button:hover,
    .st-key-nav_contact button:hover, .st-key-nav_language button:hover {
        color:#e66f12 !important;
        border-bottom:3px solid #f58220 !important;
    }

    /* Hero/banner: built in HTML/CSS/SVG rather than a screenshot */
    .hero-banner {
        position:relative;
        isolation:isolate;
        overflow:hidden;
        min-height:365px;
        margin:0 0 14px;
        border-radius:0 0 15px 15px;
        border-bottom:4px solid #fff;
        background:
          radial-gradient(ellipse at 14% 83%, rgba(126,163,86,.45) 0 12%, transparent 37%),
          radial-gradient(ellipse at 75% 80%, rgba(255,194,77,.6) 0 8%, transparent 33%),
          linear-gradient(180deg,#f8f2df 0%,#fff9e9 62%,#f6dba0 100%);
    }
    .hero-landscape {
        position:absolute; inset:auto 0 0 0; width:100%; height:43%; z-index:-1;
    }
    .hero-wave {
        position:absolute; top:0; right:-2%; width:67%; height:80%; z-index:-1;
        opacity:.98;
    }
    .hero-content {
        position:relative;
        display:grid;
        grid-template-columns: 22% 49% 29%;
        align-items:center;
        min-height:365px;
        padding:25px 28px 15px;
        gap:8px;
    }
    .azadi-badge {text-align:center; color:#805822; font-weight:800; padding:8px;}
    .azadi-badge .number {font-family:Georgia,serif; font-weight:800; font-size:clamp(44px,5vw,75px); line-height:.95; color:#987344;}
    .azadi-badge .mini-ribbon {font-size:28px; letter-spacing:2px; line-height:1.1;}
    .azadi-badge .badge-copy {font-size:clamp(16px,1.5vw,23px); line-height:1.35; margin-top:8px;}
    .hero-main {text-align:center; padding:5px 8px 0;}
    .hero-eyebrow {font-size:15px; font-weight:800; color:#1d7d3a; letter-spacing:.4px;}
    .hero-main h1 {font-size:clamp(30px,3.5vw,48px); line-height:1.2; color:#11462e; font-weight:800; margin:9px 0 8px;}
    .hero-main h1 span {color:#e87517;}
    .hero-main h2 {font-size:clamp(18px,2vw,27px); line-height:1.4; color:#174734; margin:0 0 17px; font-weight:750;}
    .hero-green-line {color:#247c34; font-size:clamp(12px,1.15vw,17px); font-weight:800; line-height:1.7;}
    .motto {margin-top:20px; font-size:clamp(20px,2vw,29px); color:#104431; font-weight:800;}
    .vande {font-size:clamp(17px,1.5vw,22px); font-weight:800; margin-top:3px;}
    .vande .orange {color:#ed7918;} .vande .green {color:#187d37;}
    .hero-emblem-box {position:relative; display:flex; justify-content:center; align-items:center; min-height:290px;}
    .hero-emblem {
        width:min(76%,230px); max-height:330px; object-fit:contain;
        filter: sepia(1) saturate(2.8) hue-rotate(350deg) contrast(1.06) drop-shadow(0 9px 6px rgba(64,44,16,.18));
        opacity:.97; position:relative; z-index:2;
    }
    .chakra-wrap {position:absolute; right:-5px; top:6px; z-index:1; width:115px; height:115px; opacity:.98;}
    .hero-slogan-base {font-size:15px;color:#f3cf79;font-weight:800;position:absolute;bottom:5px;left:0;right:0;text-align:center;}

    /* Portal cards */
    .section-heading {
        display:flex; align-items:center; justify-content:center; gap:13px;
        text-align:center; color:#124831; font-weight:800;
        font-size:clamp(21px,2vw,27px); margin:6px 0 15px;
    }
    .heading-rule {display:inline-block; width:62px; height:5px; border-top:2px solid #f58220; border-bottom:2px solid #138808;}
    .portal-card {
        height:190px; border:1px solid rgba(0,0,0,.035); border-radius:15px;
        padding:14px 11px 9px; text-align:center; position:relative; overflow:hidden;
        display:flex; flex-direction:column; align-items:center; justify-content:flex-start;
    }
    .portal-card::after {content:''; position:absolute; width:100px;height:100px;border-radius:50%;right:-20px;bottom:-25px;background:rgba(255,255,255,.40);}
    .portal-card.public {background:linear-gradient(135deg,#f1fbef,#d8f1d6);}
    .portal-card.citizen {background:linear-gradient(135deg,#fff6e9,#ffead4);}
    .portal-card.admin {background:linear-gradient(135deg,#edf6ff,#dceeff);}
    .portal-card.officer {background:linear-gradient(135deg,#f7efff,#e9def9);}
    .portal-icon {
        width:54px;height:54px;border-radius:50%;display:flex;align-items:center;justify-content:center;
        color:#fff;font-size:27px;margin:0 auto 7px;position:relative;z-index:1;
        box-shadow:0 5px 15px rgba(0,0,0,.09);
    }
    .public .portal-icon {background:#07852f;}.citizen .portal-icon{background:#ff730b;}.admin .portal-icon{background:#0755ab;}.officer .portal-icon{background:#6425a1;}
    .portal-card h3 {font-size:clamp(17px,1.45vw,22px);font-weight:800;margin:0 0 7px;position:relative;z-index:1;}
    .public h3{color:#08752c;}.citizen h3{color:#dc6507;}.admin h3{color:#074d9d;}.officer h3{color:#5b2494;}
    .portal-card p {font-size:13px;line-height:1.5;margin:0;position:relative;z-index:1;max-width:260px;}
    .st-key-portal_public button,.st-key-portal_citizen button,.st-key-portal_admin button,.st-key-portal_officer button {
        min-height:40px !important; width:100% !important; border-radius:9px !important;
        border:0 !important; color:#fff !important; font-weight:700 !important; margin-top:-1px !important;
    }
    .st-key-portal_public button {background:#07852f !important;}
    .st-key-portal_citizen button {background:#f06c0a !important;}
    .st-key-portal_admin button {background:#0755ab !important;}
    .st-key-portal_officer button {background:#6425a1 !important;}
    .st-key-portal_public button:hover,.st-key-portal_citizen button:hover,.st-key-portal_admin button:hover,.st-key-portal_officer button:hover {filter:brightness(.92);}

    /* Feature strip */
    .feature-strip {background:rgba(255,255,255,.90); border:1px solid #e5e7df; border-radius:15px; padding:12px 9px 8px; box-shadow:0 3px 14px rgba(22,50,34,.035);}
    .feature-grid {display:grid;grid-template-columns:repeat(8,minmax(0,1fr));}
    .feature-item {text-align:center; min-height:82px; padding:7px 3px 0; border-right:1px solid #d9dfd5;}
    .feature-item:last-child {border-right:0;}
    .feature-icon {height:49px;width:49px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:23px;margin:0 auto 7px;}
    .feature-label {color:#18392a;font-size:12px;font-weight:750;line-height:1.35;}
    .f-pink{background:#ffccd0;color:#d33d53}.f-orange{background:#ffebc5;color:#d27a12}.f-green{background:#d6f0d2;color:#22813b}.f-blue{background:#d5ebff;color:#1970bd}.f-lime{background:#d8efc9;color:#34843c}.f-purple{background:#ead8ff;color:#7a42af}.f-cyan{background:#cfeef2;color:#218da0}.f-red{background:#ffd5dd;color:#d62852}
    .footer-bar {background:#073f2e;color:#fff;border-radius:0 0 12px 12px;padding:16px 20px;margin-top:14px;display:flex;align-items:center;justify-content:space-between;gap:12px;}
    .footer-name {font-size:15px;font-weight:800;}.footer-sub {font-size:11px;opacity:.85;}.footer-motto{font-weight:700;font-size:15px;text-align:center;}.footer-right{font-size:12px;text-align:right;}
    .page-info {background:#fff;border:1px solid #dfe8dc;border-radius:15px;padding:22px;margin:14px 0;}

    @media (max-width: 1050px) {
        .hero-content {grid-template-columns:17% 53% 30%;padding:20px 12px;}
        .hero-emblem {width:78%;}
        .chakra-wrap{width:80px;height:80px;right:-8px;}
        .portal-card{height:205px;}
        .portal-card p{font-size:12px;}
    }
    @media (max-width: 720px) {
        .block-container{padding-left:.55rem;padding-right:.55rem;}
        .site-header{flex-wrap:wrap;gap:8px;}
        .brand-copy{min-width:180px;}
        .header-mark{height:58px;width:48px;flex-basis:48px;}
        .hero-content{grid-template-columns:1fr;min-height:unset;padding:25px 14px;}
        .hero-banner{min-height:unset;}
        .azadi-badge{display:none;}
        .hero-main h1{font-size:31px;}
        .hero-emblem-box{min-height:130px;}
        .hero-emblem{width:90px;max-height:120px;}
        .chakra-wrap{width:62px;height:62px;right:10%;top:0;}
        .portal-card{height:192px;}
        .feature-label{font-size:10px;}
        .feature-grid{grid-template-columns:repeat(4,minmax(0,1fr));}
        .feature-item:nth-child(4n){border-right:0;}
        .footer-bar{flex-direction:column;text-align:center;}
        .footer-right{text-align:center;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Session navigation state
if "page" not in st.session_state:
    st.session_state.page = "home"


def go(page_name: str) -> None:
    st.session_state.page = page_name

# Top header: real page buttons with a visual style matching the reference design.
st.markdown('<div class="header-mini-tricolor"></div>', unsafe_allow_html=True)
h_logo, h_brand, h_nav, h_lang = st.columns([0.65, 2.25, 4.3, 0.65], vertical_alignment="center")
with h_logo:
    st.markdown(
        f'<div style="text-align:center;padding-top:11px"><img class="header-mark" src="{EMBLEM_URL}" alt="ભારતનું રાષ્ટ્રીય ચિહ્ન"></div>',
        unsafe_allow_html=True,
    )
with h_brand:
    st.markdown(
        """
        <div class="brand-copy" style="padding-top:9px">
          <div class="guj-brand">કુવાસણા ગ્રામ પંચાયત</div>
          <div class="eng-brand">Kuvasana Gram Panchayat</div>
          <div class="tagline">Digital Village | Smart Governance | Better Tomorrow</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with h_nav:
    nav_cols = st.columns(5, gap="small")
    nav_buttons = [
        ("⌂  મુખ્ય પેજ", "home", "nav_home"),
        ("▣  ગામની માહિતી", "village", "nav_village"),
        ("▧  વિકાસકાર્યો", "development", "nav_development"),
        ("▤  સમાચાર", "news", "nav_news"),
        ("☎  સંપર્ક", "contact", "nav_contact"),
    ]
    for col, (label, page_name, key) in zip(nav_cols, nav_buttons):
        with col:
            st.button(label, key=key, on_click=go, args=(page_name,))
with h_lang:
    st.markdown('<div style="text-align:center;font-size:15px;padding-top:10px">🇮🇳<br>ગુજરાતી</div>', unsafe_allow_html=True)

# Hero banner with layered SVG landscape and three-col composition.
hero_svg = """
<svg class="hero-landscape" viewBox="0 0 1400 220" preserveAspectRatio="none" aria-hidden="true">
  <defs>
    <linearGradient id="hillA" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7c9c58"/><stop offset="1" stop-color="#315b38"/></linearGradient>
    <linearGradient id="skySun" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f9d47a"/><stop offset="1" stop-color="#fff3ce"/></linearGradient>
  </defs>
  <circle cx="1050" cy="70" r="38" fill="url(#skySun)" opacity=".92"/>
  <path d="M0 115 Q120 62 235 105 T470 92 T720 118 T970 90 T1210 105 T1400 88 L1400 220 L0 220Z" fill="#b2c68f" opacity=".62"/>
  <path d="M0 145 Q150 80 310 140 T620 125 T900 146 T1160 118 T1400 135 L1400 220 L0 220Z" fill="url(#hillA)" opacity=".65"/>
  <path d="M0 170 Q190 120 360 166 T730 151 T1050 167 T1400 150 L1400 220 L0 220Z" fill="#315a37" opacity=".9"/>
  <g fill="#f2e4bd" stroke="#b89b69" stroke-width="2" opacity=".95">
    <path d="M50 172 l38 -29 38 29 v30 H50Z"/><path d="M40 173 L88 135 L137 173Z" fill="#c57c40"/>
    <path d="M155 181 l28 -21 30 21 v24 H155Z"/><path d="M147 181 L183 151 L221 181Z" fill="#b76530"/>
    <path d="M1180 174 l38 -29 39 29 v31 H1180Z"/><path d="M1172 175 L1218 136 L1259 175Z" fill="#bc743c"/>
    <path d="M1290 181 l31 -23 30 23 v24 H1290Z"/><path d="M1282 181 L1321 151 L1357 181Z" fill="#b86d35"/>
  </g>
  <g fill="#275332" opacity=".9"><circle cx="24" cy="184" r="15"/><circle cx="143" cy="190" r="18"/><circle cx="265" cy="182" r="17"/><circle cx="1100" cy="190" r="18"/><circle cx="1264" cy="188" r="20"/><circle cx="1380" cy="182" r="18"/></g>
  <g fill="#dce7c7" opacity=".8"><rect x="72" y="184" width="7" height="18"/><rect x="180" y="188" width="7" height="16"/><rect x="1210" y="183" width="7" height="19"/><rect x="1315" y="187" width="7" height="16"/></g>
</svg>
<svg class="hero-wave" viewBox="0 0 900 450" preserveAspectRatio="none" aria-hidden="true">
  <path d="M120 0 C260 75 350 100 495 45 S740 105 900 15 L900 95 C740 165 630 105 490 100 S270 155 120 70Z" fill="#ff9933"/>
  <path d="M0 165 C180 130 300 220 475 195 S710 185 900 140 L900 230 C715 275 600 265 455 260 S170 205 0 250Z" fill="#138808" opacity=".94"/>
  <path d="M190 85 C315 138 365 148 495 115 S740 165 900 105 L900 140 C720 200 620 160 488 164 S300 155 190 120Z" fill="#ffffff" opacity=".88"/>
</svg>
"""

st.markdown(
    f"""
    <section class="hero-banner">
      {hero_svg}
      <div class="hero-content">
        <div class="azadi-badge">
          <div class="number">75</div>
          <div class="mini-ribbon">〰️</div>
          <div class="badge-copy">આઝાદી કા<br>અમૃત મહોત્સવ</div>
        </div>
        <div class="hero-main">
          <div class="hero-eyebrow">🇮🇳 ભારત • ગુજરાત • કુવાસણા 🇮🇳</div>
          <h1>કુવાસણા <span>ગ્રામ પંચાયત</span></h1>
          <h2>ડિજિટલ ગ્રામ વિકાસ અને નાગરિક સેવા પોર્ટલ</h2>
          <div class="hero-green-line">🌿 સ્વચ્છ કુવાસણા &nbsp; • &nbsp; 🌱 હરિયાળું કુવાસણા &nbsp; • &nbsp; 🏡 ડિજિટલ કુવાસણા</div>
          <div class="motto">“સત્યમેવ જયતે”</div>
          <div class="vande"><span class="orange">Vande</span> <span class="green">Mataram</span> 🇮🇳</div>
        </div>
        <div class="hero-emblem-box">
          <img class="hero-emblem" src="{GOLD_EMBLEM_URL}" alt="અશોક સ્તંભનું રાષ્ટ્રીય ચિહ્ન">
          <div class="chakra-wrap">
            <svg viewBox="0 0 240 240" width="100%" height="100%" aria-label="અશોક ચક્ર">
              <circle cx="120" cy="120" r="108" fill="#ffffff" fill-opacity=".8" stroke="#183b70" stroke-width="10"/>
              <circle cx="120" cy="120" r="14" fill="#183b70"/>
              <g stroke="#183b70" stroke-width="5" stroke-linecap="round">
                <line x1="120" y1="26" x2="120" y2="214"/>
                <line x1="120" y1="26" x2="120" y2="214" transform="rotate(15 120 120)"/>
                <line x1="120" y1="26" x2="120" y2="214" transform="rotate(30 120 120)"/>
                <line x1="120" y1="26" x2="120" y2="214" transform="rotate(45 120 120)"/>
                <line x1="120" y1="26" x2="120" y2="214" transform="rotate(60 120 120)"/>
                <line x1="120" y1="26" x2="120" y2="214" transform="rotate(75 120 120)"/>
                <line x1="120" y1="26" x2="120" y2="214" transform="rotate(90 120 120)"/>
                <line x1="120" y1="26" x2="120" y2="214" transform="rotate(105 120 120)"/>
                <line x1="120" y1="26" x2="120" y2="214" transform="rotate(120 120 120)"/>
                <line x1="120" y1="26" x2="120" y2="214" transform="rotate(135 120 120)"/>
                <line x1="120" y1="26" x2="120" y2="214" transform="rotate(150 120 120)"/>
                <line x1="120" y1="26" x2="120" y2="214" transform="rotate(165 120 120)"/>
              </g>
              <circle cx="120" cy="120" r="87" fill="none" stroke="#183b70" stroke-width="3"/>
            </svg>
          </div>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# Main four portals: cards plus working in-app demo navigation.
st.markdown(
    '<div class="section-heading"><span class="heading-rule"></span>અમારા ચાર મુખ્ય પોર્ટલ<span class="heading-rule"></span></div>',
    unsafe_allow_html=True,
)
portal_cols = st.columns(4, gap="medium")
portals = [
    ("public", "🌐", "જાહેર માહિતી પોર્ટલ", "ગામની માહિતી, સમાચાર, નોટિસ અને વિકાસકાર્યો", "જુઓ", "public"),
    ("citizen", "👨‍👩‍👧", "ગ્રામજન પોર્ટલ", "ફરિયાદો, પાણીની માહિતી, સ્ટ્રીટલાઇટ અને સૂચનો", "લોગિન કરો", "citizen"),
    ("admin", "🛡️", "Admin પોર્ટલ", "ફરિયાદો, નોટિસ, વિકાસકાર્યો અને સભ્યોનું સંચાલન", "લોગિન કરો", "admin"),
    ("officer", "🧑‍💼", "અધિકારી પોર્ટલ", "સરપંચ, તલાટી અને અધિકૃત કર્મચારીઓ માટે", "લોગિન કરો", "officer"),
]
for col, (slug, icon, title, description, button_label, target) in zip(portal_cols, portals):
    with col:
        st.markdown(
            f"""
            <div class="portal-card {slug}">
              <div class="portal-icon">{icon}</div>
              <h3>{title}</h3>
              <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button(button_label, key=f"portal_{slug}", on_click=go, args=(target,))

# Feature strip
st.markdown(
    '<div class="section-heading" style="margin-top:18px"><span class="heading-rule"></span>અમારી મુખ્ય સુવિધાઓ<span class="heading-rule"></span></div>',
    unsafe_allow_html=True,
)
features = [
    ("📝", "ફરિયાદ વ્યવસ્થાપન", "f-pink"),
    ("🏗️", "વિકાસકાર્યો", "f-orange"),
    ("💰", "બજેટ અને ખર્ચ", "f-green"),
    ("🗳️", "ડિજિટલ મતદાન", "f-blue"),
    ("🌱", "Green Kuvasana", "f-lime"),
    ("🤖", "AI ચેટબોટ", "f-purple"),
    ("📊", "Analytics ડેશબોર્ડ", "f-cyan"),
    ("📱", "મોબાઇલ સુવિધા", "f-red"),
]
feature_items_html = "".join(
    f'<div class="feature-item"><div class="feature-icon {color_class}">{icon}</div>'
    f'<div class="feature-label">{label}</div></div>'
    for icon, label, color_class in features
)
st.markdown(
    f'<div class="feature-strip"><div class="feature-grid">{feature_items_html}</div></div>',
    unsafe_allow_html=True,
)

# Prototype page content. These are intentionally demo-only; no login/database yet.
page = st.session_state.page
page_titles = {
    "public": "🌐 જાહેર માહિતી પોર્ટલ",
    "citizen": "👨‍👩‍👧 ગ્રામજન પોર્ટલ",
    "admin": "🛡️ Admin પોર્ટલ",
    "officer": "🧑‍💼 અધિકારી પોર્ટલ",
    "village": "🏡 ગામની માહિતી",
    "development": "🏗️ વિકાસકાર્યો",
    "news": "📢 સમાચાર અને સૂચનાઓ",
    "contact": "☎ સંપર્ક માહિતી",
}
if page != "home":
    st.markdown('<div class="page-info">', unsafe_allow_html=True)
    st.subheader(page_titles.get(page, "કુવાસણા ગ્રામ પંચાયત"))
    messages = {
        "public": "અહીં ગામની માહિતી, જાહેર નોટિસ, સમાચાર અને વિકાસકાર્યો બતાવી શકાય છે.",
        "citizen": "આ ડિઝાઇન પ્રોટોટાઇપ છે. સુરક્ષિત નાગરિક login અને ફરિયાદ નોંધણી હજી બનાવવાની બાકી છે.",
        "admin": "આ ડિઝાઇન પ્રોટોટાઇપ છે. Admin login, roles અને permission સુરક્ષા હજી બનાવવાની બાકી છે.",
        "officer": "આ ડિઝાઇન પ્રોટોટાઇપ છે. અધિકારીઓ માટે સુરક્ષિત login અને જવાબદારી આધારિત સુવિધાઓ હજી બનાવવાની બાકી છે.",
        "village": "અહીં ગામનો પરિચય, જાહેર સુવિધાઓ, ઇતિહાસ અને ઉપયોગી માહિતી ઉમેરવામાં આવશે.",
        "development": "અહીં મંજૂર વિકાસકાર્યો, હાલની પ્રગતિ અને પૂર્ણ થયેલાં કાર્યોની વિગતો દેખાડવામાં આવશે.",
        "news": "અહીં ગ્રામ પંચાયતની જાહેર નોટિસો અને સમાચાર દર્શાવવામાં આવશે.",
        "contact": "અહીં અધિકૃત રીતે મંજૂર સરપંચ, તલાટી-કમ-મંત્રી અને કચેરીના સંપર્ક ઉમેરવામાં આવશે.",
    }
    st.write(messages.get(page, "આ વિભાગ તૈયાર થઈ રહ્યો છે."))
    if page in ("admin", "officer", "citizen"):
        st.warning("હાલમાં અહીં login કાર્યરત નથી. જાહેર ઉપયોગ પહેલાં authentication અને database સુરક્ષા ઉમેરવી જરૂરી છે.")
    st.button("← મુખ્ય પેજ પર પાછા જાઓ", key="back_home", on_click=go, args=("home",))
    st.markdown('</div>', unsafe_allow_html=True)

# Footer matching the reference image.
st.markdown(
    """
    <div class="footer-bar">
      <div>
        <div class="footer-name">🏛️ કુવાસણા ગ્રામ પંચાયત</div>
        <div class="footer-sub">Kuvasana Gram Panchayat</div>
      </div>
      <div class="footer-motto">સત્યમેવ જયતે &nbsp; | &nbsp; વંદે માતરમ્</div>
      <div class="footer-right">ડિજિટલ ગામ &nbsp; | &nbsp; સમૃદ્ધ ભારત 🇮🇳</div>
    </div>
    <div style="text-align:center;color:#788278;font-size:10px;padding:7px 4px">
      પ્રોટોટાઇપ ડિઝાઇન — આ સત્તાવાર સરકારી વેબસાઇટ નથી.
    </div>
    """,
    unsafe_allow_html=True,
)

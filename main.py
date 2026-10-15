import streamlit as st

st.set_page_config(
    page_title="કુવાસણા ગ્રામ પંચાયત | Kuvasana Gram Panchayat",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

EMBLEM_URL = "https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg"

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Gujarati:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --green: #104b33;
        --leaf: #16853e;
        --saffron: #f58220;
        --navy: #173f7a;
        --ink: #17392b;
        --paper: #fbfaf5;
    }

    html, body, [class*="css"], .stApp {
        font-family: 'Noto Sans Gujarati', 'Inter', sans-serif;
    }
    .stApp { background: var(--paper); color: var(--ink); }
    header[data-testid="stHeader"] { background: transparent; }
    #MainMenu, footer { visibility: hidden; }
    div[data-testid="stToolbar"] { visibility: hidden; height: 0; }
    .block-container { max-width: 1550px; padding: .35rem 1rem 1rem; }

    .tricolor-top {
        height: 6px; border-radius: 5px;
        background: linear-gradient(90deg,#ff9933 0 33.333%,#fff 33.333% 66.666%,#138808 66.666% 100%);
        box-shadow: 0 1px 0 #e8e6df;
    }
    .brand-wrap { display:flex; flex-direction:column; justify-content:center; min-height:78px; padding:3px 0; }
    .brand-guj { font-size:clamp(20px,2vw,30px); font-weight:800; line-height:1.22; color:var(--green); }
    .brand-eng { font-size:15px; font-weight:800; color:#1f3a2d; margin-top:2px; }
    .brand-tag { font-size:11px; color:#66746a; margin-top:4px; }
    .header-emblem { height:68px; width:auto; max-width:100%; object-fit:contain; }
    .language-mark { text-align:center; color:var(--green); font-size:13px; padding-top:15px; }

    .st-key-nav_home button, .st-key-nav_village button,
    .st-key-nav_development button, .st-key-nav_news button,
    .st-key-nav_contact button {
        width:100%; background:transparent !important; color:#244936 !important;
        border:0 !important; border-radius:0 !important; box-shadow:none !important;
        font-size:12px !important; font-weight:700 !important; min-height:38px !important;
        padding:3px 2px !important; white-space:nowrap !important;
    }
    .st-key-nav_home button:hover, .st-key-nav_village button:hover,
    .st-key-nav_development button:hover, .st-key-nav_news button:hover,
    .st-key-nav_contact button:hover {
        color:#d56e16 !important; border-bottom:3px solid #ff9933 !important;
    }

    /* The hero is a responsive three-column layout. The SVG is only artwork behind it. */
    .hero {
        position:relative; isolation:isolate; overflow:hidden;
        margin:10px 0 15px; border:1px solid #e9e1d1; border-bottom:5px solid #138808;
        border-radius:18px; min-height:326px;
        background:linear-gradient(115deg,#fff9ec 0%,#fffdf7 47%,#fff4dc 100%);
        box-shadow:0 5px 18px rgba(25,61,37,.045);
    }
    .hero-art { position:absolute; inset:0; width:100%; height:100%; z-index:-1; pointer-events:none; }
    .hero-grid {
        display:grid; grid-template-columns:16% 56% 28%; align-items:center;
        min-height:326px; padding:20px 20px 22px; gap:7px;
    }
    .azadi { text-align:center; color:#8e682f; padding:0 4px; }
    .azadi-number { font-family:Georgia,serif; font-size:clamp(48px,4.7vw,71px); line-height:.95; color:#997749; }
    .azadi-wave { color:#e48a1d; font-size:22px; letter-spacing:3px; line-height:1; }
    .azadi-label { font-size:clamp(14px,1.25vw,19px); font-weight:800; line-height:1.45; margin-top:7px; }
    .hero-copy { text-align:center; min-width:0; padding:3px 5px; }
    .hero-eyebrow { color:#247c43; font-size:13px; font-weight:800; margin-bottom:5px; }
    .hero-title { color:#0d5138; font-size:clamp(27px,3vw,45px); line-height:1.25; font-weight:800; margin:0 0 8px; }
    .hero-title .saffron { color:#e87517; }
    .hero-subtitle { color:#244d39; font-size:clamp(17px,1.75vw,25px); font-weight:750; line-height:1.4; margin-bottom:7px; }
    .hero-village { color:#237a37; font-size:clamp(11px,1.07vw,15px); font-weight:800; line-height:1.8; }
    .hero-satyam { color:#124b34; font-size:clamp(21px,1.9vw,28px); font-weight:800; margin-top:8px; }
    .hero-vande { font-size:clamp(16px,1.45vw,21px); font-weight:800; margin-top:1px; }
    .hero-vande .orange { color:#e87517; } .hero-vande .green { color:#16813c; }
    .hero-symbols { display:flex; height:100%; align-items:center; justify-content:center; gap:12px; padding:4px 4px 28px; }
    .hero-emblem { height:188px; width:auto; max-width:64%; object-fit:contain; filter:brightness(0) saturate(100%) invert(62%) sepia(32%) saturate(825%) hue-rotate(2deg) brightness(92%) contrast(94%); }
    .chakra { width:72px; height:72px; flex-shrink:0; border:4px solid #173f7a; border-radius:50%; color:#173f7a; display:flex; align-items:center; justify-content:center; font-size:43px; background:rgba(255,255,255,.86); box-shadow:0 3px 10px rgba(23,63,122,.10); }

    .section-heading { display:flex; align-items:center; justify-content:center; gap:12px; color:#124831; font-size:clamp(20px,1.9vw,27px); font-weight:800; text-align:center; margin:9px 0 13px; }
    .rule { height:5px; width:58px; flex-shrink:0; border-top:2px solid #ff9933; border-bottom:2px solid #138808; }
    .portal-card { border:1px solid rgba(0,0,0,.035); border-radius:14px; text-align:center; min-height:171px; padding:12px 10px 9px; }
    .portal-card.public { background:linear-gradient(145deg,#f2fbef,#dcf3d8); }
    .portal-card.citizen { background:linear-gradient(145deg,#fff8ed,#ffecd7); }
    .portal-card.admin { background:linear-gradient(145deg,#f0f7ff,#deefff); }
    .portal-card.officer { background:linear-gradient(145deg,#faf4ff,#eadef8); }
    .portal-icon { width:49px; height:49px; display:flex; align-items:center; justify-content:center; margin:0 auto 6px; border-radius:50%; color:white; font-size:25px; box-shadow:0 3px 9px rgba(0,0,0,.08); }
    .public .portal-icon { background:#07852f; } .citizen .portal-icon { background:#f06c0a; }
    .admin .portal-icon { background:#0755ab; } .officer .portal-icon { background:#6425a1; }
    .portal-card h3 { font-size:clamp(15px,1.25vw,19px); line-height:1.35; margin:0 0 4px; font-weight:800; }
    .public h3 {color:#08752c}.citizen h3 {color:#dc6507}.admin h3 {color:#074d9d}.officer h3 {color:#5b2494}
    .portal-card p { font-size:11px; line-height:1.45; margin:0; min-height:33px; }
    .st-key-portal_public button, .st-key-portal_citizen button, .st-key-portal_admin button, .st-key-portal_officer button {
        width:100% !important; min-height:36px !important; border:0 !important; border-radius:8px !important;
        color:white !important; font-weight:750 !important; font-size:13px !important; margin-top:-3px;
    }
    .st-key-portal_public button {background:#07852f!important}.st-key-portal_citizen button {background:#f06c0a!important}
    .st-key-portal_admin button {background:#0755ab!important}.st-key-portal_officer button {background:#6425a1!important}

    .features { background:rgba(255,255,255,.94); border:1px solid #e4e8dd; border-radius:14px; padding:8px 6px 5px; box-shadow:0 3px 13px rgba(22,50,34,.03); }
    .feature-grid { display:grid; grid-template-columns:repeat(8,minmax(0,1fr)); }
    .feature { min-width:0; text-align:center; min-height:75px; padding:7px 4px 3px; border-right:1px solid #dce1d8; }
    .feature:last-child { border-right:0; }
    .feature-icon { width:43px; height:43px; display:flex; align-items:center; justify-content:center; font-size:21px; border-radius:50%; margin:0 auto 5px; }
    .feature-label { font-size:10px; line-height:1.35; font-weight:750; color:#183a2b; }
    .pink{background:#ffdade}.amber{background:#ffedca}.mint{background:#d9f1d3}.sky{background:#d8eeff}.leaf{background:#def1d0}.lilac{background:#ecdfff}.aqua{background:#d3f0f2}.rose{background:#ffe0e6}

    .footer { display:flex; align-items:center; justify-content:space-between; gap:10px; margin-top:13px; padding:13px 18px; color:#fff; background:#073f2e; border-radius:11px; }
    .footer-brand { font-size:13px; font-weight:800; }.footer-small {font-size:10px;opacity:.83}.footer-motto {font-size:14px;font-weight:800;text-align:center}.footer-right{font-size:11px;text-align:right}
    .page-info {background:#fff;border:1px solid #e0e8dd;border-radius:14px;padding:20px;margin:12px 0}

    @media(max-width:1050px) {
        .hero-grid {grid-template-columns:14% 58% 28%;padding:17px 10px}
        .hero-emblem {height:158px;max-width:60%}.chakra{width:57px;height:57px;font-size:34px}
        .portal-card{min-height:182px}
    }
    @media(max-width:740px) {
        .block-container{padding-left:.55rem;padding-right:.55rem}
        .hero-grid{grid-template-columns:1fr;gap:8px;padding:17px 12px}
        .hero{min-height:0}
        .azadi{display:none}
        .hero-copy{padding:10px 3px}
        .hero-title{font-size:30px}.hero-subtitle{font-size:18px}
        .hero-symbols{padding:4px;gap:14px}.hero-emblem{height:110px;max-width:44%}
        .chakra{width:58px;height:58px;font-size:34px}
        .feature-grid{grid-template-columns:repeat(4,minmax(0,1fr))}
        .feature:nth-child(4n){border-right:0}
        .footer{flex-direction:column;text-align:center}.footer-right{text-align:center}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "page" not in st.session_state:
    st.session_state.page = "home"


def go(page_name: str) -> None:
    st.session_state.page = page_name

# Header
st.markdown('<div class="tricolor-top"></div>', unsafe_allow_html=True)
logo_col, brand_col, nav_col, lang_col = st.columns([0.55, 2.35, 4.5, 0.55], vertical_alignment="center")
with logo_col:
    st.markdown(
        f'<div style="text-align:center;padding:3px 0"><img class="header-emblem" src="{EMBLEM_URL}" alt="ભારતનું રાષ્ટ્રીય ચિહ્ન"></div>',
        unsafe_allow_html=True,
    )
with brand_col:
    st.markdown(
        """
        <div class="brand-wrap">
          <div class="brand-guj">કુવાસણા ગ્રામ પંચાયત</div>
          <div class="brand-eng">Kuvasana Gram Panchayat</div>
          <div class="brand-tag">Digital Village | Smart Governance | Better Tomorrow</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with nav_col:
    nav_cols = st.columns(5, gap="small")
    nav_buttons = [
        ("⌂ મુખ્ય પેજ", "home", "nav_home"),
        ("▣ ગામની માહિતી", "village", "nav_village"),
        ("▧ વિકાસકાર્યો", "development", "nav_development"),
        ("▤ સમાચાર", "news", "nav_news"),
        ("☎ સંપર્ક", "contact", "nav_contact"),
    ]
    for col, (label, page_name, key) in zip(nav_cols, nav_buttons):
        with col:
            st.button(label, key=key, on_click=go, args=(page_name,))
with lang_col:
    st.markdown('<div class="language-mark">🇮🇳<br>ગુજરાતી</div>', unsafe_allow_html=True)

# Hero banner with a soft tricolour wave and a simple village landscape illustration.
st.markdown(
    f"""
    <section class="hero">
      <svg class="hero-art" viewBox="0 0 1500 340" preserveAspectRatio="none" aria-hidden="true">
        <defs>
          <linearGradient id="sunGlow" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#ffe7b0" stop-opacity=".4"/>
            <stop offset="100%" stop-color="#fff9ec" stop-opacity="0"/>
          </linearGradient>
        </defs>
        <rect width="1500" height="340" fill="url(#sunGlow)"/>
        <circle cx="1290" cy="105" r="44" fill="#fff8db" opacity=".9"/>
        <path d="M780 0 C980 40 1180 40 1500 0 L1500 72 C1240 138 1060 76 830 114 Z" fill="#ff9933" opacity=".88"/>
        <path d="M765 92 C1000 130 1225 150 1500 82 L1500 153 C1260 200 1025 160 790 184 Z" fill="#ffffff" opacity=".95"/>
        <path d="M795 177 C1030 202 1250 225 1500 157 L1500 255 C1255 292 1045 258 820 280 Z" fill="#138808" opacity=".9"/>
        <path d="M0 278 C160 245 270 260 410 278 C545 296 650 285 770 270 L850 340 L0 340 Z" fill="#d8e6bf" opacity=".62"/>
        <path d="M0 310 C160 275 280 296 420 310 C555 326 690 304 850 294 L920 340 L0 340 Z" fill="#99bf76" opacity=".52"/>
        <path d="M0 325 C175 300 320 325 470 330 C625 334 720 318 870 318 L930 340 L0 340 Z" fill="#4a9650" opacity=".50"/>
        <g opacity=".52" fill="#7c9a63">
          <rect x="60" y="267" width="42" height="25" rx="2"/><path d="M52 267 L81 247 L110 267 Z"/>
          <rect x="119" y="279" width="37" height="20" rx="2"/><path d="M111 279 L137 261 L164 279 Z"/>
          <rect x="215" y="271" width="47" height="24" rx="2"/><path d="M206 271 L239 249 L270 271 Z"/>
          <rect x="305" y="284" width="37" height="19" rx="2"/><path d="M298 284 L324 267 L349 284 Z"/>
          <rect x="390" y="275" width="45" height="23" rx="2"/><path d="M381 275 L412 253 L444 275 Z"/>
        </g>
        <g opacity=".58" fill="#4c8750">
          <circle cx="185" cy="270" r="18"/><rect x="181" y="269" width="8" height="30"/>
          <circle cx="276" cy="281" r="15"/><rect x="272" y="280" width="7" height="23"/>
          <circle cx="360" cy="270" r="20"/><rect x="355" y="269" width="9" height="32"/>
          <circle cx="475" cy="288" r="16"/><rect x="471" y="287" width="8" height="20"/>
        </g>
        <g transform="translate(1350,225)" fill="#b98e50" opacity=".62">
          <rect x="-25" y="-8" width="50" height="80"/>
          <rect x="-35" y="-15" width="70" height="10"/>
          <rect x="-16" y="8" width="32" height="62" fill="#f2d39b"/>
          <path d="M-45 -15 L0 -48 L45 -15 Z"/>
          <rect x="-6" y="32" width="12" height="40" fill="#956b3e"/>
        </g>
      </svg>
      <div class="hero-grid">
        <div class="azadi">
          <div class="azadi-number">75</div>
          <div class="azadi-wave">〰〰〰</div>
          <div class="azadi-label">આઝાદી કા<br>અમૃત મહોત્સવ</div>
        </div>
        <div class="hero-copy">
          <div class="hero-eyebrow">🇮🇳 ભારત • ગુજરાત • કુવાસણા 🇮🇳</div>
          <div class="hero-title">કુવાસણા <span class="saffron">ગ્રામ પંચાયત</span></div>
          <div class="hero-subtitle">ડિજિટલ ગ્રામ વિકાસ અને નાગરિક સેવા પોર્ટલ</div>
          <div class="hero-village">🌿 સ્વચ્છ કુવાસણા &nbsp; • &nbsp; 🌱 હરિયાળું કુવાસણા &nbsp; • &nbsp; 🏡 ડિજિટલ કુવાસણા</div>
          <div class="hero-satyam">“સત્યમેવ જયતે”</div>
          <div class="hero-vande"><span class="orange">Vande</span> <span class="green">Mataram</span> 🇮🇳</div>
        </div>
        <div class="hero-symbols">
          <img class="hero-emblem" src="{EMBLEM_URL}" alt="ભારતનું રાષ્ટ્રીય ચિહ્ન">
          <div class="chakra">☸</div>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-heading"><span class="rule"></span>અમારા ચાર મુખ્ય પોર્ટલ<span class="rule"></span></div>',
    unsafe_allow_html=True,
)

portal_cols = st.columns(4, gap="medium")
portals = [
    ("public", "🌐", "જાહેર માહિતી પોર્ટલ", "ગામની માહિતી, સમાચાર, નોટિસ અને વિકાસકાર્યો", "જાહેર પેજ જુઓ", "public"),
    ("citizen", "👨‍👩‍👧", "ગ્રામજન પોર્ટલ", "ફરિયાદો, પાણીની માહિતી, સ્ટ્રીટલાઇટ અને સૂચનો", "ગ્રામજન પોર્ટલ", "citizen"),
    ("admin", "🛡️", "Admin પોર્ટલ", "ફરિયાદો, નોટિસ, વિકાસકાર્યો અને સભ્યોનું સંચાલન", "Admin પોર્ટલ", "admin"),
    ("officer", "🧑‍💼", "અધિકારી પોર્ટલ", "સરપંચ, તલાટી અને અધિકૃત કર્મચારીઓ માટે", "Officer પોર્ટલ", "officer"),
]
for col, (slug, icon, title, description, button_label, target) in zip(portal_cols, portals):
    with col:
        st.markdown(
            f'<div class="portal-card {slug}"><div class="portal-icon">{icon}</div><h3>{title}</h3><p>{description}</p></div>',
            unsafe_allow_html=True,
        )
        st.button(button_label, key=f"portal_{slug}", on_click=go, args=(target,))

st.markdown(
    '<div class="section-heading" style="margin-top:16px"><span class="rule"></span>અમારી મુખ્ય સુવિધાઓ<span class="rule"></span></div>',
    unsafe_allow_html=True,
)
features = [
    ("📝", "ફરિયાદ વ્યવસ્થાપન", "pink"),
    ("🏗️", "વિકાસકાર્યો", "amber"),
    ("💰", "બજેટ અને ખર્ચ", "mint"),
    ("🗳️", "ડિજિટલ મતદાન", "sky"),
    ("🌱", "Green Kuvasana", "leaf"),
    ("🤖", "AI ચેટબોટ", "lilac"),
    ("📊", "Analytics ડેશબોર્ડ", "aqua"),
    ("📱", "મોબાઇલ સુવિધા", "rose"),
]
feature_html = "".join(
    f'<div class="feature"><div class="feature-icon {color}">{icon}</div><div class="feature-label">{label}</div></div>'
    for icon, label, color in features
)
st.markdown(f'<div class="features"><div class="feature-grid">{feature_html}</div></div>', unsafe_allow_html=True)

# Demo navigation pages
page = st.session_state.page
page_titles = {
    "public": "🌐 જાહેર માહિતી પોર્ટલ", "citizen": "👨‍👩‍👧 ગ્રામજન પોર્ટલ",
    "admin": "🛡️ Admin પોર્ટલ", "officer": "🧑‍💼 અધિકારી પોર્ટલ",
    "village": "🏡 ગામની માહિતી", "development": "🏗️ વિકાસકાર્યો",
    "news": "📢 સમાચાર અને સૂચનાઓ", "contact": "☎ સંપર્ક માહિતી",
}
page_messages = {
    "public": "અહીં ગામની માહિતી, જાહેર નોટિસ, સમાચાર અને વિકાસકાર્યો બતાવી શકાય છે.",
    "citizen": "આ ડિઝાઇન પ્રોટોટાઇપ છે. સુરક્ષિત નાગરિક login અને ફરિયાદ નોંધણી હજી બનાવવાની બાકી છે.",
    "admin": "આ ડિઝાઇન પ્રોટોટાઇપ છે. Admin login, roles અને permission સુરક્ષા હજી બનાવવાની બાકી છે.",
    "officer": "આ ડિઝાઇન પ્રોટોટાઇપ છે. અધિકારીઓ માટે સુરક્ષિત login અને જવાબદારી આધારિત સુવિધાઓ હજી બનાવવાની બાકી છે.",
    "village": "અહીં ગામનો પરિચય, જાહેર સુવિધાઓ, ઇતિહાસ અને ઉપયોગી માહિતી ઉમેરવામાં આવશે.",
    "development": "અહીં મંજૂર વિકાસકાર્યો, હાલની પ્રગતિ અને પૂર્ણ થયેલાં કાર્યોની વિગતો દેખાડવામાં આવશે.",
    "news": "અહીં ગ્રામ પંચાયતની જાહેર નોટિસો અને સમાચાર દર્શાવવામાં આવશે.",
    "contact": "અહીં અધિકૃત રીતે મંજૂર સરપંચ, તલાટી-કમ-મંત્રી અને કચેરીના સંપર્ક ઉમેરવામાં આવશે.",
}
if page != "home":
    st.markdown('<div class="page-info">', unsafe_allow_html=True)
    st.subheader(page_titles.get(page, "કુવાસણા ગ્રામ પંચાયત"))
    st.write(page_messages.get(page, "આ વિભાગ તૈયાર થઈ રહ્યો છે."))
    if page in ("admin", "officer", "citizen"):
        st.warning("હાલમાં અહીં login કાર્યરત નથી. જાહેર ઉપયોગ પહેલાં authentication અને database સુરક્ષા ઉમેરવી જરૂરી છે.")
    st.button("← મુખ્ય પેજ પર પાછા જાઓ", key="back_home", on_click=go, args=("home",))
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="footer">
      <div><div class="footer-brand">🏛️ કુવાસણા ગ્રામ પંચાયત</div><div class="footer-small">Kuvasana Gram Panchayat</div></div>
      <div class="footer-motto">સત્યમેવ જયતે &nbsp; | &nbsp; વંદે માતરમ્</div>
      <div class="footer-right">ડિજિટલ ગામ &nbsp; | &nbsp; સમૃદ્ધ ભારત 🇮🇳</div>
    </div>
    <div style="text-align:center;color:#7a8379;font-size:10px;padding:7px 4px">પ્રોટોટાઇપ ડિઝાઇન — આ સત્તાવાર સરકારી વેબસાઇટ નથી.</div>
    """,
    unsafe_allow_html=True,
)

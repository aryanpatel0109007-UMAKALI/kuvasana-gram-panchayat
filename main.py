import streamlit as st

st.set_page_config(
    page_title="કુવાસણા ગ્રામ પંચાયત | Kuvasana Gram Panchayat",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Official emblem artwork hosted by Wikimedia Commons.
EMBLEM_URL = "https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg"

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Gujarati:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --green: #0d5138;
        --green2: #16843b;
        --saffron: #f58220;
        --navy: #173f7a;
        --cream: #fff9ee;
        --page: #f7f8f2;
        --ink: #173a2c;
    }

    html, body, [class*="css"], .stApp {
        font-family: 'Noto Sans Gujarati', 'Inter', sans-serif;
    }
    .stApp { background: var(--page); color: var(--ink); }
    header[data-testid="stHeader"] { background: transparent; }
    #MainMenu, footer { visibility: hidden; }
    .block-container {
        max-width: 1540px;
        padding: .45rem 1.1rem 1rem;
    }

    /* Clean tricolour header */
    .tricolour-line {
        height: 7px;
        border-radius: 4px;
        background: linear-gradient(90deg,
            #ff9933 0 33.333%, #ffffff 33.333% 66.666%, #138808 66.666% 100%);
        border: 1px solid rgba(20, 50, 35, .08);
    }
    .header-brand { padding: 8px 0 4px; }
    .header-guj { font-size: clamp(20px, 2.05vw, 31px); line-height: 1.25; font-weight: 800; color: var(--green); }
    .header-eng { font-size: 16px; font-weight: 750; margin-top: 2px; }
    .header-tag { font-size: 12px; color: #56685d; margin-top: 2px; }
    .emblem-small { width: auto; height: 75px; max-width: 100%; object-fit: contain; }
    .language-mark { text-align: center; color: var(--green); font-size: 14px; padding-top: 7px; }

    .st-key-nav_home button, .st-key-nav_village button,
    .st-key-nav_development button, .st-key-nav_news button,
    .st-key-nav_contact button {
        background: transparent !important; color: #234738 !important;
        border: 0 !important; border-radius: 0 !important;
        padding: 5px 3px !important; min-height: 40px !important;
        white-space: nowrap !important; font-weight: 650 !important;
        font-size: 13px !important; box-shadow: none !important;
    }
    .st-key-nav_home button:hover, .st-key-nav_village button:hover,
    .st-key-nav_development button:hover, .st-key-nav_news button:hover,
    .st-key-nav_contact button:hover {
        color: #d96713 !important; border-bottom: 3px solid #ff9933 !important;
    }

    /* Hero banner: independent grid zones avoid overlapping text and emblem */
    .hero-banner {
        position: relative;
        overflow: hidden;
        isolation: isolate;
        border-radius: 16px;
        margin: 13px 0 17px;
        border: 1px solid #eadfca;
        border-bottom: 5px solid #138808;
        background:
            radial-gradient(ellipse at 6% 95%, rgba(132, 171, 97, .24), transparent 33%),
            radial-gradient(ellipse at 57% 100%, rgba(255, 192, 84, .28), transparent 35%),
            linear-gradient(120deg, #fff9eb 0%, #fffdf8 52%, #fff3d6 100%);
    }
    .hero-banner:before {
        content: "";
        position: absolute;
        z-index: -1;
        right: 0;
        top: 0;
        width: 28%;
        height: 100%;
        background: linear-gradient(180deg,
            rgba(255,153,51,.93) 0 31%,
            rgba(255,255,255,.94) 31% 63%,
            rgba(19,136,8,.91) 63% 100%);
        clip-path: polygon(18% 0,100% 0,100% 100%,0 100%,20% 73%,7% 48%,0 25%);
    }
    .hero-grid {
        display: grid;
        grid-template-columns: 17% 55% 28%;
        align-items: center;
        gap: 8px;
        min-height: 345px;
        padding: 25px 22px 22px;
    }
    .azadi-badge { text-align: center; padding: 4px 5px; color: #865c27; }
    .azadi-number { font-family: Georgia, serif; font-size: clamp(48px, 5vw, 76px); line-height: .98; color: #967144; }
    .azadi-ribbon { color: #dc8a20; letter-spacing: 3px; font-size: 25px; line-height: 1; }
    .azadi-copy { font-size: clamp(15px, 1.4vw, 21px); font-weight: 800; line-height: 1.4; margin-top: 8px; }
    .hero-main { text-align: center; padding: 4px 8px; min-width: 0; }
    .hero-eyebrow { font-size: 14px; font-weight: 800; color: #268044; margin-bottom: 7px; }
    .hero-title { color: #0d5138; font-size: clamp(28px, 3.1vw, 47px); line-height: 1.23; font-weight: 800; margin: 5px 0 9px; overflow-wrap: anywhere; }
    .hero-title span { color: #e87517; }
    .hero-subtitle { color: #214f3a; font-size: clamp(17px, 1.9vw, 26px); line-height: 1.45; font-weight: 750; margin: 0 0 12px; }
    .hero-green-line { color: #247b36; font-size: clamp(12px, 1.15vw, 16px); line-height: 1.8; font-weight: 800; }
    .hero-motto { color: #0d5138; font-size: clamp(20px, 1.9vw, 28px); font-weight: 800; margin-top: 12px; }
    .hero-vande { font-size: clamp(17px, 1.5vw, 22px); font-weight: 800; margin-top: 3px; }
    .hero-vande .orange { color: #e87517; }
    .hero-vande .green { color: #13823b; }
    .hero-right { min-width: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px; padding: 5px; }
    .hero-emblem { width: auto; height: 205px; max-width: 76%; object-fit: contain; filter: sepia(.55) saturate(1.35) hue-rotate(350deg) contrast(1.03); }
    .chakra { width: 61px; height: 61px; border: 4px solid #173f7a; border-radius: 50%; color: #173f7a; background: rgba(255,255,255,.9); display: flex; align-items: center; justify-content: center; font-size: 37px; line-height: 1; }
    .hero-emblem-caption { color: #77531d; font-size: 13px; font-weight: 800; text-align: center; }

    /* Portal cards */
    .section-heading { display:flex; align-items:center; justify-content:center; gap:13px; text-align:center; color:#124831; font-weight:800; font-size:clamp(21px,2vw,28px); margin:8px 0 15px; }
    .heading-rule { display:inline-block; width:60px; height:5px; border-top:2px solid #f58220; border-bottom:2px solid #138808; flex-shrink:0; }
    .portal-card { min-height:184px; border:1px solid rgba(0,0,0,.04); border-radius:15px; padding:14px 10px 11px; text-align:center; display:flex; flex-direction:column; align-items:center; justify-content:flex-start; }
    .portal-card.public { background:linear-gradient(135deg,#f2fbef,#d9f2d6); }
    .portal-card.citizen { background:linear-gradient(135deg,#fff7eb,#ffead4); }
    .portal-card.admin { background:linear-gradient(135deg,#eef7ff,#deefff); }
    .portal-card.officer { background:linear-gradient(135deg,#f8f1ff,#eadef9); }
    .portal-icon { width:52px; height:52px; border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-size:26px; margin:0 auto 7px; box-shadow:0 4px 12px rgba(0,0,0,.08); }
    .public .portal-icon { background:#07852f; } .citizen .portal-icon { background:#ff730b; } .admin .portal-icon { background:#0755ab; } .officer .portal-icon { background:#6425a1; }
    .portal-card h3 { font-size:clamp(16px,1.35vw,21px); font-weight:800; margin:0 0 5px; }
    .public h3 { color:#08752c; } .citizen h3 { color:#dc6507; } .admin h3 { color:#074d9d; } .officer h3 { color:#5b2494; }
    .portal-card p { font-size:12px; line-height:1.5; margin:0; max-width:260px; }
    .st-key-portal_public button, .st-key-portal_citizen button, .st-key-portal_admin button, .st-key-portal_officer button { width:100% !important; min-height:39px !important; border:0 !important; border-radius:9px !important; color:white !important; font-weight:750 !important; }
    .st-key-portal_public button { background:#07852f !important; } .st-key-portal_citizen button { background:#f06c0a !important; } .st-key-portal_admin button { background:#0755ab !important; } .st-key-portal_officer button { background:#6425a1 !important; }

    /* Eight feature icons */
    .feature-strip { background:rgba(255,255,255,.92); border:1px solid #e5e7df; border-radius:15px; padding:13px 8px 9px; box-shadow:0 3px 14px rgba(22,50,34,.035); }
    .feature-grid { display:grid; grid-template-columns:repeat(8,minmax(0,1fr)); }
    .feature-item { text-align:center; min-height:81px; padding:7px 4px 0; border-right:1px solid #d9dfd5; }
    .feature-item:last-child { border-right:0; }
    .feature-icon { height:46px; width:46px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:22px; margin:0 auto 7px; }
    .feature-label { color:#18392a; font-size:11px; font-weight:750; line-height:1.4; }
    .f-pink{background:#ffccd0;color:#d33d53}.f-orange{background:#ffebc5;color:#d27a12}.f-green{background:#d6f0d2;color:#22813b}.f-blue{background:#d5ebff;color:#1970bd}.f-lime{background:#d8efc9;color:#34843c}.f-purple{background:#ead8ff;color:#7a42af}.f-cyan{background:#cfeef2;color:#218da0}.f-red{background:#ffd5dd;color:#d62852}
    .footer-bar { background:#073f2e; color:#fff; border-radius:12px; padding:16px 20px; margin-top:14px; display:flex; align-items:center; justify-content:space-between; gap:12px; }
    .footer-name { font-size:15px; font-weight:800; } .footer-sub { font-size:11px; opacity:.85; } .footer-motto { font-weight:700; font-size:15px; text-align:center; } .footer-right { font-size:12px; text-align:right; }
    .page-info { background:#fff; border:1px solid #dfe8dc; border-radius:15px; padding:22px; margin:14px 0; }

    @media (max-width: 1050px) {
        .hero-grid { grid-template-columns: 15% 57% 28%; padding:20px 12px; gap:3px; }
        .hero-emblem { height:175px; max-width:88%; }
        .hero-banner:before { width:29%; }
        .portal-card { min-height:195px; }
    }
    @media (max-width: 740px) {
        .block-container { padding-left:.55rem; padding-right:.55rem; }
        .hero-grid { grid-template-columns:1fr; padding:21px 12px; gap:10px; }
        .hero-banner:before { width:100%; height:100%; opacity:.13; clip-path:none; }
        .azadi-badge { display:none; }
        .hero-title { font-size:30px; }
        .hero-subtitle { font-size:18px; }
        .hero-right { flex-direction:row; flex-wrap:wrap; }
        .hero-emblem { height:120px; max-width:35%; }
        .chakra { width:54px; height:54px; font-size:32px; }
        .feature-grid { grid-template-columns:repeat(4,minmax(0,1fr)); }
        .feature-item:nth-child(4n) { border-right:0; }
        .footer-bar { flex-direction:column; text-align:center; }
        .footer-right { text-align:center; }
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
st.markdown('<div class="tricolour-line"></div>', unsafe_allow_html=True)
logo_col, brand_col, nav_col, lang_col = st.columns([0.62, 2.45, 4.2, 0.55])
with logo_col:
    st.markdown(
        f'<div style="text-align:center;padding-top:10px"><img class="emblem-small" src="{EMBLEM_URL}" alt="ભારતનું રાષ્ટ્રીય ચિહ્ન"></div>',
        unsafe_allow_html=True,
    )
with brand_col:
    st.markdown(
        """
        <div class="header-brand">
          <div class="header-guj">કુવાસણા ગ્રામ પંચાયત</div>
          <div class="header-eng">Kuvasana Gram Panchayat</div>
          <div class="header-tag">Digital Village | Smart Governance | Better Tomorrow</div>
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

# Hero: each visual element has its own grid area, not layered on top of text.
st.markdown(
    f"""
    <section class="hero-banner">
      <div class="hero-grid">
        <div class="azadi-badge">
          <div class="azadi-number">75</div>
          <div class="azadi-ribbon">〰〰</div>
          <div class="azadi-copy">આઝાદી કા<br>અમૃત મહોત્સવ</div>
        </div>
        <div class="hero-main">
          <div class="hero-eyebrow">🇮🇳 ભારત • ગુજરાત • કુવાસણા 🇮🇳</div>
          <div class="hero-title">કુવાસણા <span>ગ્રામ પંચાયત</span></div>
          <div class="hero-subtitle">ડિજિટલ ગ્રામ વિકાસ અને નાગરિક સેવા પોર્ટલ</div>
          <div class="hero-green-line">🌿 સ્વચ્છ કુવાસણા &nbsp; • &nbsp; 🌱 હરિયાળું કુવાસણા &nbsp; • &nbsp; 🏡 ડિજિટલ કુવાસણા</div>
          <div class="hero-motto">“સત્યમેવ જયતે”</div>
          <div class="hero-vande"><span class="orange">Vande</span> <span class="green">Mataram</span> 🇮🇳</div>
        </div>
        <div class="hero-right">
          <img class="hero-emblem" src="{EMBLEM_URL}" alt="ભારતનું રાષ્ટ્રીય ચિહ્ન">
          <div class="chakra">☸</div>
          <div class="hero-emblem-caption">સત્યમેવ જયતે</div>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# Four main portals
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
            f'<div class="portal-card {slug}"><div class="portal-icon">{icon}</div><h3>{title}</h3><p>{description}</p></div>',
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
items_html = "".join(
    f'<div class="feature-item"><div class="feature-icon {color}">{icon}</div><div class="feature-label">{label}</div></div>'
    for icon, label, color in features
)
st.markdown(
    f'<div class="feature-strip"><div class="feature-grid">{items_html}</div></div>',
    unsafe_allow_html=True,
)

# Prototype navigation targets
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

# Footer
st.markdown(
    """
    <div class="footer-bar">
      <div><div class="footer-name">🏛️ કુવાસણા ગ્રામ પંચાયત</div><div class="footer-sub">Kuvasana Gram Panchayat</div></div>
      <div class="footer-motto">સત્યમેવ જયતે &nbsp; | &nbsp; વંદે માતરમ્</div>
      <div class="footer-right">ડિજિટલ ગામ &nbsp; | &nbsp; સમૃદ્ધ ભારત 🇮🇳</div>
    </div>
    <div style="text-align:center;color:#788278;font-size:10px;padding:7px 4px">પ્રોટોટાઇપ ડિઝાઇન — આ સત્તાવાર સરકારી વેબસાઇટ નથી.</div>
    """,
    unsafe_allow_html=True,
)

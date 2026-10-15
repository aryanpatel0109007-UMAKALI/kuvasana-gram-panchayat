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
    unsafe_allow_html=True,        <div class="hero-emblem-box">
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

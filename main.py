.hero p{color:#4d6858;font-size:16px;line-height:1.75;max-width:690px}
.hero-slogan{color:var(--deep);font-size:23px;font-weight:800;margin-top:12px}
.hero-art{position:absolute;right:7%;top:50%;transform:translateY(-50%);width:205px;height:205px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-direction:column;background:#ffffffd1;border:1px solid #1388082e;box-shadow:0 12px 30px #193c2314}
.hero-art .wheel{font-size:72px;line-height:1;color:#17477b}
.hero-art strong{color:var(--deep);font-size:14px;margin-top:8px}
.tricolor-line{height:6px;width:180px;border-radius:9px;background:linear-gradient(90deg,var(--saffron) 0 33.33%,#fff 33.33% 66.66%,var(--green) 66.66%);margin-top:17px}
.section-title{display:flex;align-items:center;gap:12px;margin:30px 0 16px}
.section-title h2{color:var(--deep);font-size:25px;font-weight:800;margin:0}
.section-title:after{content:"";height:4px;flex:1;max-width:100px;border-radius:8px;background:linear-gradient(90deg,var(--saffron) 0 33%,#fff 33% 66%,var(--green) 66%)}
.portal-card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px 18px 15px;min-height:170px;box-shadow:0 7px 22px #1a422b0b}
.portal-icon{width:48px;height:48px;border-radius:14px;display:grid;place-items:center;background:linear-gradient(145deg,#fff1df,#edf7ec);font-size:24px;margin-bottom:11px}
.portal-card h3{color:var(--deep);font-size:19px;margin:0 0 5px;font-weight:800}
.portal-card p{color:var(--muted);font-size:14px;line-height:1.55;min-height:42px;margin:0}
div.stButton>button{width:100%;min-height:44px;border-radius:11px;border:1px solid var(--green);background:var(--green);color:#fff;font-weight:700;transition:all .18s ease}
div.stButton>button:hover{background:var(--saffron);border-color:var(--saffron);color:#25382d;box-shadow:0 5px 14px #f28c2833}
div[data-testid="stVerticalBlockBorderWrapper"]{border-radius:16px;border-color:var(--line)}
div[data-testid="stAlert"]{border-radius:12px}
.footer{background:linear-gradient(110deg,#124734,#176c37);color:#fff;text-align:center;padding:24px 18px;border-radius:18px;margin-top:32px;border-top:5px solid var(--saffron)}
.footer small{color:#e4f0e6}
@media(max-width:850px){.block-container{padding:1rem 1rem 2rem}.brand{align-items:flex-start}.brand-tag{display:none}.hero{padding:30px 22px;min-height:320px}.hero-art{right:-45px;opacity:.18;width:190px;height:190px}.hero-content{max-width:100%}}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="brand">
  <div class="brand-left">
    <div class="brand-mark">🇮🇳</div>
    <div>
      <h1>કુવાસણા ગ્રામ પંચાયત</h1>
      <p><b>Kuvasana Gram Panchayat</b> · Digital Village | Smart Governance | Better Tomorrow</p>
    </div>
  </div>
  <div class="brand-tag">સ્વચ્છ ગામ · સમૃદ્ધ ગામ</div>
</div>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<section class="hero">
  <div class="hero-content">
    <div class="eyebrow">🇮🇳 ભારત • ગુજરાત • કુવાસણા</div>
    <h1>કુવાસણા <span>ગ્રામ પંચાયત</span></h1>
    <h2>ડિજિટલ ગ્રામ વિકાસ અને નાગરિક સેવા પોર્ટલ</h2>
    <p>સ્વચ્છ કુવાસણા • હરિયાળું કુવાસણા • ડિજિટલ કુવાસણા<br>
    ગામની માહિતી, નાગરિક સેવાઓ અને વિકાસકાર્યો — એક જ જગ્યાએ.</p>
    <div class="hero-slogan">“સત્યમેવ જયતે”</div>
    <div style="color:#e87513;font-size:18px;font-weight:800;">વંદે માતરમ્ 🇮🇳</div>
    <div class="tricolor-line"></div>
  </div>
  <div class="hero-art">
    <div class="wheel">☸</div>
    <strong>સત્યમેવ જયતે</strong>
  </div>
</section>
""", unsafe_allow_html=True)

st.markdown("## 🇮🇳 અમારા ડિજિટલ પોર્ટલ")

# FOUR PORTALS
c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container(border=True):
        st.markdown("### 🌐 જાહેર પોર્ટલ")
        st.write("ગામની માહિતી, સમાચાર અને વિકાસકાર્યો.")
        if st.button("જાહેર માહિતી જુઓ", key="public"):
            st.session_state["portal"] = "public"

with c2:
    with st.container(border=True):
        st.markdown("### 👨‍👩‍👧 ગ્રામજન પોર્ટલ")
        st.write("ફરિયાદો, પાણીની માહિતી અને સૂચનો.")
        if st.button("ગ્રામજન પોર્ટલ", key="villager"):
            st.session_state["portal"] = "villager"

with c3:
    with st.container(border=True):
        st.markdown("### 🛡️ Admin પોર્ટલ")
        st.write("નોટિસ, ફરિયાદો અને વિકાસકાર્યો.")
        if st.button("Admin પોર્ટલ", key="admin"):
            st.session_state["portal"] = "admin"

with c4:
    with st.container(border=True):
        st.markdown("### 🧑‍💼 Officer પોર્ટલ")
        st.write("અધિકૃત કર્મચારીઓ માટેની સુવિધાઓ.")
        if st.button("Officer પોર્ટલ", key="officer"):
            st.session_state["portal"] = "officer"

# PORTAL RESPONSES
portal = st.session_state.get("portal", "")

if portal == "public":
    st.subheader("🌐 કુવાસણા ગામની જાહેર માહિતી")
    st.info("અહીં ગામની માહિતી, નોટિસ અને વિકાસકાર્યો બતાવવામાં આવશે.")

elif portal == "villager":
    st.subheader("👨‍👩‍👧 ગ્રામજન પોર્ટલ")
    st.info("આગળના તબક્કામાં સુરક્ષિત login અને ફરિયાદ નોંધણી ઉમેરીશું.")

elif portal == "admin":
    st.subheader("🛡️ Admin પોર્ટલ")
    st.warning("આ demo વિભાગ છે. સુરક્ષિત authentication હજુ ઉમેરવાનું છે.")

elif portal == "officer":
    st.subheader("🧑‍💼 Officer પોર્ટલ")
    st.info("અધિકૃત login અને role permissions આગળના તબક્કામાં ઉમેરાશે.")

st.divider()

st.markdown("## 🌳 અમારી મુખ્ય સુવિધાઓ")

features = st.columns(4)

items = [
    ("📝", "ફરિયાદ વ્યવસ્થાપન"),
    ("🏗️", "વિકાસકાર્યો"),
    ("💰", "બજેટ અને ખર્ચ"),
    ("🗳️", "ડિજિટલ Polls"),
    ("🌱", "Green Kuvasana"),
    ("🤖", "AI Chatbot"),
    ("📊", "Analytics Dashboard"),
    ("📱", "મોબાઇલ સુવિધા"),
]

for i, (icon, name) in enumerate(items):
    with features[i % 4]:
        st.markdown(f"### {icon}")
        st.write(name)

st.markdown("""
<div class="footer">
    <b>કુવાસણા ગ્રામ પંચાયત</b><br>
    સત્યમેવ જયતે | વંદે માતરમ્<br>
    <small>Digital Village • Better Tomorrow</small>
</div>
""", unsafe_allow_html=True)

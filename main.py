
import streamlit as st

st.set_page_config(
    page_title="કુવાસણા ગ્રામ પંચાયત",
    page_icon="🇮🇳",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #fffdf6;
    color: #123b2c;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 1.5rem;
    max-width: 1400px;
}

.brand {
    border-bottom: 4px solid #138808;
    padding: 12px 0 20px;
    text-align: center;
}

.brand h1 {
    color: #123b2c;
    font-size: 34px;
    margin-bottom: 4px;
}

.brand p {
    margin: 5px;
    font-size: 17px;
}

.hero {
    background: linear-gradient(
        115deg,
        #fff7e9 0%,
        #ffffff 48%,
        #eaf7e9 100%
    );
    border-top: 8px solid #ff9933;
    border-bottom: 8px solid #138808;
    border-radius: 18px;
    padding: 32px 15px;
    text-align: center;
    margin: 22px 0;
}

.hero h1 {
    font-size: 38px;
    color: #154734;
}

.hero h2 {
    color: #e87513;
    font-size: 25px;
}

.hero p {
    font-size: 19px;
}

.slogan {
    color: #14532d;
    font-weight: bold;
    font-size: 23px;
}

div.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 10px;
    border: 1px solid #138808;
    background: #138808;
    color: white;
    font-weight: bold;
}

div.stButton > button:hover {
    background: #ff9933;
    color: #123b2c;
    border-color: #ff9933;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 14px;
}

.footer {
    background: #123b2c;
    color: white;
    text-align: center;
    padding: 20px;
    border-radius: 12px;
    margin-top: 25px;
}
</style>
""", unsafe_allow_html=True)

# HEADER
left, right = st.columns([3, 1])

with left:
    st.markdown("""
    <div style="padding:10px 0">
        <h2 style="color:#123b2c;margin:0">
            🇮🇳 કુવાસણા ગ્રામ પંચાયત
        </h2>
        <p style="margin:4px 0">
            Kuvasana Gram Panchayat
        </p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div style="text-align:center;padding:10px">
        <h2>🦁</h2>
        <b>સત્યમેવ જયતે</b>
    </div>
    """, unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<div class="hero">
    <p>🇮🇳 ભારત • ગુજરાત • કુવાસણા 🇮🇳</p>
    <h1>કુવાસણા ગ્રામ પંચાયત</h1>
    <h2>ડિજિટલ ગ્રામ વિકાસ અને નાગરિક સેવા પોર્ટલ</h2>
    <p>સ્વચ્છ કુવાસણા • હરિયાળું કુવાસણા • ડિજિટલ કુવાસણા</p>
    <div class="slogan">“સત્યમેવ જયતે”</div>
    <h2 style="color:#138808">વંદે માતરમ્ 🇮🇳</h2>
</div>
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

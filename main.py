
import streamlit as st

st.set_page_config(
    page_title="કુવાસણા ગ્રામ પંચાયત",
    page_icon="🇮🇳",
    layout="wide"
)

# ---------------- DESIGN ----------------
st.markdown("""
<style>
.stApp {
    background: #f8faf7;
    color: #20382c;
}

.block-container {
    max-width: 1450px;
    padding-top: 1rem;
    padding-bottom: 2rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.tricolor {
    height: 9px;
    border-radius: 5px;
    background: linear-gradient(
        to right,
        #ff9933 0%, #ff9933 33.3%,
        #ffffff 33.3%, #ffffff 66.6%,
        #138808 66.6%, #138808 100%
    );
    border: 1px solid #e6e6e6;
}

.brand {
    background: white;
    border: 1px solid #e0e8df;
    border-radius: 16px;
    padding: 20px;
    margin: 14px 0;
    text-align: center;
    box-shadow: 0 4px 15px rgba(20,60,35,.05);
}

.brand h1 {
    color: #174b32;
    font-size: 34px;
    margin: 4px 0;
}

.brand p {
    margin: 5px;
    color: #53645a;
}

.hero {
    background: linear-gradient(
        115deg, #fff0dc 0%,
        #ffffff 47%, #eaf7e9 100%
    );
    border: 1px solid #eadfcd;
    border-top: 7px solid #ff9933;
    border-bottom: 7px solid #138808;
    border-radius: 20px;
    padding: 34px 25px;
    text-align: center;
    margin: 20px 0;
}

.hero h1 {
    color: #174b32;
    font-size: 42px;
}

.hero h3 {
    color: #c56817;
}

.hero p {
    font-size: 17px;
    color: #46584c;
}

.ashoka {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 96px;
    height: 96px;
    border: 5px solid #1b4a91;
    border-radius: 50%;
    color: #1b4a91;
    font-size: 45px;
    margin: 12px;
}

.section-title {
    color: #174b32;
    font-size: 28px;
    font-weight: 750;
    margin: 24px 0 8px;
}

div.stButton > button {
    width: 100%;
    min-height: 46px;
    border-radius: 9px;
    background: #167b3a;
    border: 1px solid #167b3a;
    color: white;
    font-weight: 600;
}

div.stButton > button:hover {
    background: #ff9933;
    border-color: #ff9933;
    color: #183a29;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border-radius: 14px;
    border-color: #dce7dc;
}

.footer {
    background: #173e2c;
    color: white;
    text-align: center;
    padding: 24px 12px;
    border-radius: 14px;
    margin-top: 28px;
}

.small-note {
    text-align: center;
    color: #657369;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

def go(page):
    st.session_state.page = page

# ---------------- HEADER ----------------
st.markdown('<div class="tricolor"></div>',
            unsafe_allow_html=True)

emblem_url = (
    "https://upload.wikimedia.org/wikipedia/commons/"
    "thumb/5/55/Emblem_of_India.svg/"
    "120px-Emblem_of_India.svg.png"
)

left, middle, right = st.columns([1, 4, 1])

with left:
    st.markdown(
        f'<div style="text-align:center;padding:8px">'
        f'<img src="{emblem_url}" '
        f'alt="ભારતનું રાષ્ટ્રીય ચિહ્ન" '
        f'style="height:105px;max-width:100%;object-fit:contain">'
        f'</div>',
        unsafe_allow_html=True
    )

with middle:
    st.markdown("""
    <div class="brand">
        <h1>કુવાસણા ગ્રામ પંચાયત</h1>
        <h3 style="color:#d57920;margin:5px">
            ભારત • ગુજરાત • કુવાસણા
        </h3>
        <p>ડિજિટલ ગ્રામ વિકાસ અને નાગરિક સેવા પોર્ટલ</p>
        <p style="color:#17813d;font-weight:bold">
            સત્યમેવ જયતે • વંદે માતરમ્
        </p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div style="text-align:center;padding:14px 2px">
        <div class="ashoka">☸</div>
        <p style="font-weight:bold;color:#174b32">
            એક ભારત<br>શ્રેષ્ઠ ભારત
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- NAV MENU ----------------
nav_items = [
    ("હોમ", "home"),
    ("ગામની માહિતી", "village"),
    ("નાગરિક સેવાઓ", "services"),
    ("વિકાસકાર્યો", "development"),
    ("Green Kuvasana", "green"),
]

nav_cols = st.columns(len(nav_items))

for col, (label, target) in zip(nav_cols, nav_items):
    with col:
        st.button(
            label,
            key="nav_" + target,
            on_click=go,
            args=(target,)
        )

# ---------------- HOME PAGE ----------------
page = st.session_state.page

if page == "home":

    st.markdown("""
    <div class="hero">
        <p>🇮🇳 જનસેવા • પારદર્શિતા • ગ્રામ વિકાસ 🇮🇳</p>
        <h1>આપણું ગામ, આપણી જવાબદારી</h1>
        <h3>કુવાસણા ગ્રામ પંચાયત ડિજિટલ પોર્ટલ</h3>
        <div class="ashoka">☸</div>
        <p>
            ગામની માહિતી, નાગરિક સેવાઓ અને વિકાસકાર્યો
            એક જ સ્થળે મેળવવા માટેનું ડિજિટલ પ્લેટફોર્મ.
        </p>
        <h3 style="color:#18813b">વંદે માતરમ્ 🇮🇳</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">'
        '🇮🇳 અમારા ચાર મુખ્ય પોર્ટલ</div>',
        unsafe_allow_html=True
    )

    portal_data = [
        ("🌐", "જાહેર પોર્ટલ",
         "ગામની માહિતી, જાહેર નોટિસ અને સમાચાર.",
         "public"),
        ("👨‍👩‍👧", "ગ્રામજન પોર્ટલ",
         "ફરિયાદો, પાણીની માહિતી અને સૂચનો.",
         "citizen"),
        ("🛡️", "Admin પોર્ટલ",
         "ફરિયાદો, નોટિસ અને વિકાસકાર્યોનું સંચાલન.",
         "admin"),
        ("🧑‍💼", "Officer પોર્ટલ",
         "અધિકૃત કર્મચારીઓ માટેનું કાર્યક્ષેત્ર.",
         "officer"),
    ]

    cols = st.columns(4)

    for col, (icon, title, description, target) in zip(
        cols, portal_data
    ):
        with col:
            with st.container(border=True):
                st.markdown(
                    f"<h2 style='text-align:center'>{icon}</h2>"
                    f"<h3 style='text-align:center;color:#174b32'>"
                    f"{title}</h3>"
                    f"<p style='text-align:center;min-height:55px'>"
                    f"{description}</p>",
                    unsafe_allow_html=True
                )
                st.button(
                    "પોર્ટલ ખોલો",
                    key="portal_" + target,
                    on_click=go,
                    args=(target,)
                )

    st.markdown(
        '<div class="section-title">'
        '🌳 ગામના વિકાસ માટેની મુખ્ય સુવિધાઓ</div>',
        unsafe_allow_html=True
    )

    features = [
        ("📝", "ફરિયાદ વ્યવસ્થાપન"),
        ("💧", "પાણી પુરવઠાની માહિતી"),
        ("💡", "સ્ટ્રીટલાઇટ ફરિયાદ"),
        ("🏗️", "વિકાસકાર્યોની પ્રગતિ"),
        ("💰", "બજેટ અને ખર્ચ"),
        ("🗳️", "જાહેર અભિપ્રાય અને Polls"),
        ("🌱", "Green Kuvasana"),
        ("🤖", "AI Chatbot"),
        ("📊", "Analytics Dashboard"),
        ("📸", "ફોટો ગેલેરી"),
        ("📢", "જાહેર નોટિસ"),
        ("📞", "મહત્ત્વના સંપર્કો"),
    ]

    feature_cols = st.columns(4)

    for i, (icon, name) in enumerate(features):
        with feature_cols[i % 4]:
            with st.container(border=True):
                st.markdown(
                    f"<h2 style='text-align:center'>{icon}</h2>"
                    f"<p style='text-align:center;font-weight:600'>"
                    f"{name}</p>",
                    unsafe_allow_html=True
                )

    st.markdown("""
    <div class="hero">
        <h2 style="color:#174b32">🌱 Green Kuvasana</h2>
        <p>
            વૃક્ષારોપણ • સ્વચ્છતા • જળ સંરક્ષણ • હરિયાળું ગામ
        </p>
        <h3 style="color:#17813d">સ્વચ્છ ગામ, સુંદર ગામ</h3>
    </div>
    """, unsafe_allow_html=True)

# ---------------- OTHER PAGES ----------------
elif page == "village":
    st.title("🏡 કુવાસણા ગામની માહિતી")
    st.write(
        "આ વિભાગમાં ગામનો પરિચય, જાહેર સુવિધાઓ, "
        "ઇતિહાસ અને ગામનાં મહત્ત્વનાં સ્થળોની માહિતી આવશે."
    )
    st.info("ગામની પ્રમાણિત માહિતી અહીં પછી ઉમેરીશું.")

elif page == "services":
    st.title("👨‍👩‍👧 નાગરિક સેવાઓ")
    st.write("નાગરિકોને ઉપયોગી સેવાઓ અને માહિતી.")
    st.markdown("""
    - 📝 ફરિયાદ નોંધણી અને Complaint ID
    - 💧 પાણી પુરવઠાની માહિતી
    - 💡 સ્ટ્રીટલાઇટ અને સફાઈ સંબંધિત ફરિયાદો
    - 📢 જાહેર નોટિસ અને જાહેરાતો
    - 📞 અધિકૃત સંપર્કોની માહિતી
    """)
    st.info(
        "ફરિયાદ સાચવવાની અને તેનું status જોવા માટે "
        "આગળ database જોડવાનું રહેશે."
    )

elif page == "development":
    st.title("🏗️ ગામનાં વિકાસકાર્યો")
    st.write(
        "ચાલુ અને પૂર્ણ થયેલાં વિકાસકાર્યોની વિગતો "
        "અહીં બતાવવામાં આવશે."
    )
    st.info(
        "વિકાસકાર્ય, બજેટ અને પ્રગતિની વાસ્તવિક માહિતી "
        "મળ્યા પછી અહીં ઉમેરીશું."
    )

elif page == "green":
    st.title("🌳 Green Kuvasana")
    st.markdown("""
    - 🌱 વૃક્ષારોપણ અને વૃક્ષોની દેખરેખ
    - 🧹 સ્વચ્છતા અભિયાન
    - 🚰 જળ સંરક્ષણ અને પાણીની સમસ્યાઓ
    - 💡 સ્ટ્રીટલાઇટ મરામતની પ્રગતિ
    - 📸 વિકાસકાર્યોનાં પહેલાં અને પછીનાં ફોટા
    - 🙋 સ્વયંસેવક નોંધણી
    """)

elif page == "public":
    st.title("🌐 જાહેર પોર્ટલ")
    st.write("ગામની જાહેર માહિતી અને સૂચનાઓ માટેનું પાનું.")
    st.info("જાહેર માહિતી પછી અહીં દર્શાવવામાં આવશે.")

elif page == "citizen":
    st.title("👨‍👩‍👧 ગ્રામજન પોર્ટલ")
    st.write("ગ્રામજનો માટેની સેવાઓ.")
    st.info(
        "સુરક્ષિત Login, ફરિયાદ નોંધણી અને Complaint Tracking "
        "આગળના તબક્કામાં ઉમેરાશે."
    )

elif page == "admin":
    st.title("🛡️ Admin પોર્ટલ")
    st.warning(
        "આ ડિઝાઇનનો Demo વિભાગ છે. "
        "હાલમાં સુરક્ષિત Admin Login કાર્યરત નથી."
    )

elif page == "officer":
    st.title("🧑‍💼 Officer પોર્ટલ")
    st.info(
        "અધિકારી Login અને અલગ permissions "
        "પછી ઉમેરવામાં આવશે."
    )

st.markdown("""
<div class="footer">
    <h3>🇮🇳 કુવાસણા ગ્રામ પંચાયત</h3>
    <p>સત્યમેવ જયતે • વંદે માતરમ્</p>
    <p>ડિજિટલ ગ્રામ વિકાસ • જનસેવા • પારદર્શિતા</p>
    <hr>
    <p style="font-size:12px">
        આ સ્વતંત્ર પ્રોજેક્ટનો પ્રોટોટાઇપ છે;
        સત્તાવાર સરકારી વેબસાઇટ હોવાનો દાવો નથી.
    </p>
</div>
""", unsafe_allow_html=True)

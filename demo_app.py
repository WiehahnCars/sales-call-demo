import streamlit as st
import pandas as pd
from datetime import datetime
import random
import time

# === Page Config ===
st.set_page_config(
    page_title="Ithemba Call Centre Portal",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# === Fake Login Page ===
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown(
        """
        <style>
        .stApp, body {
            background-color: #111 !important;
            color: #fff !important;
        }
        .block-container {
            background-color: #111 !important;
        }
        .stButton>button {
            background-color: #222 !important;
            color: #fff !important;
            border: 1px solid #444 !important;
        }
        .stImage img {
            background: transparent !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("logo.png", width=160)
    with col2:
        st.title("Welcome to Ithemba Call Centre")
        st.subheader("Log in to continue")
        if st.button("Sign in"):
            st.session_state.logged_in = True
    st.stop()

# === Sidebar Navigation ===
st.sidebar.image("logo.png", width=100)
selection = st.sidebar.radio("📂 Navigation", [
    "Upload & Transcribe",
    "Live Call Analysis",
    "Client Personas",
    "Team",
    "Business Resources"
])

# === Force Dark Theme ===
st.markdown(
    """
    <style>
    body, .stApp {
        background-color: #111 !important;
        color: #fff !important;
    }
    .css-1d391kg, .css-1d391kg .css-1v0mbdj, .css-1d391kg .css-1v0mbdj .css-1cpxqw2 {
        background-color: #111 !important;
    }
    .stSidebar, .css-6qob1r, .css-1d391kg {
        background-color: #111 !important;
        color: #fff !important;
    }
    .stSidebar .css-1v0mbdj, .stSidebar .css-1cpxqw2 {
        background-color: #111 !important;
        color: #fff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# === Upload Tab ===
if selection == "Upload & Transcribe":
    st.title("Upload & Transcribe")
    live_calls = random.randint(1, 5)
    st.metric("📞 Live Calls in Progress", live_calls)

    col1, col2, col3 = st.columns(3)
    col1.metric("Calls Today", 12 + live_calls)
    col2.metric("Calls This Week", 46)
    col3.metric("Calls This Month", 139)

    st.divider()
    uploaded_file = st.file_uploader("Upload a sales call audio file", type=["mp3", "wav"])

    if uploaded_file:
        st.success("Audio file uploaded successfully!")
        if st.button("Transcribe & Analyse"):
            with st.spinner("Processing audio..."):
                time.sleep(2)
            st.subheader("🗣 Transcript")
            st.code("""
Agent: Hi John, thank you for your interest in our rent-to-buy vehicle plan.
Client: I’m trying to understand the payments.
Agent: It's R299/month for 36 months. Includes tracking and maintenance.
Client: Do I pay a deposit?
Agent: Yes, R2,500 before delivery.
            """, language="text")
            st.success("Transcript generated and added to dashboard.")

# === Live Call Analysis Tab ===
elif selection == "Live Call Analysis":
    st.title("Live Call Monitoring")
    st.caption("Real-time overview of ongoing calls")

    df_live = pd.DataFrame([
        {"Agent": "Thando M.", "Client": "Sibongile", "Sentiment": "😊 Positive", "Prediction": "Likely", "Flag": "🟢"},
        {"Agent": "James L.", "Client": "Vusi", "Sentiment": "😐 Neutral", "Prediction": "Maybe", "Flag": "🟡"},
        {"Agent": "Lerato N.", "Client": "Anna", "Sentiment": "😠 Frustrated", "Prediction": "Unlikely", "Flag": "🔴"}
    ])
    st.dataframe(df_live)

    st.subheader("🔍 Flagged Issues")
    st.markdown("- 🔴 Deposit refund criteria not explained")
    st.markdown("- 🟡 Missed needs analysis")
    st.markdown("- 🔴 Skipped product disclaimer")

# === Personas Tab ===
elif selection == "Client Personas":
    st.title("👥 Client Personas")
    st.markdown("Overview of recognised customer types based on call insights.")

    personas = {
        "Budget Conscious Commuter": 15,
        "Family First Planner": 9,
        "Skeptical Opportunity Seeker": 6
    }
    df = pd.DataFrame(list(personas.items()), columns=["Persona", "Client Count"])
    st.bar_chart(df.set_index("Persona"))

# === Team Tab ===
elif selection == "Team":
    st.title("Team Overview")

    df_team = pd.DataFrame([
        {"Name": "Lindiwe M.", "Role": "Sales Agent", "Manager": "S. Dlamini", "Join Date": "2022-03-01"},
        {"Name": "Eddie S.", "Role": "QA Reviewer", "Manager": "T. Ndlovu", "Join Date": "2021-11-15"},
        {"Name": "Neo R.", "Role": "Team Lead", "Manager": "S. Dlamini", "Join Date": "2020-08-07"}
    ])
    st.dataframe(df_team)

    st.subheader("🔍 Development Areas & Enneagrams")
    st.markdown("""
**Lindiwe M.**  
- Strength: Empathy  
- Dev: Upselling  
- Enneagram: Type 2 (Helper)

**Eddie S.**  
- Strength: Detail  
- Dev: Speed  
- Enneagram: Type 1 (Reformer)

**Neo R.**  
- Strength: Coaching  
- Dev: Delegation  
- Enneagram: Type 8 (Challenger)
    """)

    st.subheader("📈 AI-Generated Performance Snapshot")
    st.info("Neo's team conversion rate rose 12% with improved contract explanation adherence.")

# === Resources Tab ===
elif selection == "Business Resources":
    st.title("📚 Business Resources")
    st.markdown("Each call is evaluated against the contract below.")
    st.download_button("📄 Download Client Contract Template", "Client agrees to terms as stated in contract...", file_name="client_contract_template.txt")

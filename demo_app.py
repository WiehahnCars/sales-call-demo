import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random
import time
from streamlit_autorefresh import st_autorefresh
import matplotlib.pyplot as plt
import plotly.express as px




st.set_page_config(
    page_title="Ithemba Call Centre Hub",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown(
        """
        <style>
        html, body, .stApp, .block-container {
            background-color: #000 !important;
            color: #fff !important;
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
        st.title("Welcome to Ithemba's Call Centre Hub")
        st.markdown("##### Talk smarter with your AI assistant for smarter calls, stronger teams, and happier customers.")
        # st.markdown("##### Build a rich, evolving understanding of your customer base to enable tailored, high-impact conversations at scale.")
        # st.markdown("##### Equip your team with real-time, personalised feedback to continuously improve call quality, script adherence, and customer experience.")
        st.divider()
        
        if st.button("Sign in"):
            st.session_state.logged_in = True
    st.stop()

st.sidebar.image("logo.png", width=100)
selection = st.sidebar.radio("📂 Navigation", [
    "📊 Dashboard",
    "📁 Recordings / Transcripts",
    "🧠 QA Insights",
    "😊 Client Overview",
    "🧑‍🤝‍🧑 Team",
    "⚙️ Settings",
    ])

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
        background-color: #000 !important;
        color: #000 !important;
    }
    .stSidebar .css-1v0mbdj, .stSidebar .css-1cpxqw2 {
        background-color: #111 !important;
        color: #fff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


if selection == "📊 Dashboard":
    st.title("Call Centre Dashboard")

    from streamlit_autorefresh import st_autorefresh

    # 🔁 Trigger a rerun every 2 seconds
    st_autorefresh(interval=2000, key="live_call_refresh")

    # Live call metric
    live_count = random.randint(7, 15)
    st.metric("Live Calls in Progress", live_count)


    # --- SUMMARY TILES ---
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.metric("📞 Total Calls Today", "38")

    with col2:
        st.metric("📈 Calls This Week", "212")

    with col3:
        st.metric("📆 Calls This Month", "893")

    with col4:
        st.metric("🧠 Avg QA Score (Today)", "82%")

    with col5:
        st.metric("⚠️ AI-Flagged Issues", "7")

    with col6:
        st.metric("😊 Avg Client Sentiment", "67%")

    st.markdown("---")

    # --- MOCK DATA ---
    agents = ["Thabo", "Mpho", "Sarah", "Lerato", "Jason"]

    if "call_counts" not in st.session_state:
        st.session_state.call_counts = [random.randint(5, 20) for _ in agents]

    call_counts = st.session_state.call_counts


    # Define consistent colours for agents
    agent_colors = {
        "Thabo": "#1f77b4",
        "Mpho": "#d85454",
        "Sarah": "#1f77b4",
        "Lerato": "#d85454",
        "Jason": "#1f77b4"
    }

    

    # --- CHART: Calls per Agent (Plotly) ---
    st.subheader("Calls per Agent (Today)")

    bar_data = pd.DataFrame({
        "Agent": agents,
        "Calls": call_counts
    })
    # Create bar chart with consistent colours
    bar_fig = px.bar(
        bar_data,
        x="Agent",
        y="Calls",
        title="Calls per Agent (Today)",
        color="Agent",
        text="Calls",
        color_discrete_map=agent_colors
    )    
    bar_fig.update_layout(showlegend=False)
    st.plotly_chart(bar_fig, use_container_width=True)

    # --- CHART: Call Volume Over Time (Plotly) ---
    st.subheader("Calls Over Time (Today)")
    if "volumes" not in st.session_state:
        st.session_state.times = [datetime.now() - timedelta(hours=i) for i in reversed(range(8))]
        st.session_state.volumes = [random.randint(10, 30) for _ in range(8)]

    times = st.session_state.times
    volumes = st.session_state.volumes

    line_data = pd.DataFrame({
        "Time": times,
        "Call Volume": volumes
    })
    line_fig = px.line(line_data, x="Time", y="Call Volume", title="Calls Over Time (Today)", markers=True)
    st.plotly_chart(line_fig, use_container_width=True)

    # --- TABLE: Recent Calls ---
    st.subheader("Recent Calls")
    data = {
        "Agent": [random.choice(agents) for _ in range(5)],
        "Duration": [f"{random.randint(1, 10)} min" for _ in range(5)],
        "Sentiment": [random.choice(["Positive", "Neutral", "Negative"]) for _ in range(5)],
        "QA Score": [f"{random.randint(60, 100)}%" for _ in range(5)],
        "Summary and and recommendations": ["🔍 Open"] * 5,
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    

elif selection == "📁 Recordings / Transcripts":
    st.title("Recordings and Transcripts")

    st.markdown("Browse and review past calls. Click to view full transcript or play the recording.")

    # 📞 Recent Call Log (Static Table)
    st.subheader("Recent Call Log")

    call_log = pd.DataFrame([
        {"Date": "2025-06-05", "Agent": "Thabo", "Client": "Sipho", "Duration": "5 min", "Sentiment": "Positive", "Transcript": "🔍 View", "Audio": "▶️ Play"},
        {"Date": "2025-06-05", "Agent": "Sarah", "Client": "Lungi", "Duration": "8 min", "Sentiment": "Negative", "Transcript": "🔍 View", "Audio": "▶️ Play"},
        {"Date": "2025-06-04", "Agent": "Lerato", "Client": "Brian", "Duration": "4 min", "Sentiment": "Neutral", "Transcript": "🔍 View", "Audio": "▶️ Play"},
    ])

    st.dataframe(call_log, use_container_width=True)


    st.markdown("<br><br>", unsafe_allow_html=True)

    # # 👀 View example transcript
    # st.subheader("📄 Call Transcript")

    # st.markdown("""
    # **Agent (Thabo):** Hello Sipho, thanks for showing interest in the SmartRent plan.  
    # **Client:** Yes, I just want to understand the monthly cost.  
    # **Agent:** It’s R3,800 per month and includes security and water.  
    # **Client:** Okay, and the deposit?  
    # **Agent:** You’ll need to pay a R2,400 deposit before move-in.  
    # **Client:** Thanks. I’ll think about it.  
    # """)

    # # 🔉 Audio player (placeholder)
    # st.subheader("🔊 Audio Playback")
    # st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

    # st.markdown("<br><br>", unsafe_allow_html=True)


    # st.subheader("Data sources")

    # st.markdown("""
    # This dashboard brings together insights from multiple sources to enable a holistic view of client interactions and sales efforts.
    # The current sources include:
    # - 📞 Recorded sales calls
    # - 💬 WhatsApp message threads
    # - 🧠 AI-generated client personas
    # - 📑 Contract data used for QA benchmarking

    # These data points are used to surface risks, sentiment shifts, and conversion indicators in real time.
    # """)

    # # Example weekly data summary
    # st.subheader("This Week’s Engagements")
    # import pandas as pd
    # weekly_data = pd.DataFrame({
    #     "Date": ["2025-06-03", "2025-06-04", "2025-06-05", "2025-06-06"],
    #     "Number of Calls": [12, 17, 14, 9],
    #     "Number of WhatsApps": [18, 21, 19, 11]
    # })
    # st.dataframe(weekly_data)

    # st.divider()
    st.subheader("📤 Upload Calls or Info")
    uploaded_file = st.file_uploader("Upload a sales call audio file", type=["mp3", "wav"])

    if uploaded_file:
        st.success("Audio file uploaded successfully!")
        if st.button("Transcribe & Analyse"):
            with st.spinner("Processing audio..."):
                time.sleep(2)
            st.subheader("🗣 Transcript")
            st.code("""
Agent: Hi John, thank you for your interest in our rental apartment.
Client: I’m trying to understand the monthly payments.
Agent: It's R3,800 per month, which includes water and security.
Client: Do I need to pay a deposit?
Agent: Yes, there's a R2,400 deposit required before moving in.
            """, language="text")
            st.success("Transcript generated and added to dashboard.")











elif selection == "🧠 QA Insights":
    st.title("QA Insights")
    st.markdown("This section shows QA trends across customer interactions.")

    # Sentiment Score Summary
    sentiment_score = 82
    st.metric("Average QA Score Today", f"{sentiment_score}%", delta="+1.5% vs last week")

    st.markdown("<br><br>", unsafe_allow_html=True)  # adds more space


    st.subheader("🚨 Recently Flagged Calls")

    st.markdown("""
    These are conversations where the AI detected potential concerns — such as compliance breaches, missed disclosures, or customer frustration.
    """)

    flagged_data = pd.DataFrame({
        "Agent": ["Thabo", "Sarah", "Lerato"],
        "Issue": ["Script skipped", "Negative tone", "No disclosure"],
        "Severity": ["High", "Medium", "High"],
        "Call": ["View transcript", "View transcript", "View transcript"]

    })

    st.dataframe(flagged_data, use_container_width=True)



    st.markdown("<br><br>", unsafe_allow_html=True)
    st.subheader("Issue Types Overview")

    qa_issue_counts = pd.DataFrame({
        "Category": ["Script Adherence", "Tone & Empathy", "Disclosure Compliance", "Call Handling"],
        "Issues Flagged": [12, 9, 7, 5]
    })

    fig = px.bar(qa_issue_counts, x="Category", y="Issues Flagged", color="Category", title="Top QA Issue Categories")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Trending Issues (This Week)")

    trend_data = pd.DataFrame({
        "Date": pd.date_range(end=pd.Timestamp.today(), periods=7).strftime('%Y-%m-%d'),
        "Script Skipped": [2, 3, 4, 3, 2, 1, 3],
        "Negative Tone": [1, 2, 2, 2, 3, 2, 3],
        "No Disclosure": [0, 1, 1, 2, 1, 2, 1]
    })

    fig_trend = px.line(
        trend_data,
        x="Date",
        y=["Script Skipped", "Negative Tone", "No Disclosure"],
        title="QA Issue Trends Over Time"
    )
    st.plotly_chart(fig_trend, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)






elif selection == "😊 Client Overview":
    st.title("Client Overview")
    st.markdown("This section shows sentiment trends across customer interactions.")

    # Sentiment Score Summary
    sentiment_score = 67
    st.metric("Average Sentiment Score", f"{sentiment_score}%", delta="+2% vs last week")

    # Sentiment Breakdown Chart
    sentiment_breakdown = pd.DataFrame({
        "Sentiment": ["Positive", "Neutral", "Negative"],
        "Calls": [57, 29, 14]
    })

    fig = px.bar(sentiment_breakdown, x="Sentiment", y="Calls", color="Sentiment", title="Sentiment Distribution")
    st.plotly_chart(fig, use_container_width=True)

    # Trend Over Time (Optional)
    st.subheader("Sentiment Trend (Past Week)")
    trend_data = pd.DataFrame({
        "Date": pd.date_range(end=pd.Timestamp.today(), periods=7).strftime('%Y-%m-%d'),
        "Average Sentiment Score": [62, 64, 65, 66, 67, 66, 67]
    })

    fig_line = px.line(trend_data, x="Date", y="Average Sentiment Score", markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)  # adds more space

    st.subheader("🧠 Client Attributes & Understanding")

    st.markdown("""
    Below is a breakdown of key attributes the AI has inferred from recent calls, and whether the client showed understanding of each during the conversation.
    """)

    attribute_data = pd.DataFrame([
        {
            "Client": "Sipho",
            "Interested in Financing": "✅",
            "Understands Deposit": "✅",
            "Understands Monthly Cost": "❌",
            "Concerned About Location": "❌",
            "Client Fit": "🟡 Moderate"
        },
        {
            "Client": "Lungi",
            "Interested in Financing": "❌",
            "Understands Deposit": "✅",
            "Understands Monthly Cost": "✅",
            "Concerned About Location": "✅",
            "Client Fit": "🔴 Low"
        },
        {
            "Client": "Brian",
            "Interested in Financing": "✅",
            "Understands Deposit": "❌",
            "Understands Monthly Cost": "✅",
            "Concerned About Location": "❌",
            "Client Fit": "🟢 High"
        },
    ])

    st.dataframe(attribute_data, use_container_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)  # adds more space

    st.subheader("🧬 Identified Client Personas")

    st.markdown("""
    The AI groups customers into personas based on preferences, financial behaviours, and sentiment signals. This helps agents tailor conversations to match needs.
    """)

    persona_data = pd.DataFrame([
        {"Persona": "Budget Conscious Commuter", "Clients": 23, "Avg Sentiment": "69%", "Typical Concern": "Upfront cost"},
        {"Persona": "Family First Planner", "Clients": 15, "Avg Sentiment": "74%", "Typical Concern": "Safety & reliability"},
        {"Persona": "Skeptical Opportunity Seeker", "Clients": 9, "Avg Sentiment": "58%", "Typical Concern": "Too good to be true"}
    ])

    st.dataframe(persona_data, use_container_width=True)

    st.caption("Use personas to adapt sales scripts, address typical objections early, and boost conversion rates.")

    fig_persona = px.pie(persona_data, names="Persona", values="Clients", title="Client Persona Distribution")
    st.plotly_chart(fig_persona, use_container_width=True)


elif selection == "🧑‍🤝‍🧑 Team":
    st.title("Team")

    st.markdown("This section highlights each agent's team placement, personality type, performance trend, and personalised growth suggestions.")

    agent_data = pd.DataFrame([
        {
            "Name": "Thabo",
            "Role": "Sales Agent",
            "Team": "Alpha",
            "Enneagram": "Type 2 - The Helper",
            "Performance Trend": "📈 Up",
            "Last Week Score": 76,
            "This Week Score": 84
        },
        {
            "Name": "Eddie S.",
            "Role": "Sales Sgent",
            "Team": "Bravo",
            "Enneagram": "Type 1 - The Reformer",
            "Performance Trend": "📉 Down",
            "Last Week Score": 89,
            "This Week Score": 81
        },
        {
            "Name": "Neo R.",
            "Role": "Team Lead",
            "Team": "Alpha",
            "Enneagram": "Type 8 - The Challenger",
            "Performance Trend": "📈 Up",
            "Last Week Score": 82,
            "This Week Score": 90
        }
    ])

    st.subheader("📋 Agent Overview")
    st.dataframe(agent_data.drop(columns=["Last Week Score", "This Week Score"]), use_container_width=True)

    st.divider()

    st.subheader("Personalised Feedback & Development Plans")

    st.markdown("""
**🟢 Lindiwe M.** *(Type 2 - The Helper)* 
- **Strength**: High empathy, clients feel cared for  
- **Watchout**: Avoids hard conversations  
- **Trend**: 📈 Improved 8pts this week  
- **Coaching Tip**: Practise delivering tough truths with supportive framing.

**🚨 Eddie S.** *(Type 1 - The Reformer)*
- **Strength**: Precision and rule-following  
- **Watchout**: Can be overly critical under pressure  
- **Trend**: 📉 Dropped 8pts this week  
- **Coaching Tip**: Focus on what went right before highlighting corrections.

**🟢 Neo R.** *(Type 8 - The Challenger)*  
- **Strength**: Assertive leader, takes initiative  
- **Watchout**: May dominate calls or miss emotional nuance  
- **Trend**: 📈 Strong improvement  
- **Coaching Tip**: Incorporate pauses to check for client emotional cues.
    """)

    st.divider()

    st.subheader("📈 Performance Trend Summary")
    trend_chart = pd.DataFrame({
        "Agent": ["Lindiwe", "Eddie", "Neo"],
        "Last Week": [76, 89, 82],
        "This Week": [84, 81, 90]
    })

    trend_chart = trend_chart.melt(id_vars=["Agent"], var_name="Week", value_name="QA Score")
    import plotly.express as px
    fig = px.line(trend_chart, x="Week", y="QA Score", color="Agent", markers=True, title="QA Score Trends")
    st.plotly_chart(fig, use_container_width=True)
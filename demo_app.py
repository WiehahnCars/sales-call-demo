import streamlit as st

# === Pre-baked transcript and analysis for demo ===

transcript = """
Agent: Hi John, thank you for your interest in our rent-to-buy vehicle plan.
Client: Thanks, I'm just trying to understand what’s included and how the payments work.
Agent: Sure, it's R299 per month for 36 months. It includes maintenance and a tracking device.
Client: Do I need to pay anything upfront?
Agent: Yes, a deposit of R2,500 is required before we hand over the car.
Client: Okay, sounds reasonable. What if I want to upgrade the vehicle?
Agent: That’s definitely possible after 18 months, we can assist with that.
"""

analysis = """
**✅ Contract Adherence**
- Monthly fee (R299): Clearly mentioned.
- Term (36 months): Clearly mentioned.
- Maintenance & tracking: Covered.
- Deposit (R2,500): Correctly stated.
- Upgrade terms: Vaguely referenced, should clarify process and conditions.

**👤 Client Persona**
- Budget-conscious but open-minded.
- Wants clarity and transparency.
- Likely values flexibility and practicality in ownership.

**🧠 Agent Feedback**
- Warm and professional tone.
- Clarified most key terms well.
- Missed an opportunity to proactively address objections (e.g., insurance, ownership).

**🛠 Script Recommendations**
1. Proactively explain ownership at end of term.
2. Clearly outline upgrade conditions.
3. Ask more qualifying questions about the client’s needs.
"""

# === Streamlit UI ===

st.set_page_config(page_title="Sales Call Demo", layout="centered")
st.title("📞 Sales Call Analysis Demo")
st.markdown("This is a simulated demo showing how our system analyses a sales call.")

st.header("📤 Uploaded Call Transcript")
st.code(transcript, language="text")

st.header("📊 AI-Powered Call Analysis")
st.markdown(analysis)

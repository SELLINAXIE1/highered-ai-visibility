import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("Demo Dashboard")

category_df = pd.DataFrame({
    "category": ["Real Estate", "TEFL", "Workforce Development", "Continuing Education"],
    "visibility_score": [42, 28, 18, 35]
})

competitor_df = pd.DataFrame({
    "institution": ["NJCU", "Rutgers", "Pace", "Montclair", "Kean", "CCM"],
    "mentions": [12, 20, 15, 13, 11, 9]
})

prompt_df = pd.DataFrame({
    "prompt": [
        "best real estate license program in New Jersey",
        "online TEFL certification USA",
        "affordable continuing education programs NJ",
        "workforce development certificates near me",
        "career change certificate online",
        "adult education programs New Jersey",
        "best online real estate school NJ",
        "TEFL certification for teaching abroad"
    ],
    "ai_response": [
        "Top programs include Rutgers Continuing Education, Montclair State, and NJCU Adult & Continuing Education.",
        "Popular programs include Pace University, NJCU TEFL certificate, and International TEFL Academy.",
        "Affordable options include community colleges and NJCU continuing education programs.",
        "Rutgers workforce programs and Montclair State certificates are often recommended.",
        "Career certificates from Rutgers and NJCU are commonly suggested.",
        "NJCU ACE and Montclair continuing education programs are recommended.",
        "Real estate licensing programs at Rutgers and NJCU are widely known.",
        "TEFL programs from NJCU and Pace University are popular options."
    ],
    "njcu_mentioned": [True, True, True, False, True, True, True, True],
    "top_competitor": [
        "Rutgers",
        "Pace",
        "Community Colleges",
        "Rutgers",
        "Rutgers",
        "Montclair",
        "Rutgers",
        "Pace"
    ],
    "category": [
        "Real Estate",
        "TEFL",
        "Continuing Education",
        "Workforce Development",
        "Workforce Development",
        "Continuing Education",
        "Real Estate",
        "TEFL"
    ]
})

c1, c2, c3, c4 = st.columns(4)
c1.metric("Visibility Score", "31%")
c2.metric("Average Rank", "3.2")
c3.metric("Mention Frequency", "12 / 30")
c4.metric("Top Competitor", "Rutgers")

st.subheader("Visibility by Category")
fig1 = px.bar(category_df, x="category", y="visibility_score")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Competitor Landscape")
fig2 = px.bar(competitor_df, x="institution", y="mentions")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Prompt Explorer")
st.dataframe(
    prompt_df[["prompt","ai_response","njcu_mentioned","top_competitor"]],
    use_container_width=True
)

st.subheader("Recommendations")
st.warning("NJCU underperforms in Workforce Development prompts. Create stronger workforce-focused landing page copy using job-ready, certificate, career advancement, and flexible online terms.")
st.info("Competitors are more associated with flexibility and career outcomes. Revise program headlines and meta descriptions to emphasize online flexibility and practical outcomes.")

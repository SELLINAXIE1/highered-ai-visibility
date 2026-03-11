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
        "Best real estate license program in New Jersey",
        "Affordable TEFL certification online",
        "Workforce development certificates near me",
        "Continuing education programs in NJ"
    ],
    "category": ["Real Estate", "TEFL", "Workforce Development", "Continuing Education"],
    "njcu_mentioned": ["Yes", "No", "No", "Yes"],
    "rank": [3, None, None, 2],
    "top_institution": ["Rutgers", "Pace", "Rutgers", "NJCU"]
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
st.dataframe(prompt_df, use_container_width=True)

st.subheader("Recommendations")
st.warning("NJCU underperforms in Workforce Development prompts. Create stronger workforce-focused landing page copy using job-ready, certificate, career advancement, and flexible online terms.")
st.info("Competitors are more associated with flexibility and career outcomes. Revise program headlines and meta descriptions to emphasize online flexibility and practical outcomes.")

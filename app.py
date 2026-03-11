import streamlit as st

st.set_page_config(page_title="HigherEd AI Program Visibility Analyzer", layout="wide")

st.title("HigherEd AI Program Visibility Analyzer")
st.subheader("Track how continuing education programs appear in AI-generated recommendations.")

st.markdown("""
Institutions invest in websites, CRM, email, and SEO — but often do not know how their programs appear in AI-generated recommendation flows.

This demo shows how NJCU Adult & Continuing Education programs can be benchmarked for AI discoverability, competitor visibility, and content opportunities.
""")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_Dashboard.py", label="View Demo Dashboard", icon="📊")

with col2:
    st.button("Run Sample Analysis", disabled=True)

st.markdown("### What this demo includes")
st.markdown("""
- Visibility score by category
- Competitor comparison
- Prompt-level results
- Recommendation engine
- Case-study style summary
""")

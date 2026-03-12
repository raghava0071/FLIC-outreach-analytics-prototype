import streamlit as st
import pandas as pd

st.set_page_config(page_title="FLIC Outreach Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/outreach_cleaned.csv")
    df["event_date"] = pd.to_datetime(df["event_date"])
    return df

df = load_data()

# ----------------------------
# Sidebar filters
# ----------------------------
st.sidebar.header("Filters")

county_options = sorted(df["county"].dropna().unique())
program_options = sorted(df["program_type"].dropna().unique())

selected_counties = st.sidebar.multiselect(
    "Select County",
    county_options,
    default=county_options
)

selected_programs = st.sidebar.multiselect(
    "Select Program Type",
    program_options,
    default=program_options
)

filtered_df = df[
    (df["county"].isin(selected_counties)) &
    (df["program_type"].isin(selected_programs))
]

# ----------------------------
# Title and introduction
# ----------------------------
st.title("FLIC Outreach & Engagement Data Dashboard")
st.markdown(
    """
    This prototype demonstrates how a nonprofit organization could organize, clean, 
    monitor, and analyze outreach data to support reporting, program evaluation, 
    and strategic decision-making.
    """
)

# ----------------------------
# KPIs
# ----------------------------
total_events = len(filtered_df)
total_participants = int(filtered_df["participants"].sum())
total_volunteers = int(filtered_df["volunteers"].sum())
avg_engagement = round(filtered_df["engagement_score"].mean(), 2)
total_signups = int(filtered_df["followup_signups"].sum())

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Events", total_events)
col2.metric("Total Participants", total_participants)
col3.metric("Total Volunteers", total_volunteers)
col4.metric("Follow-up Signups", total_signups)
col5.metric("Avg Engagement", avg_engagement)

st.markdown("---")

# ----------------------------
# Key insights
# ----------------------------
st.subheader("Key Insights")

top_county = filtered_df.groupby("county")["participants"].sum().idxmax()
top_program = filtered_df.groupby("program_type")["participants"].sum().idxmax()
top_channel = filtered_df.groupby("outreach_channel")["volunteers"].sum().idxmax()
top_language = filtered_df.groupby("language")["engagement_score"].mean().idxmax()

insight_col1, insight_col2 = st.columns(2)

with insight_col1:
    st.info(f"Highest participation county: **{top_county}**")
    st.info(f"Most attended program type: **{top_program}**")

with insight_col2:
    st.info(f"Strongest volunteer support channel: **{top_channel}**")
    st.info(f"Highest average engagement language group: **{top_language}**")

# ----------------------------
# Charts
# ----------------------------
st.subheader("Participants by County")
county_summary = filtered_df.groupby("county")["participants"].sum().sort_values(ascending=False)
st.bar_chart(county_summary)

st.subheader("Participants by Program Type")
program_summary = filtered_df.groupby("program_type")["participants"].sum().sort_values(ascending=False)
st.bar_chart(program_summary)

st.subheader("Monthly Participation Trend")
monthly_summary = filtered_df.groupby("month")["participants"].sum().sort_index()
st.line_chart(monthly_summary)

st.subheader("Average Engagement by Language")
language_summary = filtered_df.groupby("language")["engagement_score"].mean().sort_values(ascending=False)
st.bar_chart(language_summary)

st.subheader("Volunteers by Outreach Channel")
channel_summary = filtered_df.groupby("outreach_channel")["volunteers"].sum().sort_values(ascending=False)
st.bar_chart(channel_summary)

# ----------------------------
# Data Quality Section
# ----------------------------
st.subheader("Data Quality Snapshot")

quality_df = pd.DataFrame({
    "Metric": [
        "Rows in cleaned dataset",
        "Duplicate rows remaining",
        "Missing language values",
        "Missing participant values",
        "Unique counties",
        "Unique program types",
        "Unique outreach channels"
    ],
    "Value": [
        len(df),
        int(df.duplicated().sum()),
        int((df["language"] == "Unknown").sum()),
        int(df["participants"].isna().sum()),
        int(df["county"].nunique()),
        int(df["program_type"].nunique()),
        int(df["outreach_channel"].nunique())
    ]
})

st.dataframe(quality_df, use_container_width=True)

# ----------------------------
# Data preview
# ----------------------------
st.subheader("Cleaned Data Preview")
st.dataframe(filtered_df.head(20), use_container_width=True)

# ----------------------------
# Final takeaway
# ----------------------------
st.markdown("---")
st.subheader("Prototype Value")
st.write(
    """
    This dashboard prototype illustrates how outreach, participation, volunteer activity, 
    and engagement data can be transformed into actionable reporting for nonprofit programs. 
    It also demonstrates a simple data quality workflow to support more reliable internal reporting.
    """
)

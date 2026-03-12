# FLIC Outreach & Engagement Analytics Dashboard

A nonprofit analytics prototype designed to demonstrate how outreach, participation, volunteer activity, and data quality workflows can be organized into a simple reporting system.

## Project Overview

This project simulates how a nonprofit organization could structure and analyze outreach data to support program reporting, stakeholder visibility, and strategic decision-making.

The prototype includes:

- a simulated outreach dataset
- a data cleaning pipeline
- an interactive Streamlit dashboard
- participation and engagement metrics
- volunteer activity analysis
- data quality monitoring

## Dashboard Features

- Total events, participants, volunteers, follow-up signups, and engagement metrics
- Participation by county
- Participation by program type
- Monthly outreach trend analysis
- Average engagement by language
- Volunteer activity by outreach channel
- Data quality snapshot
- Interactive filters for county and program type

## Project Structure

```text
FLIC-outreach-analytics-prototype/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── outreach_raw.csv
│   └── outreach_cleaned.csv
├── scripts/
│   ├── create_sample_data.py
│   └── clean_data.py
└── images/
    ├── dashboard_overview.png
    ├── program_analytics.png
    ├── engagement_insights.png
    └── data_quality.png

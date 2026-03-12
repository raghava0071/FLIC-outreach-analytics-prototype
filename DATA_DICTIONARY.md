# Data Dictionary – Outreach Analytics Dataset

This document describes the structure and governance considerations for the simulated outreach dataset used in this project.

## Dataset Purpose

The dataset represents nonprofit outreach program activity including events, volunteer participation, and engagement indicators. The goal is to demonstrate how structured data can support reporting and analytics workflows.

## Table Structure

| Column | Description | Data Type | Example |
|------|------|------|------|
| event_id | Unique identifier for each outreach event | string | EVT1024 |
| county | Florida county where outreach event occurred | categorical | Miami-Dade |
| program_type | Type of outreach program conducted | categorical | Citizenship Workshop |
| participants | Number of community participants attending the event | integer | 42 |
| volunteers | Number of volunteers supporting the event | integer | 6 |
| language | Primary language used during outreach | categorical | Spanish |
| engagement_score | Calculated engagement indicator derived from participation and follow-up metrics | float | 0.82 |
| outreach_channel | Primary outreach channel used | categorical | SMS Campaign |
| month | Month when outreach event occurred | categorical | March |

## Data Quality Rules

To maintain consistent and reliable data:

- event_id must be unique
- participants must be >= 0
- volunteers must be >= 0
- engagement_score must be between 0 and 1
- program_type must belong to a predefined category list

## Data Governance Considerations

Although this dataset is simulated, real outreach systems should consider:

**Data Privacy**
- Personally identifiable information (PII) should not be stored in analytics datasets
- Individual participant data should be anonymized

**Access Control**
- Raw outreach datasets should be restricted to authorized staff
- Reporting dashboards should use aggregated data

**Data Documentation**
- Each dataset should include a data dictionary to ensure stakeholders understand field definitions and data sources

## Project Context

This dataset is generated for demonstration purposes to illustrate how nonprofit outreach data could be structured, cleaned, and analyzed for reporting and decision-making.

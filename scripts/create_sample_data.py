import pandas as pd
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
random.seed(42)

# Counties and cities
counties = ["Miami-Dade", "Broward", "Palm Beach", "Orange", "Hillsborough"]

cities = {
    "Miami-Dade": ["Miami", "Hialeah", "Homestead"],
    "Broward": ["Fort Lauderdale", "Hollywood", "Pembroke Pines"],
    "Palm Beach": ["West Palm Beach", "Boca Raton", "Delray Beach"],
    "Orange": ["Orlando", "Apopka", "Winter Park"],
    "Hillsborough": ["Tampa", "Brandon", "Plant City"]
}

program_types = [
    "Know Your Rights",
    "Citizenship Workshop",
    "Community Meeting",
    "Volunteer Training",
    "Voter Outreach"
]

channels = [
    "Phone Bank",
    "Text Campaign",
    "Community Event",
    "Partner Referral",
    "Social Media"
]

languages = ["English", "Spanish", "Haitian Creole"]

rows = []

start_date = datetime(2025, 1, 1)

for i in range(200):

    county = random.choice(counties)
    city = random.choice(cities[county])

    event_date = start_date + timedelta(days=random.randint(0, 365))

    program_type = random.choice(program_types)
    channel = random.choice(channels)
    language = random.choice(languages)

    participants = random.randint(15, 300)
    volunteers = random.randint(2, 25)

    followup_signups = random.randint(0, participants // 2)

    engagement_score = round(random.uniform(1.5, 5.0), 2)

    notes = random.choice([
        "High turnout",
        "Needed more volunteers",
        "Strong community response",
        "Follow-up requested",
        "Good multilingual support"
    ])

    rows.append([
        event_date.strftime("%Y-%m-%d"),
        county,
        city,
        program_type,
        channel,
        language,
        participants,
        volunteers,
        followup_signups,
        engagement_score,
        notes
    ])

# Create DataFrame
df = pd.DataFrame(rows, columns=[
    "event_date",
    "county",
    "city",
    "program_type",
    "outreach_channel",
    "language",
    "participants",
    "volunteers",
    "followup_signups",
    "engagement_score",
    "notes"
])

# Add a few intentional data issues
df.loc[5, "city"] = "miami"
df.loc[12, "language"] = None
df.loc[18, "participants"] = None

# Duplicate a row intentionally
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

# Save file
df.to_csv("data/outreach_raw.csv", index=False)

print("Sample dataset created successfully.")
print("File location: data/outreach_raw.csv")

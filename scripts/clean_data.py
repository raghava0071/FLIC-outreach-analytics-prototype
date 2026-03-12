import pandas as pd

print("Loading raw dataset...")

# Load raw dataset
df = pd.read_csv("data/outreach_raw.csv")

print("Initial dataset shape:", df.shape)

# ---------------------------
# Remove duplicate rows
# ---------------------------
df = df.drop_duplicates()

# ---------------------------
# Standardize text fields
# ---------------------------
df["city"] = df["city"].astype(str).str.title().str.strip()
df["county"] = df["county"].astype(str).str.title().str.strip()
df["program_type"] = df["program_type"].astype(str).str.strip()
df["outreach_channel"] = df["outreach_channel"].astype(str).str.strip()

# ---------------------------
# Handle missing values
# ---------------------------
df["language"] = df["language"].fillna("Unknown")

# Convert participants to numeric safely
df["participants"] = pd.to_numeric(df["participants"], errors="coerce")

# Replace missing participants with median
median_participants = df["participants"].median()
df["participants"] = df["participants"].fillna(median_participants)

# ---------------------------
# Convert date column
# ---------------------------
df["event_date"] = pd.to_datetime(df["event_date"], errors="coerce")

# Create month column for analysis
df["month"] = df["event_date"].dt.to_period("M").astype(str)

# ---------------------------
# Data Quality Checks
# ---------------------------
missing_languages = (df["language"] == "Unknown").sum()
missing_participants = df["participants"].isna().sum()

print("Missing language entries:", missing_languages)
print("Missing participant entries:", missing_participants)

# ---------------------------
# Save cleaned dataset
# ---------------------------
df.to_csv("data/outreach_cleaned.csv", index=False)

print("Cleaned dataset saved to: data/outreach_cleaned.csv")
print("Final dataset shape:", df.shape)

import pandas as pd

df = pd.read_csv("data/south_asia_ai.csv")

# print(df.head())
# print(df.columns.tolist())
# print(df.shape)

# important columns select
cols = [
    "Country",
    "Year",
    "GDP_USD_Bn",
    "RD_Pct_GDP",
    "AI_Market_Size_USDm",
    "AI_Startup_Investment_USDm",
    "Total_Startup_Investment_USDm",
    "AI_Readiness_Score",
    "AI_Employment_Pct",
    "Internet_Penetration_Pct",
    "AI_Adoption_Rate_Pct",
    "AI_Market_Intensity_Pct_GDP",
    "AI_Inv_Pct_Total_Startup"
]

df = df[cols].copy()

print(df.isnull().sum())
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.impute import SimpleImputer


# =========================
# 0. FOLDER SETUP
# =========================
os.makedirs("output", exist_ok=True)


# =========================
# 1. LOAD DATA
# =========================
df = pd.read_csv("data/south_asia_ai.csv")
df.columns = df.columns.str.strip()

print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)


# =========================
# 2. SELECT IMPORTANT COLUMNS
# =========================
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
    "AI_Market_Pct_GDP",
    "AI_Inv_Pct_Total_Startup"
]

df = df[cols].copy()


# =========================
# 3. CLEAN NUMERIC COLUMNS
# =========================
numeric_cols = [
    "GDP_USD_Bn",
    "RD_Pct_GDP",
    "AI_Market_Size_USDm",
    "AI_Startup_Investment_USDm",
    "Total_Startup_Investment_USDm",
    "AI_Readiness_Score",
    "AI_Employment_Pct",
    "Internet_Penetration_Pct",
    "AI_Adoption_Rate_Pct",
    "AI_Market_Pct_GDP",
    "AI_Inv_Pct_Total_Startup"
]

for col in numeric_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.strip()
        .replace(["", "nan", "None"], np.nan)
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)


# =========================
# 4. TABLE 2: DESCRIPTIVE STATISTICS
# =========================
desc_cols = [
    "GDP_USD_Bn",
    "RD_Pct_GDP",
    "AI_Market_Size_USDm",
    "AI_Startup_Investment_USDm",
    "Total_Startup_Investment_USDm",
    "AI_Readiness_Score",
    "AI_Employment_Pct",
    "Internet_Penetration_Pct",
    "AI_Adoption_Rate_Pct",
    "AI_Market_Pct_GDP",
    "AI_Inv_Pct_Total_Startup"
]

desc = df[desc_cols].describe().T
desc = desc[["count", "mean", "std", "min", "max"]]
desc.columns = ["Observations", "Mean", "Std_Dev", "Min", "Max"]

print("\nTable 2: Descriptive Statistics")
print(desc)

desc.to_csv("output/table2_descriptive_statistics.csv", index=True)


# =========================
# 5. TABLE 3: CORRELATION MATRIX
# =========================
corr = df[desc_cols].corr(numeric_only=True)

print("\nTable 3: Correlation Matrix")
print(corr)

corr.to_csv("output/table3_correlation_matrix.csv", index=True)


# 6. TABLE 4: FE REGRESSION 

df_emp = df[[
    "Country",
    "Year",
    "AI_Employment_Pct",
    "AI_Adoption_Rate_Pct",
    "AI_Readiness_Score",
    "AI_Market_Pct_GDP",
    "AI_Inv_Pct_Total_Startup",
    "Internet_Penetration_Pct",
    "RD_Pct_GDP"
]].dropna().copy()

model_emp = smf.ols(
    """
    AI_Employment_Pct ~
    AI_Adoption_Rate_Pct +
    AI_Readiness_Score +
    AI_Market_Pct_GDP +
    AI_Inv_Pct_Total_Startup +
    Internet_Penetration_Pct +
    RD_Pct_GDP +
    C(Country) +
    C(Year)
    """,
    data=df_emp
).fit(cov_type="HC1")


def stars(p):
    if p < 0.01:
        return "***"
    elif p < 0.05:
        return "**"
    elif p < 0.1:
        return "*"
    else:
        return ""

emp_results = pd.DataFrame({
    "Variable": model_emp.params.index,
    "Coefficient": model_emp.params.values,
    "Std_Error": model_emp.bse.values,
    "P_Value": model_emp.pvalues.values
})


emp_results["Variable"] = (
    emp_results["Variable"]
    .str.replace("C(Year)[T.", "Year ", regex=False)
    .str.replace("C(Country)[T.", "", regex=False)
    .str.replace("]", "", regex=False)
)


emp_results["Variable"] = emp_results["Variable"].replace({
    "AI_Adoption_Rate_Pct": "AI Adoption",
    "AI_Readiness_Score": "AI Readiness",
    "AI_Market_Pct_GDP": "AI Market (% GDP)",
    "AI_Inv_Pct_Total_Startup": "AI Investment Share",
    "Internet_Penetration_Pct": "Internet Penetration",
    "RD_Pct_GDP": "R&D (% GDP)"
})


emp_results["Significance"] = emp_results["P_Value"].apply(stars)


emp_results["Coefficient"] = emp_results["Coefficient"].round(3)
emp_results["Std_Error"] = emp_results["Std_Error"].round(3)
emp_results["P_Value"] = emp_results["P_Value"].round(3)

print("\nTable 4 :")
print(emp_results)

emp_results.to_csv("output/table4_fe_ai_employment.csv", index=False)


# 7. TABLE 5: FE REGRESSION (GDP)

df_gdp = df[[
    "Country",
    "Year",
    "GDP_USD_Bn",
    "AI_Adoption_Rate_Pct",
    "AI_Readiness_Score",
    "AI_Market_Pct_GDP",
    "AI_Inv_Pct_Total_Startup",
    "Internet_Penetration_Pct",
    "RD_Pct_GDP"
]].dropna().copy()

df_gdp = df_gdp[df_gdp["GDP_USD_Bn"] > 0].copy()
df_gdp["log_GDP"] = np.log(df_gdp["GDP_USD_Bn"])

model_gdp = smf.ols(
    """
    log_GDP ~
    AI_Adoption_Rate_Pct +
    AI_Readiness_Score +
    AI_Market_Pct_GDP +
    AI_Inv_Pct_Total_Startup +
    Internet_Penetration_Pct +
    RD_Pct_GDP +
    C(Country) +
    C(Year)
    """,
    data=df_gdp
).fit(cov_type="HC1")

gdp_results = pd.DataFrame({
    "Variable": model_gdp.params.index,
    "Coefficient": model_gdp.params.values,
    "Std_Error": model_gdp.bse.values,
    "P_Value": model_gdp.pvalues.values
})

gdp_results["Variable"] = (
    gdp_results["Variable"]
    .str.replace("C(Year)[T.", "Year ", regex=False)
    .str.replace("C(Country)[T.", "", regex=False)
    .str.replace("]", "", regex=False)
)

gdp_results["Variable"] = gdp_results["Variable"].replace({
    "AI_Adoption_Rate_Pct": "AI Adoption",
    "AI_Readiness_Score": "AI Readiness",
    "AI_Market_Pct_GDP": "AI Market (% GDP)",
    "AI_Inv_Pct_Total_Startup": "AI Investment Share",
    "Internet_Penetration_Pct": "Internet Penetration",
    "RD_Pct_GDP": "R&D (% GDP)"
})

gdp_results["Significance"] = gdp_results["P_Value"].apply(stars)

gdp_results["Coefficient"] = gdp_results["Coefficient"].round(3)
gdp_results["Std_Error"] = gdp_results["Std_Error"].round(3)
gdp_results["P_Value"] = gdp_results["P_Value"].round(3)

gdp_results.to_csv("output/table5_fe_economic_performance.csv", index=False)

# =========================
# 8. TABLE 6: RANDOM FOREST
# =========================
features = [
    "AI_Adoption_Rate_Pct",
    "AI_Readiness_Score",
    "AI_Market_Pct_GDP",
    "AI_Inv_Pct_Total_Startup",
    "Internet_Penetration_Pct",
    "RD_Pct_GDP"
]

target = "AI_Employment_Pct"

rf_data = df[features + [target]].copy()

X = rf_data[features]
y = rf_data[target]

mask = y.notna()
X = X[mask]
y = y[mask]

imputer = SimpleImputer(strategy="median")
X_imputed = imputer.fit_transform(X)

rf = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

scores = cross_val_score(rf, X_imputed, y, cv=5, scoring="r2")
print("\nRandom Forest CV R2 scores:", scores)
print("Average CV R2:", scores.mean())

rf.fit(X_imputed, y)

importance_df = pd.DataFrame({
    "Variable": features,
    "Importance": rf.feature_importances_
}).sort_values("Importance", ascending=False)

print("\nTable 6: Random Forest Variable Importance")
print(importance_df)

importance_df.to_csv("output/table6_rf_importance.csv", index=False)


# =========================
# 9. FIGURE 2: SOUTH ASIA AI MARKET TREND
# =========================
plot_df = df[df["Year"].between(2020, 2025)].copy()

plt.figure(figsize=(10, 6))
for country in plot_df["Country"].dropna().unique():
    temp = plot_df[plot_df["Country"] == country]
    plt.plot(temp["Year"], temp["AI_Market_Size_USDm"], marker="o", label=country)

plt.xlabel("Year")
plt.ylabel("AI Market Size (USD million)")
plt.title("Growth in AI Market Size across South Asia, 2020–2025")
plt.legend()
plt.tight_layout()
plt.savefig("output/figure2_ai_market_trend.png", dpi=300)
plt.show()


# =========================
# 10. FIGURE 3: BANGLADESH TREND
# =========================
bd = df[(df["Country"] == "Bangladesh") & (df["Year"].between(2020, 2025))].copy()

fig, ax1 = plt.subplots(figsize=(9, 5))

ax1.plot(bd["Year"], bd["AI_Market_Size_USDm"], marker="o")
ax1.set_xlabel("Year")
ax1.set_ylabel("AI Market Size (USD million)")

ax2 = ax1.twinx()
ax2.plot(bd["Year"], bd["AI_Inv_Pct_Total_Startup"], marker="s")
ax2.set_ylabel("AI Investment Share (%)")

plt.title("Bangladesh: AI Market Size and AI Investment Share")
plt.tight_layout()
plt.savefig("output/figure3_bangladesh_trend.png", dpi=300)
plt.show()


# =========================
# 11. FIGURE 4: AI ADOPTION VS EMPLOYMENT
# =========================
x = df["AI_Adoption_Rate_Pct"]
y = df["AI_Employment_Pct"]

mask = x.notna() & y.notna()
x = x[mask]
y = y[mask]

plt.figure(figsize=(8, 5))
plt.scatter(x, y)

if len(x) > 1:
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b)

plt.xlabel("AI Adoption Rate (%)")
plt.ylabel("AI Employment Share (%)")
plt.title("AI Adoption and AI-Related Employment")
plt.tight_layout()
plt.savefig("output/figure4_adoption_employment.png", dpi=300)
plt.show()


# =========================
# 12. FIGURE 5: RF FEATURE IMPORTANCE
# =========================
importance_df_plot = pd.read_csv("output/table6_rf_importance.csv")

plt.figure(figsize=(8, 5))
plt.barh(importance_df_plot["Variable"], importance_df_plot["Importance"])
plt.xlabel("Importance")
plt.ylabel("Variable")
plt.title("Random Forest Feature Importance")
plt.tight_layout()
plt.savefig("output/figure5_rf_importance.png", dpi=300)
plt.show()


print("\nAll tables and figures have been generated successfully in the output folder.")
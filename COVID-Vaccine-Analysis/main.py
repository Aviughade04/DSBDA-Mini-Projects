# ============================================================
#   COVID VACCINE DATA ANALYTICS — Mini Project
#   Tools: Python, Pandas, Matplotlib
#   Level: Beginner
# ============================================================

# ── STEP 1: Import Libraries ─────────────────────────────────
import pandas as pd          # for data handling
import matplotlib.pyplot as plt  # for charts
import os                      # to check file path


# ── STEP 2: Create Sample Dataset (CSV file) ──────────────────
# We create the CSV programmatically so you don't need an external file

data = {
    'State': [
        'Maharashtra', 'Delhi', 'Karnataka', 'Tamil Nadu',
        'Uttar Pradesh', 'Gujarat', 'West Bengal', 'Rajasthan'
    ],
    'First_Dose': [
        1200000, 980000, 870000, 750000,
        1500000, 920000, 830000, 680000
    ],
    'Second_Dose': [
        950000, 760000, 640000, 580000,
        1100000, 710000, 620000, 510000
    ],
    'Male_Vaccinated': [
        640000, 510000, 450000, 380000,
        820000, 490000, 420000, 360000
    ],
    'Female_Vaccinated': [
        560000, 470000, 420000, 370000,
        680000, 430000, 410000, 320000
    ]
}

# Save to CSV file
df_raw = pd.DataFrame(data)
df_raw.to_csv('vaccine_data.csv', index=False)
print("✅ vaccine_data.csv created successfully!\n")


# ── STEP 3: Load the Dataset ──────────────────────────────────
# pd.read_csv() reads the CSV file into a DataFrame (like an Excel table)

df = pd.read_csv('vaccine_data.csv')
print("📂 Dataset loaded successfully!")
print(f"   Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")


# ── STEP 4: Display First 5 Rows ─────────────────────────────
# df.head() shows the top 5 rows — a quick look at the data

print("=" * 60)
print("📋 FIRST 5 ROWS OF DATASET")
print("=" * 60)
print(df.head())
print()


# ── STEP 5: Total First Dose Vaccinations ─────────────────────
# .sum() adds up all values in a column

total_first_dose = df['First_Dose'].sum()
print("=" * 60)
print("💉 VACCINATION TOTALS")
print("=" * 60)
print(f"Total First Dose Vaccinations  : {total_first_dose:,}")


# ── STEP 6: Total Second Dose Vaccinations ────────────────────

total_second_dose = df['Second_Dose'].sum()
print(f"Total Second Dose Vaccinations : {total_second_dose:,}")
print()


# ── STEP 7: Male vs Female Vaccination Comparison ─────────────
# Compare total male and female vaccinated counts across all states

total_male   = df['Male_Vaccinated'].sum()
total_female = df['Female_Vaccinated'].sum()

print("=" * 60)
print("👥 GENDER-WISE VACCINATION COMPARISON")
print("=" * 60)
print(f"Total Male Vaccinated   : {total_male:,}")
print(f"Total Female Vaccinated : {total_female:,}")

if total_male > total_female:
    print(f"📊 Males were vaccinated more by {total_male - total_female:,}")
else:
    print(f"📊 Females were vaccinated more by {total_female - total_male:,}")
print()


# ── STEP 8: Bar Chart — Male vs Female Vaccination ────────────
# Matplotlib creates a visual bar chart for easy comparison

categories = ['Male Vaccinated', 'Female Vaccinated']
values     = [total_male, total_female]
colors     = ['#00d4ff', '#c084fc']   # blue for male, purple for female

plt.figure(figsize=(8, 5))            # set chart size
bars = plt.bar(
    categories, values,
    color=colors,
    width=0.5,
    edgecolor='white',
    linewidth=0.8
)

# Add value labels on top of each bar
for bar, val in zip(bars, values):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 20000,
        f'{val:,}',
        ha='center', va='bottom',
        fontsize=12, fontweight='bold'
    )

plt.title('COVID Vaccination: Male vs Female Comparison',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Total Vaccinated Count', fontsize=12)
plt.ylim(0, max(values) * 1.2)       # add space above bars
plt.grid(axis='y', alpha=0.3)         # light horizontal grid
plt.tight_layout()
plt.savefig('vaccination_chart.png', dpi=150) # save chart
plt.show()                             # display chart
print("📊 Bar chart saved as vaccination_chart.png")

print("\n✅ Project complete!")

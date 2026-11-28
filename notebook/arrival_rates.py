import pandas as pd

#TODO(next session):
#-Fix the check: print(seconds.max() instead of minutes.max)
#Add section 8 - arrival rate per session
#REVIEW CODE so that I understand

DATA_PATH = "data/raw/security_checkpoint_data.xlsx"
START_COL = "Time Start Baggage drop off"
SLOW_TYPES = ["senior", "family", "PRM"] #PRM stands for Persons with Reduced Mobility
EXPERIMENTAL_DAYS = ["2018_12_06", "2018_12_17", "2018_12_18"]

def hhmmss_to_seconds(t):
    """Convert a time string in the format hh:mm:ss to seconds."""
    hours = t // 10000
    minutes = (t // 100) % 100
    seconds = t % 100
    return hours * 3600 + minutes * 60 + seconds

sheets = pd.read_excel(DATA_PATH, sheet_name=None)
print("Sheets loaded:", len(sheets))
print("Sheets names:", list(sheets.keys()))
print()

print("Sheet, rows, columns, time range (HHMMSS)")
for name, table in sheets.items():
    start = table[START_COL]
    print(f" {name}: {len(table)} rows, {len(table.columns)} cols, " #gives the name of the sheet, and the length of passengers and columns there are
          f"{start.min():.0f} to {start.max():.0f}") #gives the time range of the sheet of arrival hours by taking the min & max values
    
print()

print("Share of slow type passengers in each sheet")
for name, table in sheets.items():
    share = table[SLOW_TYPES].sum(axis=1).gt(0).mean()
    print(f" {name}: {share:.2%}") #gives the share of slow type passengers in each sheet
print()

df = pd.concat(sheets, names=["day", "row"]).reset_index(level="day")
df["date"] = df["day"].str[:10]
df["experimental"] = df["date"].isin(EXPERIMENTAL_DAYS)

print("Total passengers:", len(df))

sheet_per_date = df.groupby("date")["day"].nunique()
print("Distincts days:", len(sheet_per_date))
print("Dates with two sheets:", list(sheet_per_date[sheet_per_date > 1].index))
print()

before = len(df)
df = df.dropna(subset=[START_COL])
print("Removed", before - len(df), "passengers with no start time")

minutes = (df[START_COL] // 100) % 100
seconds = df[START_COL] % 100
print("Max minutes:", minutes.max(), "| Min minutes:", minutes.min())

df["start_s"] = hhmmss_to_seconds(df[START_COL])
df["hour"] = (df[START_COL] // 10000).astype(int)
print("Earliest hour:", df["hour"].min(), "| Latest hour:", df["hour"].max())
print()

per_hour = df.groupby(["date", "hour"]).size()
print("Passengers per hour, per date:")
print(per_hour)
print()

avg = per_hour.mean()
busiest = per_hour.max()

print("Average passenger per hour:", round(avg, 1))
print("Busiest hour:", busiest)
print("Average gap between arrivals (s):", round(3600 / avg, 1))
print("Arrival rate λ (per second):", avg / 3600)
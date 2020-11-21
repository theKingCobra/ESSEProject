import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

# Import Data from Excel File
df = pd.read_excel("Ontario_Air_Quality_Data.xlsx", parse_dates=[['Date', 'Time']])
cols = ["Benzene", "O3", "PM2.5"]

# ------------ Preprocess Data to remove nans and strings ------------
df["Benzene"] = pd.to_numeric(df["Benzene"], errors='coerce')
df["O3"] = pd.to_numeric(df["O3"], errors='coerce')
df["PM2.5"] = pd.to_numeric(df["PM2.5"], errors='coerce')

datetime = df["Date_Time"]
benzene = df["Benzene"]
o3 = df["O3"]
pm25 = df["PM2.5"]

benz_df = pd.concat([datetime, benzene], axis=1, keys=["Date_Time", "Benzene"])
o3_df = pd.concat([datetime, o3], axis=1, keys=["Date_Time", "O3"])
pm25_df = pd.concat([datetime, pm25], axis=1, keys=["Date_Time", "PM2.5"])

benz_df = benz_df.dropna()
o3_df = o3_df.dropna()
pm25_df = pm25_df.dropna()

o3_df["Date_Time"] = pd.to_datetime(o3_df["Date_Time"])
benz_df["Date_Time"] = pd.to_datetime(benz_df["Date_Time"])
pm25_df["Date_Time"] = pd.to_datetime(pm25_df["Date_Time"])

weekday_map = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri',
               5:'Sat', 6:'Sun'}
# ------ End of Preprocessing ------


# --------- O3 Plots ---------
# --------- Hourly ---------
fig, axs = plt.subplots(figsize=(12,4))
o3_hourly = o3_df.groupby(o3_df["Date_Time"].dt.hour)["O3"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the Day")
plt.ylabel("03 Concentration (ppb)")
plt.title("Average Hourly O3 Concentration")

# --------- Daily ---------
fig, axs = plt.subplots(figsize=(12,4))
o3_daily = o3_df.groupby(o3_df["Date_Time"].dt.weekday)["O3"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Day of the week")
plt.ylabel("03 Concentration (ppb)")
plt.title("Average Daily O3 Concentration")

# --------- PM2.5 Plots ---------
# --------- Hourly ---------
fig, axs = plt.subplots(figsize=(12,4))
pm25_hourly = pm25_df.groupby(pm25_df["Date_Time"].dt.hour)["PM2.5"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the Day")
plt.ylabel("PM2.5 Concentration (ppb)")
plt.title("Average Hourly PM2.5 Concentration")

# --------- Daily ---------
fig, axs = plt.subplots(figsize=(12,4))
pm25_daily = pm25_df.groupby(pm25_df["Date_Time"].dt.weekday)["PM2.5"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Day of the week")
plt.ylabel("PM2.5 Concentration (ppb)")
plt.title("Average Daily PM2.5 Concentration")

# --------- Benzene Plots ---------
# --------- Hourly ---------
fig, axs = plt.subplots(figsize=(12,4))
benz_hourly = benz_df.groupby(benz_df["Date_Time"].dt.hour)["Benzene"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the Day")
plt.ylabel("Benzene Concentration (ppb)")
plt.title("Average Hourly Benzene Concentration")

# --------- Daily ---------
fig, axs = plt.subplots(figsize=(12,4))
benz_daily = benz_df.groupby(benz_df["Date_Time"].dt.weekday)["Benzene"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Day of the week")
plt.ylabel("Benzene Concentration (ppb)")
plt.title("Average Daily Benzene Concentration")

plt.show()
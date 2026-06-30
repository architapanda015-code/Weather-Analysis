import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

plt.style.use("seaborn-v0_8")

file_path = r"C:\Users\archi\OneDrive\Desktop\Healthcare_ Project\weather project\weather_data.csv"
df = pd.read_csv(file_path,sep=",")
print(df.columns.tolist())

df['Date/Time'] = pd.to_datetime(df['Date/Time'])

print("===\nOriginal Data: ===")
print(df.head())
print(df.info())
print(df.describe())

df.fillna({
    "precipitation":0,
    "Windspeed":df["Wind Speed_km/h"].mean(),
    "Humidity":df["Rel Hum_%"].mean()
},inplace=True)

df["month"]=df["Date/Time"].dt.month
df["day"]=df["Date/Time"].dt.day

avg_temp=df["Temp_C"].mean()
avg_humidity = df["Rel Hum_%"].mean()
print(f'Average Temperature: {avg_temp:.2f} C')
print(f'Average Humidity: {avg_humidity:.2f} C')

condition_count = df["Weather"].value_counts
print("\n===Condition Frequency===")
print(condition_count)

plt.figure(figsize = (10,5))
plt.plot(df["Date/Time"],df["Temp_C"], marker='o')
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize = (10,5))
plt.plot(df["Date/Time"],df["Rel Hum_%"], marker='o')
plt.title("Daily Rel Hum_% Trend")
plt.xlabel("Date")
plt.ylabel("Rel Hum_%")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize = (12,6))
sns.countplot(x="Weather",data=df)
plt.title("Weather Frequency")
plt.xlabel("Weather")
plt.ylabel("count")
plt.xticks(rotation=90, ha='right',fontsize=8)
plt.tight_layout()
plt.show()


plt.figure(figsize = (7,5))
sns.heatmap(df[["Temp_C","Dew Point Temp_C","Rel Hum_%","Wind Speed_km/h","Visibility_km"]].corr(),annot=True,cmap="coolwarm")
plt.title("correlation heatmap")
plt.tight_layout()
plt.show()

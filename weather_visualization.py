
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
API_KEY = "c00466ed3d7d3ff4afe03699fe26ac96"  
CITY = "Mumbai" 
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "q": CITY,          
    "appid": API_KEY,   
    "units": "metric"   
}
response = requests.get(BASE_URL, params=params)
if response.status_code == 200:
    data = response.json()
else:
    print("❌ Error fetching data:", response.status_code)
    exit()
weather_data = []
for item in data["list"]:
    dt = datetime.fromtimestamp(item["dt"])
    temp = item["main"]["temp"]
    humidity = item["main"]["humidity"]
    pressure = item["main"]["pressure"]
    desc = item["weather"][0]["description"]
    weather_data.append({
        "Datetime": dt,
        "Temperature (°C)": temp,
        "Humidity (%)": humidity,
        "Pressure (hPa)": pressure,
        "Condition": desc
    })
df = pd.DataFrame(weather_data)
df.to_csv("weather_data.csv", index=False)
print("✅ Weather data saved as weather_data.csv")
print("✅ Sample Data:")
print(df.head())
sns.set(style="darkgrid")
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Datetime", y="Temperature (°C)", color="orange")
plt.title(f"Temperature Trend in {CITY}")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Datetime", y="Humidity (%)", color="blue")
plt.title(f"Humidity Trend in {CITY}")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Datetime", y="Pressure (hPa)", color="green")
plt.title(f"Pressure Trend in {CITY}")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

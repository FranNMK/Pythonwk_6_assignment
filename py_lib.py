# Challenge: Use popular Python libraries to perform useful tasks!

# 1. Import libraries
import numpy as np        # numerical operations
import pandas as pd       # data manipulation
import matplotlib.pyplot as plt  # data visualization
import requests           # web requests

# -------------------------------
# 2. NumPy Task
# Create a NumPy array of numbers from 1 to 10 and calculate the mean
arr = np.arange(1, 11)  # array([1, 2, ..., 10])
print("NumPy Array:", arr)
print("Mean of array:", arr.mean())

# -------------------------------
# 3. Pandas Task
# Create a small dataset and load into a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 18, 35],
    "Score": [85, 90, 78, 92]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

print("\nSummary Statistics:")
print(df.describe())  # numerical summary (count, mean, std, etc.)

# -------------------------------
# 4. Requests Task
# Fetch data from a public API (Open-Meteo Weather API)
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true"
response = requests.get(url, timeout=10)

if response.status_code == 200:
    weather_data = response.json()
    temp = weather_data["current_weather"]["temperature"]
    windspeed = weather_data["current_weather"]["windspeed"]
    print(f"\nCurrent Temperature in Berlin: {temp} °C")
    print(f"Current Windspeed in Berlin: {windspeed} km/h")
else:
    print("\nFailed to fetch weather data from API.")

# -------------------------------
# 5. Matplotlib Task
# Plot a simple line graph
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]

plt.plot(numbers, squares, marker='o', color='blue', linestyle='--')
plt.title("Numbers vs Squares")
plt.xlabel("Numbers")
plt.ylabel("Squares")
plt.grid(True)
plt.show()

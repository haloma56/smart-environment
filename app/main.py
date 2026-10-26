import pandas as pd  # pyright: ignore[reportMissingModuleSource]

# Read environmental data
data = pd.read_csv("data/environment_data.csv")

print("=== Smart Environment Monitoring System ===")
print()

# Display data
print("Environmental Data:")
print(data)

print()
print("=== Statistics ===")

# Calculate averages
average_temperature = data["temperature"].mean()
average_humidity = data["humidity"].mean()
average_air_quality = data["air_quality"].mean()

print(f"Average Temperature: {average_temperature:.2f} °C")
print(f"Average Humidity: {average_humidity:.2f} %")
print(f"Average Air Quality: {average_air_quality:.2f}")
print()
print("=== Environmental Status ===")

if average_temperature > 35:
    print("Temperature Status: CRITICAL")
elif average_temperature > 30:
    print("Temperature Status: WARNING")
else:
    print("Temperature Status: NORMAL")


if average_humidity > 80:
    print("Humidity Status: CRITICAL")
elif average_humidity > 70:
    print("Humidity Status: WARNING")
else:
    print("Humidity Status: NORMAL")


if average_air_quality > 100:
    print("Air Quality Status: CRITICAL")
elif average_air_quality > 70:
    print("Air Quality Status: WARNING")
else:
    print("Air Quality Status: GOOD")

import matplotlib.pyplot as plt  # pyright: ignore[reportMissingModuleSource]

plt.figure(figsize=(10, 5))

plt.plot(data["temperature"], label="Temperature")
plt.plot(data["humidity"], label="Humidity")
plt.plot(data["air_quality"], label="Air Quality")

plt.title("Environmental Measurements")
plt.xlabel("Measurement")
plt.ylabel("Value")

plt.legend()
plt.grid()

plt.show()
import numpy as np

days = int(input("Enter number of days: "))
temperatures = []
count = 0
for i in range(days):
    temperatures.append(float(input(f"Day {i}'s high temperature: ")))

mean_temperature = np.mean(temperatures)

for temperature in temperatures:
    if temperature > mean_temperature:
        count += 1

print("Average temperature", mean_temperature)
print(f"{count} days above average temperature")

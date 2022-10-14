temperatures = []
months  = ["january:", "february","march","april","may","june","july","august","september","october","november","december"]
for i in months:
    temps = int(input(f"enter the temperature for {i}"))
    temperatures.append(temps)
temperatures.sort()
print(temperatures)

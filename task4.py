allowed_values = ["f", "F", "c", "C"]
temperature_format = "0"
while temperature_format not in allowed_values:
    temperature_format = input("Vill du ange temperaturen i Celsius (C) eller Fahrenheit (F)?")
if temperature_format.lower() == "f":
    temperature_F = input("Skriv in en temperatur i grader Fahrenheit: ")
    temperature_F = float(temperature_F)
    temperature_C = (temperature_F - 32) / 1.8
    print(f"{temperature_C} C")
else:
    temperature_C = input("Skriv in en temperatur i grader Celsius: ")
    temperature_C = float(temperature_C)
    temperature_F = 1.8 * temperature_C + 32
    print(f"{temperature_F} F")

if temperature_C >= 20:
    print("packa gärna badkläder med...")
if temperature_C < 10:
    print("ta på dig vinterkläder!")


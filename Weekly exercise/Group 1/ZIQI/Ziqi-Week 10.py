#1
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
elif bmi >= 30:
    print("Obesity")
else:
    print("Error in calculating BMI")
# BMI Calculator

#2
income = float(input("Enter your annual income (£): "))

allowance = 12570
if income > 100000:
    reduction = (income - 100000) / 2
    allowance = max(0, allowance - reduction)

taxable = max(0, income - allowance)
tax = 0

basic_band = 37700
higher_band = 74970

if taxable > 0:
    amount = min(taxable, basic_band)
    tax += amount * 0.20
    taxable -= amount

if taxable > 0:
    amount = min(taxable, higher_band)
    tax += amount * 0.40
    taxable -= amount

if taxable > 0:
    tax += taxable * 0.45

print(f"Your total income tax is: £{tax}")

#3
input_temperature_format = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
temperature = float(input("Enter the temperature: "))
if input_temperature_format == 'C':
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C is {fahrenheit}°F")
elif input_temperature_format == 'F':
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F is {celsius}°C")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
#4
number = int(input("Enter an integer: "))
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif number < 0:
    if number // 3 == 0:
        print("The number is negative and divisible by 3.")
    else:
        print("The number is negative and not divisible by 3.")
else:
    print("The number is zero.")
    
#5
year = int(input("Enter employee's service years: "))
salary = float(input("Enter employee's salary: "))
bonus = 0
if year > 5:
    if salary > 50000:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.15
    print(f"Bonus awarded: £{bonus}")
elif year <= 5:
    print("No bonus awarded.")
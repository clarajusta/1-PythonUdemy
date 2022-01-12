# Exercise 1
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Exercise 2
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Exercise 3
print(len(input("What is your name?")))

# Exercise 4

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
c = a
a = b
b = c
# Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# Day 1 Project

print("Welcome to the Band Name Generator")
city_name = input("What's name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
print("Your band name could be " + city_name + " " + pet_name)

# Exercise 6
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
first_string = two_digit_number[0]
second_string = two_digit_number[1]

print(first_string, "+", second_string, "=", int(first_string) + int(second_string))

# Exercise 7

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = float(weight)/(float(height)**2)
print(int(BMI))

# Exercise 8

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years = 90 - int(age)
months = years * 12
weeks = years * 52
days = years * 365

print(f'You have {days} days, {weeks} weeks, and {months} months left')


# Project Day 2

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill?")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15?")
number_people = input("How many people to split the bill?")

result = (float(total_bill)+((float(total_bill))*(float(percentage_tip)/100)))/int(number_people)
result_round = round(result, 2)
print(f"Each person should pay: ${result_round}")

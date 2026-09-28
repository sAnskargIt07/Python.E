def calculate_calories():
	carbs = float(input("Enter grams of carbs intake: "))
	fats = float(input("Enter grams of fats intake: "))
	proteins = float(input("Enter grams of protein intake: "))
	total_calories = (carbs * 4) + (fats * 9) + (proteins * 4)
	print("    ")
	print("-------------Daily Caloric Intake-------------")
	print("The total calories consumed in a day is", total_calories)
calculate_calories()
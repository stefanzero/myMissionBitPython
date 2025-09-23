"""
Goal
In this project, you’ll create a simple Python program to track your environmental impact,
focusing on the water used for showers. You’ll get introduced to basic Python concepts like
input/output, variables, constants, and simple calculations.
Stage 1: Input and Output
Get comfortable with capturing user input and displaying it.
1. Write a script that prompts you to enter the number of showers you take per week.
2. Write another script that prompts you to enter how long your average showers are.
3. Display the entered value to understand how input/output works.
Stage 2: Constants and Calculations
Use constants and do some basic math.
1. Define a constant for average water usage per shower.
a. Hint: Each 5 minute shower is 10 gallons of water
2. Calculate and print the total water consumption based on the user input.
Stage 3: Output and Formatting
Make sure that outputs are understandable.
1. Use Python’s string formatting to neatly label and display the water consumption results.
Stage 4: Project Completion and Reflection
Wrap things up and think about what you’ve learned.
1. Test your program with different inputs to make sure it works correctly.
2. Reflect on how tracking water usage can help people reduce their environmental impact
"""

QUESTION_SHOWERS_PER_WEEK = "Enter the number of showers you take per week: "


def enter_showers_per_week():
    return int(input(QUESTION_SHOWERS_PER_WEEK))


QUESTION_SHOWERS_LENGTH = "Enter the average length of your showers in minutes: "


def enter_shower_length():
    return int(input(QUESTION_SHOWERS_LENGTH))


def calculate_water_consumption(showers_per_week, shower_length):
    return showers_per_week * (shower_length / 5)  # 5 minutes per shower


AVERAGE_WATER_USAGE_PER_SHOWER = 10


def calculate_total_water_consumption(showers_per_week, shower_length):
    return (
        calculate_water_consumption(showers_per_week, shower_length)
        * AVERAGE_WATER_USAGE_PER_SHOWER
    )


def main():
    showers_per_week = enter_showers_per_week()
    print(showers_per_week)
    shower_length = enter_shower_length()
    total_water_consumption = calculate_total_water_consumption(
        showers_per_week, shower_length
    )
    print(f"You consume {total_water_consumption:.2f} gallons of water per week.")


"""
Goals:

In this update, you’ll take your Environmental Awareness Project to the next level by using string variables for input prompts and adding a new variable: the number of meals you eat per week.


Objective: Understand the new features and improvements..
Changes:
Use string variables to make input prompts more flexible and streamlined.
Step 1: More Inputs!

Objective: Enhance how you handle user inputs.
Actions:
Create string variables for prompts related to showers and meals.
Update your program to use these new variables for asking user inputs.
Step 2: Review Constants and Calculations

Objective: Make sure that calculations are still correct with the new inputs.
Actions:
Keep your current constants and add new ones if needed.
Update your calculations to include the environmental impact of the number of meals per week.
Step 3: Code Update

Objective:Implement and test the new features.
Actions:
Run your updated program to check that it works correctly and gives accurate results.

"""

if __name__ == "__main__":
    main()

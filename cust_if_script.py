#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'The semester is almost over, we recommend '

# wrap connection in a float() to accept decimals as numbers
grade = float(input("What is your current numeric grade?"))

# if input value was higher or equal to 25
if grade >= 90:
    message = message + 'continiung the great work.'
elif grade >= 80:
    message = message + 'continuing the great work and look into extra credit.'
elif grade >= 70:
    message = message + 'looking into extra credit options.'
else:
    message = message + 'preparing to retake class.'
print(message)


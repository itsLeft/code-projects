"""
Josh Sacharski
Step Counter
Create a script that calculates statistics about the number of steps the user has taken.

Input
Continuously ask the user to enter the number of steps they’ve taken each day until they enter -1.

Output
Once the user has finished entering their steps,
the script should output the number of days recorded, total steps,
average steps per day, and the most and least steps entered in a day.
"""

steps = int(input("Enter number of steps for Day 1 (0 to stop): "))
totalSteps = 0
days = 0
minSteps = steps
maxSteps = steps
while steps != 0:
    totalSteps += steps
    days += 1
    if steps > maxSteps:
        maxSteps = steps
    elif steps < minSteps:
        minSteps = steps
    steps = int(input(f"Enter number of steps for Day {days + 1} (0 to stop): "))
else:
    print(f"Total Steps: {totalSteps}")
    print(f"Total Days: {days}")
    print(f"Average Steps: {totalSteps / days}")
    print(f"The most steps taken is {maxSteps} and the least is {minSteps}")

# $150 for every A
# $75 for every B
# $100 (negative amount) for every class below a C
# 1 hour of playing time for every 2 hours of homework
# 1 hour of playing time for every 3 hours of chores
# 1 hour of playing time for every 4 hours of sports
import math

cost = input("Please enter the cost of the system: ")
numAs = input("How many A's did you earn last semester: ")
numBs = input("How many B's did you earn last semester: ")
numBelowC = input("How many grades under a C did you earn: ")
hoursHomework = input("How many hours of homework have been done")
hoursChores = input("How many hours of housework have been done")
hoursSports = input("How many hours of sports have been done")
print("-----------------------")
if int(cost) > (150 * int(numAs)) + (75 * int(numBs)) - (100 * int(numBelowC)):
    print("You may not buy a game system")
else:
    print("You may buy a game system")
playtime = 0
if int(hoursHomework) % 2 != 0:
    playtime += (math.trunc((int(hoursHomework) - 1) / 2))
else:
    playtime += (math.trunc(int(hoursHomework) / 2))

if int(hoursChores) % 3 != 0:
    playtime += (math.trunc((int(hoursChores) - 1) / 3))
else:
    playtime += (math.trunc(int(hoursChores) / 3))

if int(hoursSports) % 2 != 0:
    playtime += (math.trunc((int(hoursSports) - 1) / 4))
else:
    playtime += (math.trunc(int(hoursSports) / 4))

print("You have earned " + str(playtime) + " Hours of playtime")

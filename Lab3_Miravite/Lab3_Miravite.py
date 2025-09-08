"""
Gabriel Miravite
Lab 3
Sep 8, 2025
"""


print("\n========= Example 1: If, elif, ..., else (EXERCISE) =========")
"""
EXERCISE Instructions:
a) Use a while loop to validate if user_num is between 1 and 9
b) User can only guess 3 times.
"""

GUESS_NUM = 6
for g in range(0,3):
    user_num = int(input("Guess a number between 1 and 9: "))
    while user_num<1 or user_num>9:
        user_num = int(input("ERROR! Guess a number between 1 and 9: "))
    if(user_num == GUESS_NUM):
        print(f"Great job! {user_num} is the guess number.")
        break
    elif(user_num > GUESS_NUM):
        print(f"{user_num} should be lower.")
    elif(user_num < GUESS_NUM):
        print(f"{user_num} should be higher.")
    else:
        print(f"ERROR!")

print("End of guessing!")


print("\n========= Example 2: Control Flow w/ Logical Operators =========")
"""
"and"/"or"/"not"
children from 5 to 9 are given milk
children from 10 to 14 are given a sandwich
children from 15 to 17 are given a burger
"""
stu_age = int(input("Enter an age: "))
lunch = "None"
if stu_age>=5 and stu_age<=9:
    lunch = "milk"
elif stu_age>=10 and stu_age<=14:
    lunch = "sandwich"
elif stu_age>=15 and stu_age<=17:
    lunch = "burger"
else:
    lunch = "None"

print(f"At age {stu_age}, the food is {lunch}.")


print("\n========= Example 3: For Loop as a Counter =========")
for n in range(2,10):
    print(n)


print("\n========= Example 4: For Loop in a List =========")
years = [2011, 2005, 1998, 1980, 1973]
for y in years:
    print(y)

for index in range(len(years)):
    print(f"Year {index+1} = {years[index]}")


print("\n========= Example 5: While Loop as a Counter =========")
count = 1
while count<=5:
    print(count)
    count += 1


print("\n========= Example 6: While Loop to Validate a Number =========")
num = int(input("Enter a number between -5 and 5: "))
while num<-5 or num>5:
    num = int(input("ERROR! Enter a number between -5 and 5: "))
print(f"Entered number: {num}")
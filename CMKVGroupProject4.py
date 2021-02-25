'''
DOCUMENTATION: This is a podium generator for a track meet. Users must
enter names and finish times for three runners for an event, and the
program outputs the medals awarded according to placement.

The 'while' loop is utilized in order to prevent the user from giving a 
finish time less than or equal to zero.
'''

runner_1 = input("Please enter the name of runner #1: ")
runner_1_time = int(input("Please enter " + runner_1 + "'s finish time: "))
while runner_1_time <= 0:
    runner_1_time = int(input("Invalid time entry. Try again. "))
runner_2 = input("Please enter the name of runner #2: ")
runner_2_time = int(input("Please enter " + runner_2 + "'s finish time: "))
while runner_2_time <= 0:
    runner_2_time = int(input("Invalid time entry. Try again. "))
runner_3 = input("Please enter the name of runner #3: ")
runner_3_time = int(input("Please enter " + runner_3 + "'s finish time: "))
while runner_3_time <= 0:
    runner_3_time = int(input("Invalid time entry. Try again "))
if runner_1_time < runner_2_time < runner_3_time:
    print("Gold Medal Winner:", runner_1)
    print("Silver Medal Winner:", runner_2)
    print("Bronze Medal Winner:", runner_3)
elif runner_1_time < runner_3_time < runner_2_time:
    print("Gold Medal Winner:", runner_1)
    print("Silver Medal Winner:", runner_3)
    print("Bronze Medal Winner:", runner_2)
elif runner_2_time < runner_1_time < runner_3_time:
    print("Gold Medal Winner:", runner_2)
    print("Silver Medal Winner:", runner_1)
    print("Bronze Medal Winner:", runner_3)
elif runner_2_time < runner_3_time < runner_1_time:
    print("Gold Medal Winner:", runner_2)
    print("Silver Medal Winner:", runner_3)
    print("Bronze Medal Winner:", runner_1)
elif runner_1_time > runner_2_time > runner_3_time:
    print("Gold Medal Winner:", runner_3)
    print("Silver Medal Winner:", runner_2)
    print("Bronze Medal Winner:", runner_1)
elif runner_3_time < runner_1_time < runner_2_time:
    print("Gold Medal Winner:", runner_3)
    print("Silver Medal Winner:", runner_1)
    print("Bronze Medal Winner:", runner_2)

'''
A List function could also be employed to streamline the time
comparisons. Our group agreed to use simple "if else" statements to compare
runners' times due to the assignment's limitations.
'''


"""
TODO: randomly generate addition problems 
until the user has gotten 3 problems correct in a row.
"""

import random 

def main():
#set value correct to 0, if correct has a value of 3, game is finished.
    correct = 0
#while loop: as long as correct is not equal to 3
    while correct != 3 :
    #start the addition problem
    #generate the problem
        int_1 = random.randint(10,99)
        int_2 = random.randint(10,99)
        print("What is ", int_1, "+", int_2, "?")
    #ask for an answer
        your_answer = float(input("Your answer: "))
    #evalutate the solution
        correct_answer = int_1 + int_2
        if your_answer == correct_answer:
            correct = correct + 1
            print("Correct! You've gotten " + str(correct) + " correct in a row.")
        else:
            correct = 0 #wrong answer, so back to 0 :(
            print("Incorrect. The expected answer is ", correct_answer)
#while loop broken, congratulations! 3 in a row correct!!
    print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()
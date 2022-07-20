import sys
import random
import math
import time
print("Welcome to guessing game.")
name=input("What's your name? \n")
welcome=input("{}, Would you like to start playing game ? Enter Y/N \n".format(name))
if welcome.upper()=='N':
    print("See you later!")
    sys.exit()
else:
    print("Excellent! Let's start.")
time.sleep(0.5)
def get_number():
    x=True
    while x:
        min_number=input("What is your minimum number? \n")
        max_number=input("What is your maximum number? \n")
        if min_number.isnumeric() and max_number.isnumeric():
            min_number=int(min_number)
            max_number=int(max_number)
            limit_time=round(math.log(max_number-min_number+1,2))
            target_num=random.randint(min_number,max_number)
            return limit_time, target_num
        else:
            print("Please input number for minimum number and maximum number.")
def main():
    limit_tries, target_number=get_number() # limit_tries, target_number from get_number()
    print(f"You will have only {limit_tries} times to get exactly number.")
    count_tries=0
    while count_tries<limit_tries:
        guessing_number=int(input("Please input your guessing number: \n"))
        count_tries+=1
        if guessing_number==target_number:
            print(f"Congratulations you got right number in {count_tries} tries")
            break
        elif guessing_number>target_number:
            print(f"Your number is higher than our number. Please try again. You have {limit_tries-count_tries} tries remaining.")
        else:
            print(f"Your number is too low. Please try again. You have {limit_tries-count_tries} tries remaining.")     
    else:
        print(f"You've more than {limit_tries} tries. Try your luck next time!")

if __name__=="__main__":
    main()
    
import numpy as np

def generate_random_number(amt):
    """this fucntion will generate a random number based on the amount staked"""

    #generate random number
    ran_num_size = int((200/amt) * 1000)
    gen_ran_nums = np.random.randint(1000, 10000, ran_num_size).tolist()
    
    #generate random win number
    win_nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]
    gen_ran_win_num = np.random.choice(win_nums)

    #replace any occurence of winning already in the gen_ran_num
    for num in gen_ran_nums:
        if num in win_nums:
            gen_ran_nums.remove(num).append(1001)
    
    #remove an item from the list and replace with a winning number
    del gen_ran_nums[0]
    gen_ran_nums.append(gen_ran_win_num)

    random_number = np.random.choice(gen_ran_nums)
    return random_number



if __name__ == "__main__":

    rules = '''Gaming Rules: \nMinimum stake is N50 \nMaximum stake is N1000 \nMachine generates a 4 digits number randomly \nTo win, the number should have the same digits e.g 1111, 2222, 9999, 5555 etc'''
    print(rules)

    for i in range(100):

        for i in range(100):
            play = input("Ready to play? Press y: ")
            if play == 'y':
                enter_amt = int(input("Enter amount to play with: "))
                break
            else:
                print("Wrong option, you should press y to play") 

        for i in range(100):
            if enter_amt >= 50 and enter_amt <= 1000:
                result = generate_random_number(enter_amt)
                break
            else:
                print("Enter and amout not lower than N50 and not Larger N1000")
        
        print()
        print(f"Your random number is {result}")
        print()
       
        win_nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]
        if result in win_nums:
            print("YAAAAAAAAAAAAAAY! you won!")
            print()
            print(f"Your total winning is {enter_amt + (0.25*enter_amt)}")
        else:
            print("Sorry you lost. Pleas try again")

        play_again = True
        if play_again == True:
            continue
        else:
            break

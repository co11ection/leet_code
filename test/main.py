from random import randint
name = input("Write you name:")
wish = "Do you want to play?:\n Write: 'yes' or 'no'"

while True:
    trying = 0
    rand = randint(1,10)
    print(wish)
    choice = input(":")
    if choice == 'yes':
        print("I mad a number, and you need to find my number,\n so choose ONE number from 1 to 10:\n  ")
        se = int(input("Enter the num:"))
        trying += 1

        while se != rand:
            se = int(input("Enter the num:"))
            trying += 1

        
        print("My number is:", rand)
        print(f'you guessed it on  {trying} try')

    elif choice == 'no':
        print("See you!")
        break
    else:
        print("print only 'yes' or 'no'!!!")

l = 0
r = 100

print("Please think of a number between 0 and 100! ")

while l < r:
    mid =(l+r) // 2

    print("Is your secret number :")
    print(mid)

    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
    inp = input()

    if inp == 'c':
        print("Game over. Your secret number was: "str(mid))
        break
    
    elif inp == 'h':
        r = mid -1
    
    elif inp == 'l':
        l = mid + 1
    
    else:
        print("Incorrect option ")
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
        inp = input()

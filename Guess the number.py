print('Please think of a number between 0 and 100!')
low = 0
hight = 100
ans = int( (low + hight)/2)

while True:
    print("Is your secret number "+str(ans)+"?")
    manager = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
            
    if manager == 'l':
        low = ans
        ans_without_int = (low + hight)/2
        ans = int(ans_without_int)
        continue
    if manager == 'h':
        hight = ans
        ans_without_int = (low + hight)/2
        ans = int(ans_without_int)
        continue
    if manager == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
        continue
         
print("Game over. Your secret number was:" + str(ans))




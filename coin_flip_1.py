import random
print("This program will simulate a coin toss as many times as you want it to, and then tell you the results.")
while(True):
    heads = 0
    tails = 0
    number = raw_input("How many times would you like to flip the coin? ")
    for i in xrange(0, int(number)): 
        rando = random.randint(1,100)
        if rando <= 51:
            print("heads")
            heads += 1
        else:
            print("tails") 
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))
    if heads > tails:
        print("Heads wins!")
    elif heads < tails:
        print("Tails wins!")
    else:
        print("It's a tie!")
    go_again = raw_input("Would you like to go again? (yes/no)")
    if go_again.upper() == "NO":
        break
print ("The program has been closed")
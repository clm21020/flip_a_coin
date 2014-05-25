import random

def print_results(results):
    heads = results["heads"]
    tails = results["tails"]
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))
    if heads > tails:
        print("Heads wins!")
    elif heads < tails:
        print("Tails wins!")
    else:
        print("It's a tie!")

def flip_n_coins(n):
    results = {"heads": 0, "tails": 0}
    for i in xrange(0, int(n)): 
        rando = random.randint(1,100)
        if rando <= 51:
            print ("heads")
            results["heads"] += 1
        else:
            print ("tails")
            results["tails"] += 1
    return results

print("This program will simulate a coin toss as many times as you want it to, and then tell you the results.")
while(True):
    number = raw_input("How many times would you like to flip the coin? ")
    results = flip_n_coins(number)
    print_results(results)
    go_again = raw_input("Would you like to go again? (yes/no)")
    if go_again.upper() == "NO":
        break
print ("The program has been closed")
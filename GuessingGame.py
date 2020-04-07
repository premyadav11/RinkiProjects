low = 1
high = int(input("Enter a range:  "))

print("Please guess the  number between {} and {}".format(low, high))
input("Please ENTER to start")

guesses = 1
while low != high:

    guess = low + (high - low) // 2
    high_or_low = input("My guess is {}. Should i guess lower or higher?"
                        "Enter H or L or C if my guess was correct"
                        .format(guess)).casefold()

    if high_or_low == "h":
        low = guess + 1
    elif high_or_low == "l":
        high = guess - 1
    elif high_or_low == "c":
        print("I guessed in {} guesses!".format(guesses))
        break
    else:
        print("Please enter H ,L or C")

    guesses = guesses + 1
else:
    print("You thought of the number : {}".format(low))
    print("I guessed in {} guesses!".format(guesses))

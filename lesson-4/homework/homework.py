# 1. Return uncommon elements of lists

def uncommon_elements(list1, list2):
    from collections import Counter
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for k in (c1 - c2).elements():
        result.append(k)
    for k in (c2 - c1).elements():
        result.append(k)
    
    return result

# Test examples
print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]



# 2. Print the square of each number which is less than n

def print_squares(n):
    for i in range(1, n):
        print(i * i)

# Example
print_squares(5)



# 3. Add underscore after every third character unless conditions apply

def add_underscores(txt):
    result = ""
    i = 0
    vowels = "aeiou"

    while i < len(txt):
        result += txt[i]
        if (i + 1) % 3 == 0:
            if txt[i] in vowels or (i+1 < len(txt) and txt[i+1] == '_'):
                result += txt[i+1] if i+1 < len(txt) else ''
                i += 1
            result += "_"
        i += 1
    
    return result.rstrip('_')

# Test cases
print(add_underscores("hello"))            # hel_lo
print(add_underscores("assalom"))          # ass_alom
print(add_underscores("abcabcdabcdeabcdefabcdefg"))  # abc_abcd_abcdeab_cdef_abcdefg



# 4. Number Guessing Game

import random

def guessing_game():
    while True:
        number = random.randint(1, 100)
        attempts = 10
        while attempts > 0:
            guess = int(input("Guess the number (1-100): "))
            if guess == number:
                print("You guessed it right!")
                return
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")
            attempts -= 1
        
        print("You lost. Want to play again?")
        again = input("Type Y, YES, y, yes, ok to play again: ")
        if again.lower() not in ['y', 'yes', 'ok']:
            break



# 5. Password Checker

def check_password():
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password is too short.")
    elif not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")



# 6. Prime Numbers between 1 and 100

def print_primes():
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

print_primes()



# Bonus: Rock, Paper, Scissors Game

import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    comp_score = 0

    while player_score < 5 and comp_score < 5:
        comp = random.choice(choices)
        player = input("Enter rock, paper, or scissors: ").lower()
        print("Computer chose:", comp)

        if player == comp:
            print("It's a tie.")
        elif (player == "rock" and comp == "scissors") or \
             (player == "scissors" and comp == "paper") or \
             (player == "paper" and comp == "rock"):
            player_score += 1
            print("You win this round!")
        else:
            comp_score += 1
            print("Computer wins this round!")

        print(f"Score -> You: {player_score} | Computer: {comp_score}")

    print("Game Over!")
    if player_score == 5:
        print("🎉 You won the match!")
    else:
        print("💻 Computer won the match.")

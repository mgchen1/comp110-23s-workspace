"""EX02 - One Shot Wordle"""
__author__ = "730473986"

SECRET: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji_result: str = ""
index_count: int = 0
guess: str = input("What is your 6-letter guess? ")

while len(guess) != len(SECRET):
    guess = input(f"That was not {len(SECRET)} letters! Try again: ")

while index_count < len(SECRET): 
    if guess[index_count] == SECRET[index_count]:
        emoji_result += GREEN_BOX 
    else: 
        string_has_character: bool = False
        new_string: int = 0
        while new_string < len(SECRET) and string_has_character is False: 
            if SECRET[new_string] == guess[index_count]:
                string_has_character = True 
                emoji_result += YELLOW_BOX
            else: 
                new_string += 1 

        if string_has_character is False: 
            emoji_result += WHITE_BOX
    index_count += 1 
print(emoji_result)

if guess == SECRET: 
    print("Woo! You got it!")
else: 
    guess = str(input("Not quite. Play again soon!"))
    exit()





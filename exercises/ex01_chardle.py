"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730473986"

index_count: int = 0 
chardleword: str = input("Enter a 5-character word: ")
if (len(chardleword) != 5):
    print("Error: Word must contain 5 characters")
    exit()
chardle_character: str = input("Enter a single character: ")
if (len(chardle_character) != 1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + chardle_character + " in hello" )
if(chardle_character == chardleword[0]):
    print(chardle_character + " found at index 0")
    index_count = index_count + 1
if(chardle_character == chardleword[1]):
    print(chardle_character + " found at index 1")
    index_count = index_count + 1
if(chardle_character == chardleword[2]):
    print(chardle_character + " found at index 2")
    index_count = index_count + 1
if(chardle_character == chardleword[3]):
    print(chardle_character + " found at index 3")
    index_count = index_count + 1
if(chardle_character == chardleword[4]):
    print(chardle_character + " found at index 4")
    index_count = index_count + 1
if(index_count == 0): 
    print("No instances of " + str(chardle_character) + " found in " + str(chardleword))
else:
    if(index_count == 1): 
        print("1 instance of " + chardle_character + " found in " + chardleword)
    else:
        print (str(index_count) + " instances of " + str(chardle_character) + " found in " + str(chardleword))

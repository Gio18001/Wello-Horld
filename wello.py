#Dataset to extract from
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Phrase to build
phrase = "Hello World"

#Storage Variable
prntPhrase = ""

#Finds the next letter from the dataset and returns it
def find(i):
    x = 0
    prntPhrase = ""

    #Searches through the dataset until it finds the letter
    while i != alphabet[x]:
        #If the letter is not found, gives an error code to be used for debugging
        if x >= 52:
            print("Error 001: Letter Not Found")
            break
        else:
            x += 1
    
    #If the data is found, it returns it
    if i == alphabet[x]:
        return alphabet[x]

#Displays the collected data in the terminal
def prnt():
    #Iterates through the collected data and sends it to the terminal
    for letter in prntPhrase:
        print(letter, end="")
    print()

#Sends individual letters to the find function for data collection
for letter in phrase:
    prntPhrase = prntPhrase + find(letter)

#Calls the prnt function to display the data
prnt()
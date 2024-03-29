#TODO: Create a letter using starting_letter.txt 
names = []
with open("./Input/Names/invited_names.txt") as f:
    for line in f:
        names.append(line.strip())
    print(names)

with open("./Input/Letters/starting_letter.txt") as f:
    letter=f.read()
    print(letter)

for name in names:
    personalized_letter=letter.replace("[name],",f"{name},")
    with open(f"./Output/ReadyToSend/Ready_to_send_{name}","w") as f:
        f.write(personalized_letter)















#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
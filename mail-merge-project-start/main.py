#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os
with open('Input/Letters/starting_letter.txt', 'r+') as file1, open('Input/Names/invited_names.txt', 'r+') as file2:
    data1 = file1.readlines()
    data2 = file2.readlines()
    first_line_letter = data1[0]
    # for name in data2:
    #     name = name.rstrip()
    #     print(name)
    save_path = 'Output/ReadyToSend/'
    for name in data2:
        name = name.rstrip()
        with open(os.path.join(save_path, "letter_for_"+name+".txt"), 'w') as text:
            text.write(first_line_letter.replace('[name]', name))
            for i in range(1, len(data1)):
                text.write(data1[i])
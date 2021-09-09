# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
for name in range(len(names_list)):
    current_name = names_list[name].strip("\n")
    with open(f"Output/ReadyToSend/letter_for_{current_name}", "w") as file:
        letter = open("Input/Letters/starting_letter.txt")
        letter_content = letter.read().replace("[name]", current_name)
        file.write(letter_content)




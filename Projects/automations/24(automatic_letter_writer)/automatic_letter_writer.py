# Replaces the [name] placeholder in starting_letter.txt with the actual name for each name in invited_names.txt
# Creates a letter txt file to each person in the folder "ReadyToSend".

file = open('Input/Letters/starting_letter.txt')
starting_letter = file.read()

file2 = open('Input/Names/invited_names.txt')
names = file2.readlines()

for name in names:
    stripped_name = name.strip("\n")
    completed_letter = starting_letter.replace('[name]', stripped_name)
    with open(f'Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as file:
        file.write(completed_letter)

file.close()
file2.close()



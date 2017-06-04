import random

# Ask user for a question
question = input("Ask the Magic 8-Ball a question:\n")

# display one random 'in progess' message of several while ball is 'thinking'
pondering_dict = { '.\n. .\n. . .\nReading the runes\n. . .\n. .\n.': 'ponder_message_1' ,
                   'Hmm...\nAn interesting quesiton...': 'ponder_message_2',
                   'Well now... Let me think...': 'ponder_message_3',
                   'Patience. I must consult the spirits...': 'ponder_message_4' }
print(random.choice(list(pondering_dict)) + '\n')

# randomly select one of 20 responses

# allow user to ask another question, or, quit

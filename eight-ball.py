import random
import time

pondering_dict = { '.\n. .\n. . .\nReading the runes\n. . .\n. .\n.': 'ponder_message_1' ,
                   'Hmm...\nAn interesting quesiton...': 'ponder_message_2',
                   'Well now... Let me think...': 'ponder_message_3',
                   'Patience. I must consult the spirits...': 'ponder_message_4'
                   }

answer_dict = { 'It is certain.': 'answer_message_1',
                'It is decidedly so.': 'answer_message_2',
                'Without a doubt.': 'answer_message_3',
                'Yes, definitely.': 'answer_message_4',
                'You may rely on it.': 'answer_message_5',
                'As I see it, yes.': 'answer_message_6',
                'Most likely.': 'answer_message_7',
                'Outlook good.': 'answer_message_8',
                'Yes.': 'answer_message_9',
                'Signs point to yes.': 'answer_message_10',
                'Reply hazy, try again.': 'answer_message_11',
                'Ask again later.': 'answer_message_12',
                'Better not tell you now.': 'answer_message_13',
                'Cannot predict now.': 'answer_message_14',
                'Concentrate and ask again.': 'answer_message_15',
                'Don\'t count on it.': 'answer_message_16',
                'My reply is no.': 'answer_message_17',
                'My sources say no.': 'answer_message_18',
                'Outlook not so good.': 'answer_message_19',
                'Very doubtful.': 'answer_message_20'
}

def query_question():
  question = input("\nAsk the Magic 8-Ball a question:\n")
  time.sleep(2)
  return

def ponder_response():
  ponder_response = print('\n' + random.choice(list(pondering_dict)) + '\n')
  time.sleep(3)
  return

def answer_response():
  received_response = print("I've divined the answer to your question:")
  time.sleep(1)
  answer_response = print(random.choice(list(answer_dict)) + '\n')
  return

another_question = 'yes'

while another_question == 'yes':
    query_question()
    ponder_response()
    answer_response()
    another_question = input("Would you like to ask another question? If so, type yes.\n")

def magic(question):
	return f'The answer to your question is - {i}'
import random	
answer=["yes","no","sure","don't ask me that","it's your destiny","never don't ask me that again","do it","don't do it"]
random.shuffle(answer)
for i in answer:
	print(magic(question=input("Please ask a question - " )))
	break

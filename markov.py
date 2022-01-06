import re
from collections import defaultdict
import random

class Markov():
	def __init__(self, file_path=None):
		self.file_path = file_path
		self.text = self.remove_punctuation(self.get_data())
		self.model = self.model()

	def get_data(self):
		lines = open(self.file_path,'r').readlines()
		text = []
		for line in lines:
			text.append(line)
		return ' '.join(text)
	
	def remove_punctuation(self, text):
		res = re.sub(r'[^\w\s]', '', text)
		return res
	
	def model(self):
		markov_dict = defaultdict(list)

		text = self.text.split()
		for word, next_word in zip(text[0:-1], text[1:]):
			markov_dict[word].append(next_word)

		return markov_dict

	def predict(self, first_word, number_of_words):
		pred = first_word
		for i in range(number_of_words):
			if first_word in self.model:
				next_word = random.choice(self.model[first_word])
				pred += ' ' + next_word
				first_word = next_word
		return pred
		

if __name__ == '__main__':
	mc = Markov('data/t8.shakespeare.txt')
	print(mc.predict(first_word = 'shall', number_of_words = 10))

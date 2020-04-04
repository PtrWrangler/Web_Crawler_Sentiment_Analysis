#!/usr/bin/python

from afinn import Afinn
import nltk.data

def score(data):
	data = unicode(data, 'utf-8')
	ans = 0
	len = 0

	afinn = Afinn()
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	for p in (tokenizer.tokenize(data)):
		ans += afinn.score(p)
		len += 1
	return ans/len

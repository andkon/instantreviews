import spacy
import random

from spunkbot import diagnose
adj_list = ["love", "hate", "kinda like", "really like", "really don't like", "sorta like", "am indifferent to"]
en_nlp = spacy.load('en')

def review(tweet):
	doc = en_nlp(tweet)
	# diagnose(doc)
	for chunk in doc.noun_chunks:
		t = chunk.root
		if (t.pos_ == "NOUN" or t.pos_ == "PROPN") and (t.dep_ == "pobj" or t.dep_ == "dobj"):
			review_obj = chunk
			# now to make the review
			review = reviewer(chunk)
			return review
			break

def reviewer(span):
	""" Takes a noun chunk span, then makes a random review around it. """
	review_obj_string = span.text_with_ws
	adj = random.choice(adj_list)
	return "I %s %s." % (adj, review_obj_string)


def main():

	tweet = unicode(raw_input("what's up yo?\n"))
	print review(tweet)
	main()

if __name__ == '__main__':
	main()
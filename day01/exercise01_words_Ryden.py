"""return true if there is no e in 'word', else false"""
def has_no_e(word):
	return 'e' not in word


"""return true if there is e in 'word', else false"""
def has_e(word):
	return not has_no_e(word)


"""return true if word1 contains only letters from word2, else false"""
def uses_only(word1, word2):
	return not False in [i in word2 for i in [j for j in word1]]


"""return true if word1 uses all the letters in word2, else false"""
def uses_all(word1, word2):
	return not False in [i in word1 for i in [j for j in word2]]


"""true/false is the word in alphabetical order?"""
def is_abecedarian(word):
	original = [i for i in word]
	return sorted(original) == original

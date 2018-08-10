import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
	return txt.upper()



## reverse all characters in string
def reverse(txt):
	return txt[::-1]


## reverse word order in string
def reversewords(txt):
	return txt.split()[::-1]


## reverses letters in each word
def reversewordletters(txt):
	return [reverse(i) for i in txt.split()]
		
## change text to piglatin.. google it! 
def piglatin(txt):
	try:
		vowels = ['a', 'e', 'i', 'o', 'u']
		first_vowel = [i in vowels for i in txt].index(True)
	except ValueError:
		first_vowel = [i == 'y' for i in txt].index(True)
	ordering = range(first_vowel, len(txt))
	ordering.extend(range(0, first_vowel))
	result = map(txt.__getitem__, ordering)
	result.extend('ay')
	return result





## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]


		
			
			
			
			
			
			



def main():
	word = input("Enter a word:")
	print(ommit_vowels(word))
	
	
def ommit_vowels(phrase):
	exclude = ["a", "e", "i", "o", "u"]
	new = ""
	for letter in phrase:
		if letter.lower() in exclude:
			continue
		new += letter
	
	return new
	
main()
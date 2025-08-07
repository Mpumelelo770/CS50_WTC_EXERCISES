def main():
	word = input("Input something in camel case:")
	print(camel_to_snake(word))


def camel_to_snake(phrase):
	
	new = ""
	for letter in phrase:
		if letter.isupper():
			new += "_"
			new += letter.lower()
			continue
		new += letter
		
	return new
	
main()
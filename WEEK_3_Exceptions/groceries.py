

def grocery():
	dictionary = {}
	while True:
		try:
			item = input().lower()
			if item not in dictionary:
				dictionary[item] = 1
			elif item in dictionary:
				dictionary[item] += 1
					
				
		except EOFError:
			return dictionary
			
list = grocery()
sorted_dict = dict(sorted(list.items()))
for i in sorted_dict:
	print(list[i],i.upper())

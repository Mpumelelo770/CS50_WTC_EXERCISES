


def prices():
	total = 0
	dictionary = {
	"Baja Taco": 4.25,
	"Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
	
	
	while True:
		
		try:
			item = input("Item:").title()
			
			if item in dictionary:
				total += dictionary[item]
				print(f"Total: ${total:.2f}")
				
			price = dictionary[item] #can raise key error
			
		except EOFError:
			return f"Total:${total:.2f}"			
		except:
			pass
	
			
		
print(prices())
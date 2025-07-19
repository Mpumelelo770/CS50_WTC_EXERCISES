
def main():
	
	total = 0
	due = 50
	
	while True:
		insert = int(input("Insert Coin:"))
		
		if insert == 25 or insert == 10 or insert == 5:
			total += insert
		if total >= 50:
				print("Change Owed:",total - due)
				break
			
		print("Amount Due:",due - total)
		
main()
		
		

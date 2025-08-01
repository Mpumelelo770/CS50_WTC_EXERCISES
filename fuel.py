	
	
def petrol():
	
	while True:
		fraction = input("Please enter a fraction:").strip()
		try:
			separated = fraction.split("/")
			num = int(separated[0])
			den = int(separated[1])
			gauge = num / den
			percent = round(gauge*100)
			
			if num > den:
				raise Exception()
			elif num < 0 or den < 0:
				raise Exception()
				
				
			if percent <= 1:
				return "E"
			elif percent >= 99:
				return "F"
			else:
				return f"{percent}%"
			
			
		except ValueError:
				print("Please enter a valid value, as an integier")
		except ZeroDivisionError:
				print("Cannot divide by zero")
		except Exception:
				print("Fraction cannot be negative/nunerator must be less than denominator")
				
				
x = petrol()	
print(x)		
	
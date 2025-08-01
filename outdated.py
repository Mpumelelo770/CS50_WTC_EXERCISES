


def date():
	months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
	result = ""
	while True:
		n = input("Date: ")
		try:
			if n[0].isdigit():
				list = n.split("/")
				new_list = [int(i) for i in list]
				
				result += str(list[2])
				result += "-"
				result += str(f"{new_list[0]:02}")
				result += "-"
				result += str(f"{new_list[1]:02}")
				return result
			else:
				split_list = n.split()
				split_list[1] = split_list[1][0]
				result += split_list[2]
				result += "-"
				result += str(f"{months.index(split_list[0]) + 1:02}")
				result += "-"
				result += str(f"{int(split_list[1]):02}")
				return result
				
		except:
			print("Invalid input")
			

	
			

print(date())



		
		
		
	
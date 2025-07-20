
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
	nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	count = 0
	if len(s) > 6 or len(s) < 2: #checks for length specifications
		return False
	else:
		for letter in s:
			if letter.isalpha(): # checks current iteration is a letter
				count += 1
			else:
				break # leaves as soon as it finds a number and record the count
		if count == 6:  # This means the plate consist entirely of letters
			return True
			
		left = s[count:]  # the rest of the string after a number is detected.
		
		if left[0] == 0: # checks if the firsf number is not zero
			return False
		elif count < 2:  #checks if the first 2 are letters
			return False
		else:
			for i in left:
				if i not in nums: # checks if the remaining string contains all numbers
					return False
					
	return True
		





main()
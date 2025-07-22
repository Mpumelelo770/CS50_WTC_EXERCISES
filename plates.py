


def main():
    plate = input("plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
	nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	count = 0
	if len(s) > 6 or len(s) < 2: 
		return False
	else:
		for letter in s:
			if letter.isalpha():
				count += 1
			else:
				break 
				
		if len(s) == count:
			return True
			
			
		left = s[count:]  
		if left[0] == 0: 
			return False
		elif count < 2: 
			return False
		else:
			for i in left:
				if i not in nums: 
					return False
					
	return True
		





main()
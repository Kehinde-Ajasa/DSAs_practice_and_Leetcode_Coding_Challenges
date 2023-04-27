"""This program solves a challenge that keeps adding a nth digit number until its result
is another nth digit number long"""

try:
	output = ""

	def get_input():
		"""Function to accept all user's input"""
		global output
		main_number = int(input("Please enter the number you would like to add: "))
		output = int(input("How many digits do you want your result to be: "))
		return main_number


	try:
		def add_digits_to_target(user_value):
			summation = 0
			for numbers in str(user_value):
				summation += int(numbers)
			if len(str(summation)) != output:
				return add_digits_to_target(summation)
			else:
				return summation


		print(add_digits_to_target(get_input()))
	except RecursionError:
		print("Sorry, error while preparing result,\nEnsure that the length of the result \
is less than or equal to the length of the input")

except ValueError:
	print("Dear user, we encountered minor issue while preparing your result\
please check your input and ensure they are all integers")

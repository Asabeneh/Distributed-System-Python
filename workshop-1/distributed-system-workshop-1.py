import re #import Regular expression
#Workshop 1 exercises: Getting to know Python - part I
#link for the questions:https://www.cs.helsinki.fi/u/owaltari/distsys/ws1/dist_sys_ws1.html

#1.Looping and printing
#Write code that prints every integer between 0 and 20
def wrapperFunction():# This function wrap up all the functions
	print("Workshop 1 exercises: Getting to know Python - part I")
	print("Hello, Helsinki University")
	for num in range(21):
		print(num)
		
	#2.Defining functions
	#Modify the previous code and define the code snippet as a function. 
	#Also, put the numbers into an array instead of printing. 
	#The function should take no input parameters and return an array.
	#Call the function and print the output (i.e. print(my_function())) 
	
	def printZeroToTwenty():
		numbers = []
		for num in range(21):
			numbers.append(num)
		return numbers
	print(printZeroToTwenty())
	#3. Reverse and return

	#Define a function that takes an array as an input parameter.
	#Return a reverse array of the input array.
	#(You may also reverse the original array in-place.
	#Just make sure you know which way you're doing it.) 
	def reverseArray(arr):
		newArray = []
		for i in range(len(arr)):
			newArray.append(arr[len(arr)-i-1])
			
		return newArray
	print(reverseArray([5,4,3,2,1]))

	#4.Writing to files
	#Define a function that:
	#Takes an array as an input parameter
	#Opens a file
	#Writes each value from the input array to the file
	#Closes the file

	def writeArrayValueIntoFile(arr):
		f = open('example','w')
		for i in range(len(arr)):
			f.write(str(arr[i]))
		f.close()	
	writeArrayValueIntoFile([10,20,30,40,50])

	#5.Define a function that:
	#Opens a file. Give the filename as a parameter
	#Reads the file line by line and parse for an integer on each line (Beware of newline characters in line-by-line reading!)
	#Sum all integers you read from the file
	#Return the 

	def openFileAndReadLineByLine():
		sum = 0
		lines = 0 
		fname = input('enter file name:')
		try:
			fopen = open(fname)
		except:
			print('file was not found!')
			exit()
			
		for line in fopen:
			numbers = re.findall(r'\d+', line)
			print(numbers)
			lines+=1
		for num in numbers:
			print(int(num))
			sum+=int(num)
		return "The sum is " + str(sum)
	print(openFileAndReadLineByLine())
	#6.Write a main function (wrapping everything up)
	#Define a main function and perform the following using the functions you have defined:
	#Create an array with numbers from 0 to 20i
	#Reverse the array
	#Write the array into a file
	#Read the file and calculate the sum
wrapperFunction()


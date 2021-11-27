# John is finding a number from a to b, knowing that from a to b, the numbers are sorted ascendingly
# a) John propose using a linear search to find that number
# - Implement/Define that function
# b) John also want to see the binary search to find that number
# - Implement/Define that function
# c) Which one is better ? Why ?

# If found that number return f"Found the number at index {mid}"
# else return "Number not in the list"

a = 1
b = 50
listOfNumbers = list(range(a,b))

# Code for question a
def linearSearch(list,item):
  # Your code
  # Use for loop instead of while loop
  # Iterate through each index to find that number
 
# Code for question b
def binarySearch(list,item):
  #Your code
  
# Hint for question C
# Try to print the running time of each function 
# Or try to print number of guessing the number

# Testcase 1
linearSearch(listOfNumbers, 100)
binarySearch(listOfNumbers, 100)
linearSearch(listOfNumbers, 12)
binarySearch(listOfNumbers, 12)


# Testcase 2
linerSearch(listOfNumbers, 0)
binarySearch(listOfNumbers, 0)
linerSearch(listOfNumbers, 34)
binarySearch(listOfNumbers, 34)

# Testcase 3 ???

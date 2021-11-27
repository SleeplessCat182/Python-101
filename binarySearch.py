listOfNumber = list(range(1,101))

def binary_search(list,item):
    low = 0
    high = len(list)-1
    while(low<=high):
        mid = round((low+high)/2)
        guess = list[mid]
        if(guess == item):
            return f"Found the number at index {mid}"
        if guess > item:
            high = mid-1;
        else:
            low = mid+1;
    return "Number not in the list"

print(binary_search(listOfNumber,9))


# John is finding a number from a to b, knowing that from a to b, the numbers are sorted ascendingly
# a) John propose using a linear search to find that number
# - Implement/Define that function
# b) John also want to see the binary search to find that number
# - Implement/Define that function
# c) Which one is better ? Why ?
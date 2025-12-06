a=[3,2,6,8,5]
a.sort()
print("Smallest element is:",a[0])
'''
Output:
Smallest element is:2
'''


numbers = [5, 2, 8, 1, 7]
if not numbers:
    smallest_number = None # Handle empty list
else:
    smallest_number = numbers[0]
    for num in numbers:
        if num < smallest_number:
            smallest_number = num
print(smallest_number) # Output: 1

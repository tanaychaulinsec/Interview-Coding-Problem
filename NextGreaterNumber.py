def findNext(number, n):
    # Start from the right most digit and find the first
    # digit that is smaller than the digit next to it
    for i in range(n - 1, -1, -1):
        if number[i] > number[i - 1]:
            break
    if i == 0:
        print("Next number not possible")
        return

    x = number[i - 1]
    smallest = i
    for j in range(i + 1, n):
        if number[j] > x and number[j] < number[smallest]:
            smallest = j
    number[smallest], number[i - 1] = number[i - 1], number[smallest]

    # X is the final number, in integer datatype
    x = 0
    # Converting list upto i-1 into number
    for j in range(i):
        x = x * 10 + number[j]

    number = sorted(number[i:])
    # converting the remaining sorted digits into number
    for j in range(n - i):
        x = x * 10 + number[j]

    print("Next number with set of digits is", x)


# Driver Program to test above function
digits =[54321]
# converting into integer array,
# number becomes [5,3,4,9,7,6]
number =list(map(int,str(digits[0])))
n=len(number)
findNext(number, n)
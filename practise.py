# def findNext(number, n):
#     # Start from the right most digit and find the first
#     # digit that is smaller than the digit next to it
#     for i in range(n - 1, 0, -1):
#         if number[i] > number[i - 1]:
#             break
#
#     if i == 0:
#         print("Next number not possible")
#         return
#
#     # Find the smallest digit on the right side of
#     # (i-1)'th digit that is greater than number[i-1]
#     x = number[i - 1]
#     smallest = i
#     for j in range(i + 1, n):
#         if number[j] > x and number[j] < number[smallest]:
#             smallest = j
#
#             # Swapping the above found smallest digit with (i-1)'th
#     number[smallest], number[i - 1] = number[i - 1], number[smallest]
#
#     # X is the final number, in integer datatype
#     x = 0
#     # Converting list upto i-1 into number
#     for j in range(i):
#         x = x * 10 + number[j]
#
#         # Sort the digits after i-1 in ascending order
#     number = sorted(number[i:])
#     # converting the remaining sorted digits into number
#     for j in range(n - i):
#         x = x * 10 + number[j]
#     print("Next number with set of digits is", x)
#
# # Driver Program to test above function
# input =[218765]
# output =list(map(int, str(input[0])))
# findNext(output, len(output))


class newNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
# def leftView(root):
#     if root is None:
#         return
    # else:
#
# def inorder(root):
#     if root is None :
#         return 0
#     else:
#
#         print(root.data)
#         inorder(root.left)class newNode:
#     def __init__(self,val):
#         self.data=val
#         self.left=None
#         self.right=None
# # def leftView(root):
# #     if root is None:
# #         return
#     # else:
#
# def inorder(root):
#     if root is None :
#         return 0
#     else:
#
#         print(root.data)
#         inorder(root.left)

# def preorder(root):
#
# def postorder(root):



# if __name__ == '__main__':
#     root = newNode(1)
#     root.left = newNode(2)
#     root.right = newNode(3)
#     root.left.left = newNode(4)
#     root.left.right = newNode(5)
#
#     #print(leftView(root))
#     (inorder(root))
    # (preorder(root))
    #(postorder(root))
# def myfunc(n):
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
#
# print(mydoubler(11))
# print(mytripler(11))
def pClosest(points, K):
    points.sort(key=lambda K: K[0] ** 2 + K[1] ** 2)

    return points[:K]


# Driver program
points = [[3, 3], [5, -1], [-2, 4]]

K = 2

print(pClosest(points, K))
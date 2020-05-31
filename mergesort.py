# def mergeSort(nums, l, r):
#     if l > r:
#         return
#     if l == r:
#         return [nums[l]]
#     mid = l + (r-l)//2
#     left = mergeSort(nums, l, mid)
#     right =mergeSort(nums, mid+1, r)
#     return merge(left, right)
#
# def merge(l1, l2):
#     res, i, j = [], 0, 0
#     while i < len(l1) and j < len(l2):
#         if not compare(l1[i], l2[j]):
#             res.append(l2[j])
#             j += 1
#         else:
#             res.append(l1[i])
#             i += 1
#     res.extend(l1[i:] or l2[j:])
#     return res
#
# def compare(n1, n2):
#     return str(n1) + str(n2) > str(n2) + str(n1)
def mergeSort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i+=1
            else:
                nlist[k]=righthalf[j]
                j+=1
            k+=1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i+=1
            k+=1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j+=1
            k+=1
    return ("merging",nlist)

nums=[6,5,8,7,3,9,2,1]
#print(mergeSort(nums,1,len(nums)-1))
print(mergeSort(nums))

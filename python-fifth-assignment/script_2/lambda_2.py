nums1 = [1, 4, 5, 6, 5] 
nums2 = [3, 5, 7, 2, 5] 


result = map(lambda x, y: x + y, nums1, nums2)
print("\nResult: after adding two list")
print(list(result))
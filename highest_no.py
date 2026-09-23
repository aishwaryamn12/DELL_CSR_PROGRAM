nums=[12,45,2,45,67,23,67,8]
n=len(nums)
highest=nums[0]
second=nums[0]
count=0
for num in nums:
        if num>highest:
            second=highest
            highest=num
        elif num>second and num!=highest:
            second=num
print("highest:",highest)
print("second highest:",second)
    

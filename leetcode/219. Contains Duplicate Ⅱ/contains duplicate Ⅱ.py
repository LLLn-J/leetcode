
nums=[1,2,3,1,2,3]
k=2

def solution(nums,k):
    d = set()
    for i in range(len(nums)):
        if nums[i] in d:
            return True
        d.add(nums[i])
        if len(d) > k:
            d.remove(nums[i - k])
    return False

ans=solution(nums,k)
print(ans)
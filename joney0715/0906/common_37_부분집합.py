nums = [1,2,3]

subsets = []

def dfs(n, subset):
    subsets.append(subset)

    for i in range(n, len(nums)):
        dfs(i+1, subset+[nums[i]])

dfs(0, [])

print(subsets)
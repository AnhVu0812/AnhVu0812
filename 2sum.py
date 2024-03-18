#Brute force
def twoSum(nums:list[int], target: int) ->list[int]:
    target = int(input("enter target:"))
    nums = []
    while True:
        num = (int(input("enter num:")))
        nums.append(num)

        choice = input("another num ? (y/n):")
        if choice.casefold() == 'y':
            continue
        elif choice.casefold() == 'n':
            break

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
            
print(twoSum(nums=[], target=()))
class Solution:
    def search(self , nums , target ):
        # write code here
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

if __name__ == '__main__':
    s = Solution()
    a = [1,2,3,4,5]
    b = 4
    print(s.search(a,b))
#ongoing
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        # 배열 길이가 1이거나
        # 배열요소의 합이 m과 같거나 큰 배열

        # 무조건 나눌때는 둘다 good이여야지 나눌 수 있음

        # n개로 나눠지면 true, 아니면 false

        # 나누면 각각은 합이 m>=이거나, 요소가 하나이거나 

        # 투포인터에 백트래킹 


        # tmpL = nums[:l+1]
        # tmpLR = nums[l+1:]
        # print(tmpL)
        # print(tmpLR)


        # tmpR = nums[r-l:]
        # tmpRR = nums[:r-l]
        # print(tmpR)
        # print(tmpRR)

        l, r = -1, len(nums)

        while(l<=r):
            l+=1
            r-=1

            tmpL = nums[:l+1]
            tmpLR = nums[l+1:]
            print(tmpL)
            print(tmpLR)

            tmpR = nums[r-l:]
            tmpRR = nums[:r-l]
            print(tmpR)
            print(tmpRR)
            
            if (len(tmpL)==1 or sum(tmpL))>=m) and (len(tmpLR)==1 or sum(tmpLR)>=m)):
                backtrack(l, r)

            else if (len(tmpR)==1 or sum(tmpR))>=m) and (len(tmpRR)==1 or sum(tmpRR)>=m)):
                backtrack(l, r)
        

        #while l<r:




    # def backtrac(int a, int b):

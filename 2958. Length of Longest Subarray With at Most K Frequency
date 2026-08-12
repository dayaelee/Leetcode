import math
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        # -1 0 1 2 3 4 5 6 7
        #    1 2 3 1 2 3 1 2 
        #  r l
        # r: 오른쪽으로 갈 수 있을때까지 계속 가게 하는거 (k 조건이 허용하는데까지)
        # l: 그냥 한번씩만 옆으로 갈꺼야.
        
        N = len(nums)
        l, r = 0, 0
        freq = defaultdict(int)
        
        answer = 0
        
        # 여기 l은 일단 이해 못해도 돼.
        # 1 2 3 1 2 3 1 2
        for l in range(N):
            # r은 상남자야 ! 갈 수 있을때까지 갔어
            while r < N and freq[nums[r]] + 1 <= k:
                freq[nums[r]] += 1
                r += 1
            
            # l ~ r - 1 구간이 조건에 맞는 구간 (k 이하)
            answer = max(answer, r - l)
            
            # l은 어떻게 할껀데?
            freq[nums[l]]-=1
            
        return answer
        

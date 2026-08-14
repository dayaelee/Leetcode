class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        l, r = 0, -1

        tmp = defaultdict(int)
        answer = 0
        cnt = 0
        while l<len(s):
            # print()
            while r+1<len(s):
                items = s[r+1]
                if tmp[items]+1<=2:
                    # print('where are you: ', r+1)
                    tmp[items]+=1
                    cnt+=1
                    r+=1
                else:
                    break
                
            # print('cnt: ', cnt)
            answer=max(answer, cnt)
            cnt-=1
            item = s[l]
            tmp[item]-=1
            l+=1
        # print(answer)
        return answer
        

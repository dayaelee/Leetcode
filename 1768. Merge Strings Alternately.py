class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        cnt1 = 0
        cnt2 = 0
        answer =''
        flag1=0
        flag2=0

        while 1:
            if flag1==1 and flag2==1:
                break

            if cnt1<len(word1):
                answer+=word1[cnt1]
                cnt1+=1
            else:
                flag1=1
            if cnt2<len(word2):
                answer+=word2[cnt2]
                cnt2+=1
            else:
                flag2=1
        
        return answer


        

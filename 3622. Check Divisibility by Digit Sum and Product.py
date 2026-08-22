class Solution:
    def checkDivisibility(self, n: int) -> bool:
        strN = str(n)
        summ = 0
        product = 1

        for ele in strN:
            summ+= int(ele)
            product *= int(ele)

        # print('summ: ', summ)
        # print('product: ', product)
        if n%(summ+product)==0:
            return True
        else:
            return False

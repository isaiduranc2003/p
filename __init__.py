
class CalcBasica:

    def resta(*nums):
        res = 0
        for valor in nums:
            res -=valor
        
        return res
    
    def suma(*nums):
        res = 0
        for valor in nums:
            res +=valor
        
        return res
    
    def multiplicacion(*nums):
        res = 0
        for valor in nums:
            res *=valor
        
        return res
    
    def div(n1,n2):
        res = n1/n2
        sobra = n1 % n2
        
        return res, sobra
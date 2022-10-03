n=str(input())
sum=0


for i in range(1,len(n)):
        res=int(int(n[i-1])**int(n[i]))
        sum=sum+res
        if i==len(n)-1:
            res=int(n[i])**0
            sum=sum+res
            
        
        
        
        '''if i == len(n)-1 :
            sum=sum+(int(n[i-1])**int(n[i]))
            
        else:
            sum=sum+(int(n[i])**int(n[i+1]))'''
       
print(sum)
    

n=int(input("Enter n value : "))
Arr=['0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(1,n+1):
    print(f"{Arr[i]} "*i)

#OUTPUT
#Enter n value : 5
#A 
#B B 
#C C C 
#D D D D 
#E E E E E 

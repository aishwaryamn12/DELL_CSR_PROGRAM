marks=int(input("enter marks:"))
if marks<40:
    print("fail")
else: 
    print("pass")  
if marks<=0 or marks>100:
    print("invalid")    
elif marks>=80:
    print("grade A")
elif marks>=70:
    print("Grade B")
elif marks>=60:
    print("grade C")
elif marks>=50:
    print("grade D")
else:
    print("grade F")

                

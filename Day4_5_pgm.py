scores=[75,63,89,60,50,40,30,20,45,89,34,23,45]
counta,countb,countc,countd,counte=0,0,0,0,0
for score in scores:
    if score<0 or score>100:
        print("invalid")
    elif score>=70:
        counta+=1
    elif score>=60:
        countb+=1
    elif score>=50:
        countc+=1
    elif score>=40:
        countd+=1
    elif score>=30:
        counte+=1
print("grade A:",counta)
print("grade b:",countb)
print("grade c:",countc)
print("grade d:",countd)
print("grade e:",counte)
    

        

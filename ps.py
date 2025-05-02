rows=5
count=97
for i in range(1,rows+1):
    string=""
    for j in range(1,i+1):
        if j==1 or i==j or i==rows:
            string+=chr(count)+" "
            count+=1
        else:
            count+=1
            string+=" "+" "
    print(string)

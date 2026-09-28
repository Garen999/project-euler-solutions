count = 1000

for i in range(count+1):
    i+=1
    for j in range(count+1):
        j+=1
        for k in range(count+1):
            k+=1
            if i + j + k == 1000 and i**2 + j**2 == k**2:
                print(i,j,k)
                result = i*j*k

print(result)
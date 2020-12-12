def isPrime(n):
 
    if (n <= 1):
        return False
 
    for i in range(2, n):
        if (n % i == 0):
            return False
 
    return True

counter = 1
i = 1

while counter <= 10001:
	i += 1
	if(isPrime(i)):
		counter += 1
	
print(i)
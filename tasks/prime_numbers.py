#How many prime numbers are wanted?
n = 14 #specify n

#task: write a program that prints the first n prime numbers
prime = []
for i in range(1, 10000000000000000000000): #comment: I could not find a solution to run from 1 to infinity
    for j in range (2, i):
        if i % j == 0:
            break
        else:
            prime.append(i)
            break
    if(len(prime) == n):
        break

print("The first", n, "prime numbers are:", prime)

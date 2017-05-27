import time


def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print 'not a prime'
                break
        else:
            print(num, 'is a prime number')
    else:
        print(num, 'is not a prime number')

start_time = time.time()
isPrime(10000000)
print("--- %s seconds ---" % (time.time() - start_time))

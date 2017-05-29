import time
import random


def bubble_sort(num_list):
    for n in range(len(num_list)-1,0,-1):
        for i in range(n):
            if num_list[i] > num_list[i+1]:
                temp = num_list[i]
                num_list[i] = num_list[i+1]
                num_list[i+1] = temp



num_list = [int(10000*random.random()) for i in xrange(10000)]
start_time = time.time()
bubble_sort(num_list)
print("--- %s seconds ---" % (time.time() - start_time))

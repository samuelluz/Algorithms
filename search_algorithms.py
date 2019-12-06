"""
Performance comparison between linear search, interactive binary search and recussive binary search.
"""
import time
import argparse
parser = argparse.ArgumentParser(description='Search for some integer between -1000 and 1000.')
parser.add_argument('num', type=int, help='an integer', default = 1)
args = parser.parse_args()

def linear_search(num, num_list):
    for position, x in enumerate(num_list):
        if x == num:
            return position, position
    return -1, position

def binary_search_recursive(target, num_list, low=None, high=None, attempts=0):
    if low==None:
        low=0
    if high==None:
        high=len(num_list)-1
    if high >= low:
        attempts=attempts+1
        mid = int(low + (high - low)/2)
        if target == num_list[mid]: 
            return mid, attempts
        elif target < num_list[mid]: 
            return binary_search_recursive(target, num_list, low, mid-1, attempts) 
        else: 
            return binary_search_recursive(target, num_list, mid+1, high, attempts) 
    else: 
        return -1, attempts

def binary_search_interative(target, num_list):
    low=0
    high=len(num_list)-1
    attempts = 0

    while high >= low:
        attempts+=1
        mid = int(low + (high - low)/2)
        if target == num_list[mid]: 
            return mid, attempts
        elif target < num_list[mid]: 
            high = mid-1
        else: 
            low = mid+1 
    return -1, attempts

def main():
    num = args.num
    num_list = range(-1000,1001)

    print("searching for {} with linear_search".format(num))
    start = time.time()
    position, attempts = linear_search(num, num_list)
    search_time = (time.time()-start)*1000000
    print("Number: {}, Position: {}, Attempts: {}, time: {:.2f} us!\n"\
            .format(num, position, attempts, search_time))

    print("searching for {} with binary_search_interative".format(num))
    start = time.time()
    position, attempts = binary_search_interative(num, num_list)
    search_time = (time.time()-start)*1000000
    print("Number: {}, Position: {}, Attempts: {}, time: {:.2f} us!\n"\
            .format(num, position, attempts, search_time))
    
    print("searching for {} with binary_search_recursive".format(num))
    start = time.time()
    position, attempts = binary_search_recursive(num, num_list)
    search_time = (time.time()-start)*1000000
    print("Number: {}, Position: {}, Attempts: {}, time: {:.2f} us!\n"\
            .format(num, position, attempts, search_time))


if __name__ == "__main__":
    main()

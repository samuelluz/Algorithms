import time
import argparse
parser = argparse.ArgumentParser(description='Search for some integer between 0 and 1000.')
parser.add_argument('num', type=int, help='an integer')
args = parser.parse_args()

def linear_search(num, min=0, max=1000):
    print("searching for {}".format(num))
    start = time.time()
    for x in range(min,max+1):
        if x == num:
            return x, (time.time()-start)*1000000
    return "anything", (time.time()-start)*1000000 

if __name__ == "__main__":
    print("I finded {} in {:.2f} us!".format(*linear_search(args.num)))

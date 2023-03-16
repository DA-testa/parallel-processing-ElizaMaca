# python3

import heapq

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    mytrea=[(0,j)for j in range(n)]
    heapq.heapify(mytrea)
    # create the output pairs
    for s, r in enumerate(data):
        termlaiks, source = heapq.heappop(mytrea)
        output.append(source, termlaiks)
        heapq.heappush(mytrea,(termlaiks+r, source))
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    #m=map(int,input().split())
    # first line - n and m
    n,m=map(int,input().split())
    # n - thread count 
    # m - job count
    # second line - data 
    data=list(map(int,input().split()))
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    # TODO: create the function
    result = parallel_processing(n,m,data)
    # TODO: print out the results, each pair in it's own line
    for source, seconds in result:
        print(source,seconds)
if __name__ == "__main__":
    main()

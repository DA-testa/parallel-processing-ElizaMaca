# python3  Elīza Mača RDCP0.grupa
import heapq

def parallel_processing(n, m, data):
    output = []
    #  write the function for simulating parallel tasks
    mytrea=[(0,j) for j in range(n)]
    heapq.heapify(mytrea)
    # create the output pairs
    for j, r in enumerate(data):
        izpildeslaiks, source = heapq.heappop(mytrea)
        output.append((source, izpildeslaiks))
        heapq.heappush(mytrea,(izpildeslaiks+r, source))
    return output

def main():
    # create input from keyboard
    # input consists of two lines
    # first line - n and m
    n,m=map(int,input().split())
    # n - thread count and m - job count
    # second line - data 
    data=list(map(int,input().split()))
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    # create the function
    result = parallel_processing(n,m,data)
    # print out the results, each pair in it's own line
    for source, seconds in result:
        print(source,seconds)
if __name__ == "__main__":
    main()

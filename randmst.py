
# libraries 
import matplotlib.pyplot as plt
import seaborn as sns
import time
import pandas as pd 
import random
import numpy as np 


''' Below you can find the Graph Generators '''

#Complete Graph Generator 
def complete_graph(n): 

    g = {i: [] for i in range(n)} #where every node has a list of it edges to other nodes where (a,b) means edge to a with weight b 
    #weights = np.random.uniform(0, 1, (n*(n-1) // 2))
    upper_bound = 9/n

    '''
    upper bound = x / 128 
    upper boound * 128 = x
     upper bound = 6.4/124 
     upper bound = 5.66/ 256
     upper bound = 6.1/512
     upper bound = 7.7 / 1024
     upper bound = 7.5/2048
     upper bound = 9.99 / 4096
     upper bound = 
    '''
    # for w in weight: 
    #     if w > upp
    #     u = random.randint(0, n - 1) #because this is inclusive
    #     v = random.randint(0, n - 1)

    for u in range(n): 
        for v in range(u + 1, n): 
            w = random.uniform(0, 1)
            if w < upper_bound: 
                g[u].append((v, w)) #we store this edge in both to optimize for this  
                g[v].append((u, w))

    return g 


#Hypercube Graph Generator 
def hypercube_graph(n):
   
    g = {i: [] for i in range(n)}

    #basically, you dont have to check every pair 
    # if vertex a with value a, (like v =1), has edges with a + 2^0, a + 2^1, a + 2^2 = a+1, a+2, a+4 
    #so just check if those values are less than n, and if so you have an edge. this saves a lot of time

    for u in range(n): 

        p = 0

        while u + 2**p < n: 
            
            v = u + 2**p
            w = random.uniform(0, 1)

            g[v].append((u, w))
            g[u].append((v, w))
            p += 1

    return g

#Unit Square Graph Generator 
def square_graph(n): 
    '''
    upper_bound = 18/ 128
    upper bound = 28/256
    upper bound = 38/512
    upper bound = 64/1024

    '''
    g = {}
    upper_bound = 18/ 128

    while n > 0:
        #generate the location of this vertex & add it to the graph g 
        x, y = random.uniform(0, 1), random.uniform(0,1)

        #the location will be the value of this node, so that its outgoing edges can be easily looked up later on 
        g[(x,y)] = []

        n -= 1

    #go through all of the pairs of verticies and add an edge whose weight is just the euclidean distance between them 
    #dude so you avoid redundant calculations, just only compute the edge if j is greater than I!!
    for i, u in enumerate(g): 
        for j, v in enumerate(g): 
            
            if j > i: 
                
                euc_dis = ( (u[0] - v[0])**2 + (u[1] - v[1])**2 )**(1/2)

                if euc_dis < upper_bound: 

                    g[u].append((v, euc_dis))
                    g[v].append((u, euc_dis))

    return g

#4 Dimensional Graph Generator
def teseract_graph(n): 
    g = {}
    upper_bound = 0.5
    while n > 0:
        #generate the location of this vertex & add it to the graph g 
        x, y, z, w = random.uniform(0, 1), random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)

        #the location will be the value of this node, so that its outgoing edges can be easily looked up later on 
        g[(x, y, z, w)] = []

        n -= 1

    #go through all of the pairs of verticies and add an edge whose weight is just the euclidean distance between them 
    #dude so you avoid redundant calculations, just only compute the edge if j is greater than I!!
    for i, u in enumerate(g): 
        for j, v in enumerate(g): 
            
            if j > i: 
                
                euc_dis = ( (u[0] - v[0])**2 + (u[1] - v[1])**2 + (u[2] - v[2])**2 + (u[3] - v[3])**2)**(1/2)
                if euc_dis < .5: 

                    g[u].append((v, euc_dis))
                    g[v].append((u, euc_dis))

    return g

#3 Dimensional Graph Generator
def cube_graph(n, upper_bound=None):
    #first we want to generate an array of n vertices with 3 coordinates, (x,y,z), each where x, y, z are random numbers between 0 and 1
    vertices = np.random.rand(n,3)


    upper_bound = 0.3

    '''
    based on experiments, we can see that we kind of have some sort of exponential decay
    as n increases, the max weight of an edge decreases exponentially

    38/128
    55/256


    '''
    #initialize graph as empty dictionary
    g = {i: [] for i in range(n)}

    #loop through all PAIRS of vertices
    for i in range(n):
        for j in range(i+1, n):
            #calculate Euclidean distance by first finding the differences in x, y, and z coordinates
            dx = vertices[i][0] - vertices[j][0]
            dy = vertices[i][1] - vertices[j][1]
            dz = vertices[i][2] - vertices[j][2]
            # Square root of sum of squared differences
            dist = (dx * dx + dy * dy + dz * dz) ** 0.5  
            
            #if the distance is less than the threshold, then we keep the edge and add to graph
            if upper_bound is None or dist < upper_bound:  
                g[i].append((j, dist))
                g[j].append((i, dist))
        
    return g

        

''' Min Heap Implementation '''
class minheap: 
    def __init__(self): 
        self.heap = []

    def pop(self): 
        #returns and removes the minimum value in the heap. This is deleteMin() in the lecture 6 notes 
        output = self.heap[0]
        
        #swap the end with the front
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop()

        #bubble down 
        i = 0
        heap_len = len(self.heap) 
        while i < len(self.heap): 

            left = (2 * i) + 1 
            right = (2 * i) + 2

            #okay just keep replacing the chosen child thats the easiest way 
            chosen_child = i
            if left < heap_len and self.heap[left][1] < self.heap[i][1]: 
                chosen_child = left 
            if right < heap_len and self.heap[right][1] < self.heap[chosen_child][1]: 
                chosen_child = right
            if chosen_child == i: 
                break
            
            #swap 
            tmp  = self.heap[chosen_child]
            self.heap[chosen_child] = self.heap[i]
            self.heap[i] = tmp
            i = chosen_child
            
        return output

    def push(self, val, dis) : #val will have the actual node value and the d[val]
        #adds a new value into the heap and maintains heap structure. This is Insert() in the lecture 6 notes 
        self.heap.append((val, dis))

        #bubble up
        i = len(self.heap) - 1
        while i > 0: 
            
            parent_i = (i - 1) // 2 #apparently theres an empirical way to find the parent node. 
            if self.heap[parent_i][1] > self.heap[i][1]: 
                tmp = self.heap[parent_i]
                self.heap[parent_i] = self.heap[i]
                self.heap[i] = tmp
                i = parent_i
            else: 
                break

''' Below you can find Prim's Minimum Subtree Algorithm'''

def prims_mst(g): 
    #initialize d data structure to keep track of the distances
    d = {v: float('inf') for v in g}

    #initialize source node
    start = next(iter(g))
    d[start] = 0

    #initialize heap 
    queue = minheap()
    queue.push(start,0)

    #initialize S to keep track of nodes that are in the MST, of course it starts with the first node
    S = set()

    #initialize the prev data structure that just keeps track of the vertex that came before the current one in our spanning tree
    prev = {v: None for v in g}

    #track mst weightr
    mst_weight = 0
    max_weight = 0 

    #While the queue is not empty
    while queue.heap:

        #pop the minimum vertex (highest priority vertex)
        u, weight = queue.pop()

        # if node is visited, then skip
        if u in S:
            continue 

        #add this vertex to S, set of visited nodes
        S.add(u)

        #update the mst weight
        mst_weight += weight
        max_weight = max(max_weight, weight)

        #for all of that vertex's edges whose destination vertices are not in S
        for v, w in g[u]:
            #if d[v] is greater than our newly calculated distance to v: 
            if v not in S and d[v] > w:
                #update d[v]
                d[v] = w
                #update prev[v]
                prev[v] = u
                #insert v into the queue
                queue.push(v, w)

    return mst_weight, max_weight


def avg_mst_weight(n, graph_type, trials = 5):
    total_weight = 0

    print(f"\nRunning {trials} trials for {graph_type} Graph with n={n}:")
    
    for i in range(trials):
        if graph_type == "complete":
            g = complete_graph(n)
        elif graph_type == "hypercube":
            g = hypercube_graph(n)
        else:
            raise ValueError("Invalid graph type")

        mst_weight = prims_mst(g)
        total_weight += mst_weight
        print(f"  Trial {i+1}: n={n}, MST Weight={mst_weight:.4f}")

    avg_weight = total_weight / trials
    print(f"  → Average MST Weight for n={n}: {avg_weight:.4f}\n")
    return avg_weight

if __name__ == "__main__":  
    


    #experiments
    n_values = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]

   
    for n in n_values: 
        # g = teseract_graph(n)
        g = cube_graph(n, None)
        
        mst_w, max_w = prims_mst(g)
        print(f"n: {n} ----MST weight:{mst_w}  Max_w: {max_w}")



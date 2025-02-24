
# libraries 
import matplotlib.pyplot as plt
import seaborn as sns
import time
import pandas as pd 
import random


''' Below you can find the Graph Generators '''

#Complete Graph Generator 
def complete_graph(n): 

    g = {i: [] for i in range(n)} #where every node has a list of it edges to other nodes where (a,b) means edge to a with weight b 

    for u in range(n): 
        for v in range(u + 1, n): 
            w = random.uniform(0, 1)
            g[u].append((v, w)) #we store this edge in both to optimize for this  
            g[v].append((u, w))

    return g 

#Hypercube Graph Generator 
def hypercube_graph(n):

    g = {i:[] for i in range(n)}

    #iterate through every pair of nodes 
    for u in range(n): 
        for v in range(u + 1, n):
    
            # if the difference in their value is a power of 2, then assign an edge to them with random uniform weight [0, 1]
            x = abs(u - v)
            if x > 0 and (x & (x - 1)) == 0:

                w = random.uniform(0,1)
                g[u].append((v,w))
                g[v].append((u,w))

    return g

#Unit Square Graph Generator 
def square_graph(n): 
    g = {}

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

                g[u].append((v, euc_dis))
                g[v].append((u, euc_dis))

    return g

#4 Dimensional Graph Generator
def teseract_graph(n): 
    g = {}

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

                g[u].append((v, euc_dis))
                g[v].append((u, euc_dis))

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
            if left < heap_len and self.heap[left][0] < self.heap[i][0]: 
                chosen_child = left 
            if right < heap_len and self.heap[right][0] < self.heap[chosen_child][0]: 
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

    #initialize S to keep track of visited nodes
    S = set()

    #initialize the prev data structure that just keeps track of the vertex that came before the current one in our spanning tree
    prev = {v: None for v in g}

    #track mst weight
    mst_weight = 0

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
        if prev[u] is not None:
            mst_weight += weight

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

    return mst_weight
    # #return the mst, which I think is reconstructed form the prev data structure 
    # mst = {v: [] for v in g}
    # for v in g:
    #     if prev[v] is not None:
    #         mst[v].append((prev[v], d[v]))
    #         mst[prev[v]].append((v, d[v]))
    # return mst

def avg_mst_weight(n, graph_type, trails = 5):
    total_weight = 0
    for i in range(trails):
        if graph_type == "complete":
            g = complete_graph(n)
        elif graph_type == "hypercube":
            g = hypercube_graph(n)
        else:
            raise ValueError("Invalid graph type")

        #sum up weights of all MSTs generated
        total_weight += prims_mst(g)

    #returns avergae weight of MSTs
    return total_weight / trails

if __name__ == "__main__":  

    #tests:
    # g_1 = complete_graph()
    # g_2 = hypercube_graph(5)
    # g_3 = square_graph(5)
    # g_4 = teseract_graph(5)

    # print(g_4)

    # mst_1 = prims_mst(g_1)
    #experiments
    graph_types = ["complete", "hypercube"]
    trials = 5
    n_values = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]

    # Store results as a list of tuples
    results = []

    print("Running experiments...")
    for graph_type in graph_types:
        for n in n_values:
            if graph_type == "hypercube" or (graph_type == "complete" and n <= 32768):
                avg_weight = avg_mst_weight(n, graph_type, trials)
                results.append((graph_type, n, avg_weight))
                print(f"{graph_type} Graph: n={n}, Avg MST Weight={avg_weight:.4f}")

    # Store results in a DataFrame
    df = pd.DataFrame(results, columns=["Graph Type", "n", "Average MST Weight"])

    # Save to CSV
    df.to_csv("mst_experiment_results.csv", index=False)

    # Print table
    print("\nExperiment Results:")
    print(df.to_string(index=False))



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
        pass

    def push(self):
        #adds a new value into the heap and maintains heap structure. This is Insert() in the lecture 6 notes 
        pass 


''' Below you can find Prim's Minimum Subtree Algorithm'''

def prims_mst(g): 
    pass
    #initialize d data structure to keep track of the distances

    #initialize the heap & insert the source node 

    #initialize S, which I think contains all the vertices we already have spanned

    #initialize the prev data structure that just keeps track of the vertex that came before the current one in our spanning tree

    #While the queue is not empty

        #pop the minimum vertex (highest priority vertex)

        #add this vertex to S

        #for all of that vertex's edges whose destination vertices are not in S

            #if d[v] is greater than our newly calculated distance to v: 

                #update d[v]

                #update prev[v]

                #insert v into the queue

    #return the mst, which I think is reconstructed form the prev data structure 




if __name__ == "__main__":  

    g_1 = complete_graph(5)
    g_2 = hypercube_graph(5)
    g_3 = square_graph(5)
    g_4 = teseract_graph(5)

    print(g_4)

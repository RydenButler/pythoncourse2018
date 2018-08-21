## Function to link 2 nodes (not in the sense of last script)
def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

## Grid Network
## TODO: create a square graph with 256 nodes using the makeLink function
## TODO: define a function countEdges
import math

def makeSquare(n):
    dim = int(math.sqrt(n))
    square = {}
    for i in range(dim): 
        row = i*dim
        for j in range(dim-1):
            square = makeLink(square, row+j, row+j+1)
            if i != dim - 1:
                square = makeLink(square, row+j , row+j+dim)
        if i != dim - 1:
            square = makeLink(square, row+j+1, (row+j+dim+1))
    return square


def makeOtherSquare(n):
    dim = int(math.sqrt(n))
    square = {}
    for i in range(1,n+1):
        if i%dim != 0:
            square = makeLink(square, i, i + 1)
        if i not in range(n-dim+1, n+1):
            square = makeLink(square, i, i + dim)
    return square

makeOtherSquare(16)


def countEdges(square):
    dim = int(math.sqrt(len(square.keys())))
    return dim * (dim - 1) * 2

countEdges(makeSquare(16))


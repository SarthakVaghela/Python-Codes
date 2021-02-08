#This code is done for GRAPH A ONLY
#Name: Sarthak Vanrajsinh Vaghela
#Std Num: 110005362
adj_list = {
    "A":["B", "D"],
    "B":["C", "D"],
    "C":["D", "G"],
    "D":["G"],
    "G":[],
    "S":["A", "B"]

}
'''adj_list = {
    "A":["B", "D", "S"],
    "B":["C", "D", "S"],
    "C":["B", "D", "G"],
    "D":["A", "B", "C", "G"],
    "G":["C", "D"],
    "S":["A", "B"]

}'''

color = {}
parent = {}
trav_time = {}
dfs_traversal_output = []

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time = [-1, -1]

def dfs_util(u):
    color[u] = "G"
    dfs_traversal_output.append(u)

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    color[u] = "B"

dfs_util("S")
print("The traversal path is: ")
print(dfs_traversal_output)    

#The below section helps us to find the exact path
v = "G"
path = []

while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()
print("The exact path is: ")
print (path)
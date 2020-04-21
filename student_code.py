from queue import PriorityQueue
from math import sqrt

def euclidean_heuristic(start, end, M):
    start_x = M.intersections[start][0]
    start_y = M.intersections[start][1]
    end_x = M.intersections[end][0]
    end_y = M.intersections[end][1]
    
    return sqrt((start_x - end_x) ** 2 + (start_y - end_y) ** 2)
    
def shortest_path(M, start, goal):
    parent = {} # save the correct parent of a node since we need to display the path
    distances = {} # save the intermediate distance for a node 
    parent[start] = None # the first node has no parent
    distances[start] = 0
    
    priority = PriorityQueue()
    priority.put(start, 0)

    while not priority.empty():
        current_node = priority.get()# get the node with the minimum total_distance(f = g + h)
        
        #iterate through the connected nodes
        for neighbor in M.roads[current_node]:
            current_distance = euclidean_heuristic(current_node, neighbor, M) # calculate the distance between the node
            new_distance = distances[current_node] + current_distance # if we already passed through a node, we may find a better distance with another route
            
            if neighbor not in distances or new_distance < distances[neighbor]:
                goal_distance = euclidean_heuristic(neighbor, goal, M)# the distance from the new node to the goal node
                total_distance = new_distance + goal_distance # f = g + h
                distances[neighbor] = new_distance
                parent[neighbor] = current_node
                priority.put(neighbor, total_distance)

    #at the end we get the path using the parents of the nodes
    current_node = goal
    path = [current_node]
    while current_node != start:
        current_node = parent[current_node]
        path.append(current_node)
    return path[::-1]#we need to reverse the path since we started from the goal and went backwards

"""
A module containing network functions to generate and read from networks.

@author: hollybossart
"""


import networkx as nx
import numpy as np
from itertools import product


def generate_random_walk(Ny, Nx, agents, torus, mean_path_length):
    """

    :param Ny: Number of columns in domain
    :param Nx: Number of rows in domain
    :param agents: numpy array of agentIDs
    :param torus: Boolean flag for wrap around / not wrapping around grid
    :param mean_path_length: 

    :return: dictionary of agent and their network connections

    """        
    # generating the coordinates for location stored as tuples
    # this uses something similar to an x y coordinate, so it may seem backwards
    coordinates = [(i, j) for i in range(Ny) for j in range(Nx)]
    
    # create grid network and relabel the nodes 
    network = nx.grid_2d_graph(Nx, Ny, torus)
    network = nx.relabel_nodes(network, dict(zip(coordinates, agents)))
    
    # create a dictionary that will store the current location of each agent
    # this will eventually change but it starts with each agent at their coordinate
    current_loc_dict = dict(zip(agents, coordinates))
    
    # looping through time steps
    for i in time:
        
        # making a location dictionary to see who is at each location at any given time
        # this is organized such that each space is a key and the agents on it are the values
        # this is reset at the beginning of each time step
        coord_dict = dict(zip(coordinates, [None]*len(coordinates)))
        
        # looping through each agent to move
        for agent in current_loc_dict.keys():
            
            # randomly decides where the agent will "move" to make connection
            direction = np.random.randint(1,5)
        
            # getting current location of agent
            current_loc = current_loc_dict[agent]
            x_coord = current_loc[0]
            y_coord = current_loc[1]
            
            # moving west
            if direction == 1:
                new_loc = (x_coord - 1, y_coord)
                
                # check if "moving" off of the board
                if new_loc[0] < 0:
                    if torus:
                        new_loc = (Ny-1, y_coord)
                    else:
                        new_loc = current_loc
                    
                
             # moving east
            if direction == 2:
                new_loc = (x_coord + 1, y_coord)
                
                # check if "moving" off of the board
                if new_loc[0] > Ny-1: 
                    if torus:
                        new_loc =  new_loc = (0, y_coord)
                    else:
                        new_loc = current_loc
                    
                
            # moving north   
            if direction == 3:
                new_loc = (x_coord, y_coord+1)
                
                if new_loc[1] > Nx-1:
                    if torus:
                        new_loc = (x_coord, 0)
                    else:
                        new_loc = current_loc
                        
            # moving south
            if direction == 4:
                new_loc = (x_coord, y_coord-1)
                
                if new_loc[1] < 0:
                    if torus:
                        new_loc = (x_coord, Nx-1)
                    else:
                        new_loc = current_loc
                    
                    
            # now that the agent has "moved" we will add each agent to the dict
            # of who is at each coordinate to establish connections
            # if the current value is None (loc empty), then we need to replace with agent
            if coord_dict[new_loc] == None:
                temp = {new_loc: [agent]}
                coord_dict.update(temp)
            else: 
                # we need to append the current agent on to already existing agents at loc
                coord_dict[new_loc].append(agent)
                
                
            # we also need to save the current location of each agent for further walking
            current_loc_dict[agent] = new_loc
        
        # end of inner for loop -- all agents have moved after this time step 
         
        # now that we know who has made a connection with who, we need to mark that connection 
        for spot in coord_dict:
            
            # current agents at the given coordinate location
            current_agents = coord_dict[spot]
            
            if current_agents != None:
                # creates all possible edge combinations 
                edge_tuples = list(product(current_agents, current_agents))
                network.add_edges_from(edge_tuples)
    
    
    return network
    
    

def generate_erdos_renyi(agents):
    
    return 
    

def generate_barabasi_alberts(agents):
    
    return 

def get_neighbors(network, agentID):
    
    return 
    


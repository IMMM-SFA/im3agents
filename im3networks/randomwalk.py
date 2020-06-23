"""Random walk class.

:author:   hollybossart
:email:    hollybossart@u.boisestate.edu

License:  BSD 2-Clause, see LICENSE and DISCLAIMER files

"""
import numpy as np

class RandomWalk:
    """This is the class that builds a random walk network.

    :param agentIDs:               Set of agent IDs
    :type agentIDs:                numpy array of ints



    """
   


    def __init__(self, agentIDs):
        self._agentIDs = agentIDs

    @property
    def agents(self):
        """Agents must not be empty."""

        if self._agentIDs.size == 0:
            raise ValueError(f"Agents array must not be empty.")

        else:
            return self._agentIDs
        
    # TODO: docstrings -- maybe build network will actually occur in the init?
    def build_network(self):
        
    
    # TODO: docstrings
    # will return an array of the agent IDs
    @property
    def adjacency_dict(self):
        
    


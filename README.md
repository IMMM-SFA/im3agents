[![Build Status](https://travis-ci.org/IMMM-SFA/im3agents.svg?branch=master)](https://travis-ci.org/IMMM-SFA/im3agents)
[![codecov](https://codecov.io/gh/IMMM-SFA/im3agents/branch/master/graph/badge.svg)](https://codecov.io/gh/IMMM-SFA/im3agents)

# im3agents
A versatile agent and network library for Python.

## Contact
- Holly Bossart (hollybossart@u.boisestate.edu)
- Kendra Kaiser (kendrakaiser@boisestate.edu)

## Overview
The purpose of `im3agents` is to create a single library for IM3 projects to create and utilize networks and agent-based models (ABMs.)


## Getting Started Using the `im3agents` Package
The `im3agents` package uses only **Python 3.3** and up.

### Step 1:
You can install `im3agents` by running the following from your cloned directory (NOTE: ensure that you are using the desired `pip` instance that matches your Python3 distribution):

`pip3 install git+https://github.com/IMMM-SFA/im3agents.git --user`

### Step 2:
Confirm that the module and its dependencies have been installed by running from your prompt:

```python
import im3agents
```

If no error is returned then you are ready to go!

## Setting Up 

### Network Types
| Name | Description  | Additional Information |
| -- | -- | -- |
| [Barabasi-Albert](https://networkx.github.io/documentation/stable/reference/generated/networkx.generators.random_graphs.barabasi_albert_graph.html) | This graph is characterized by preferential attachment.  | See ['Emergence of scaling in random networks'](https://arxiv.org/abs/cond-mat/9910332) |
| [Erdos-Renyi](https://networkx.github.io/documentation/stable/reference/generated/networkx.generators.random_graphs.erdos_renyi_graph.html#networkx.generators.random_graphs.erdos_renyi_graph) | This algorithm chooses all possible edges with some given probability, `p.` | See ['On random graphs.'](https://www.renyi.hu/~p_erdos/1959-11.pdf) |
| [Watts-Strogatz Small World](https://networkx.github.io/documentation/stable/reference/generated/networkx.generators.random_graphs.watts_strogatz_graph.html) | Each node is joined with its `k` nearest neighbors with probability `p` of rewiring. |  See ['Collective dynamics of small world networks'](https://www.nature.com/articles/30918)|
| Random Walk | This networks simulates how agents "walk" in one of the four cardinal directions to make connections. |  See [Muthukrishna and Schaller](https://journals.sagepub.com/doi/10.1177/1088868319855783).|

See the `networkx` documentation for more information.

## Examples


### Example 1: Accessing network connections
The network structures are stored as `dict` data types. This allows for easy and fast access to network connections using built-in Python 
`dict` functionality without much overhead.


Assuming that a network structure (for example, `N`) has already been created by one of the above methods, then accessing the connections
of some known agent, (for example, `1234`) can be done as follows:

``` 
connections = N[1234]
```

where `connections` is a list.

To learn more about built-in `dict` functionality that can be used on your network, view the [Python documentation.](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) 

### Example 2: Plotting your network
To import a network and plot it from the `dict` data structure, you need to first convert the given `dict` to a `networkX` graph object using the [following function.](https://networkx.github.io/documentation/stable/reference/generated/networkx.convert.from_dict_of_dicts.html#networkx.convert.from_dict_of_dicts)

```
import networkx as nx

network_dictionary = generate_small_world(agentIDs, kneighbors, rewire_prob)
G = nx.convert.from_dict_of_lists(network_dictionary)
nx.draw(G)

```

## Notes:
* This version of `im3agents` does not support edge information, including edge weights, between agents. This is possible to implement in a future version by updating the output type of networks to `dict` of `dict`, rather than a `dict` of `list` type. 

* If you plan to include this in your `requirements.txt` file, the proper way to do this is the following:
`im3agents==<VERSIONNUMBER>|https://github.com/IMMM-SFA/im3agents/archive/<VERSIONNUMBER>.zip#egg=im3agents-<VERSIONNUMBER>` where `<VERSIONNUMBER>` is equal to the current version number, which is 0.3.0.


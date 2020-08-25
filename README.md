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
| Name | Description | Additional Parameters |
| -- | -- | -- |
| Barabasi-Albert | | |
| Erdos-Renyi | | | 
| Watts-Strogatz Small World | | |
| Random Walk | | |

## Examples

### Example 1:  Creating a Barabasi-Albert, Erdos-Renyi or Watts-Strogatz Small World network structure

The inputs for these three network generators is a `numpy` array of agent IDs.
*Note:* Each agent must have a unique, hashable attribute as an ID for the network generation to work.


### Example 2: Creating a Random Walk network structure

### Example 3: Accessing network connections
The network structures are stored as `dict` data types. This allows for easy and fast access to network connections using built-in Python 
`dict` functionality without much overhead.


Assuming that a network structure (for example, `N`) has already been created by one of the above methods, then accessing the connections
of some known agent, (for example, `1234`) can be done as follows:

``` 
connections = N[1234]
```

To learn more about built-in `dict` functionality that can be used on your network, view the [Python documentation.](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) 

#### Example 4: Plotting your network

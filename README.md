[![Build Status](https://travis-ci.org/IMMM-SFA/im3agents.svg?branch=master)](https://travis-ci.org/IMMM-SFA/im3agents)
[![codecov](https://codecov.io/gh/IMMM-SFA/im3agents/branch/master/graph/badge.svg)](https://codecov.io/gh/IMMM-SFA/im3agents)

# im3agents
A versatile agent library for Python


## Overview
The purpose of `im3agents` is to ...

## Getting Started Using the `im3agents` Package
The `im3agents` package uses only **Python 3.3** and up.

### Step 1:
You can install `im3py` by running the following from your cloned directory (NOTE: ensure that you are using the desired `pip` instance that matches your Python3 distribution):

`pip3 install git+https://github.com/IMMM-SFA/im3agents.git --user`

### Step 2:
Confirm that the module and its dependencies have been installed by running from your prompt:

```python
import im3agents
```

If no error is returned then you are ready to go!


## Examples

### Example 1:  FarmerOne agent has an age
```python
from im3agents.farmers import FarmerOne

farmer_one = FarmerOne(age=32)

print(farmer_one.age)
```

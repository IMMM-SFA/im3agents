[![Build Status](https://travis-ci.org/IMMM-SFA/im3py.svg?branch=master)](https://travis-ci.org/IMMM-SFA/im3py) 
[![codecov](https://codecov.io/gh/IMMM-SFA/im3py/branch/master/graph/badge.svg)](https://codecov.io/gh/IMMM-SFA/im3py)

# im3agents
A versatile agent library for Python


## Overview
The purpose of `im3agents` is to help developers quickly establish a GitHub repository that conforms to IM3 software engineering standards.  Our hope is to create a common user experience for all Python modeling software developed for use in IM3 experiments.  We are mindfully developing software that exposes key variables per time-step so that they may be used in integrated and/or uncertainty characterization experiments while still maintaining the ability for autonomous use.  This template package establishes the structure necessary to wrap existing Python code in our modeling interface and time-step processing generator.  We also include:  a sample test suite, `Zenodo`, `Travis-CI`, and `codecov` standard files and setup protocol, our expected `docstring` style, a `stdout` and file logger, and an example fake code file that represents a user's code contribution.

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

## Setting up a run

## Examples

### Example 1:  FarmerOne agent has an age
```python
from im3agents.farmers import FarmerOne

farmer_one = FarmerOne(age=32)

print(farmer_one.age)
```

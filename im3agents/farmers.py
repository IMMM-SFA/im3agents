"""Farmer classes.

:author:   Someone
:email:    someone@pnnl.gov

License:  BSD 2-Clause, see LICENSE and DISCLAIMER files

"""


class FarmerOne:
    """This is the first Farmer agent.

    :param age:                     Age of farmer
    :type age:                      int


    CLASS ATTRIBUTES:

    :param AGE_MIN:                 Minimum age of a farmer
    :type AGE_MIN:                  int

    :param AGE_MAX:                 Maximum age of a farmer
    :type AGE_MAX"                  int

    """
    # minimum and maximum of acceptable farmer ages
    AGE_MIN = 0
    AGE_MAX = 150

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        """Age of farmer must be between expected age."""

        if self._age > FarmerOne.AGE_MAX:
            raise ValueError(f"FarmerOne age '{self._age}' is greater than allowable age of '{FarmerOne.AGE_MAX}'")

        elif self._age < FarmerOne.AGE_MIN:
            raise ValueError(f"FarmerOne age '{self._age}' is less than allowable age of '{FarmerOne.AGE_MIN}'")

        else:
            return self._age

"""Farmer class tests.

:author:   Someone
:email:    someone@pnnl.gov

License:  BSD 2-Clause, see LICENSE and DISCLAIMER files

"""

import unittest

from im3agents.farmers import FarmerOne


class TestFarmers(unittest.TestCase):

    def test_farmerone(self):

        error_min_age = FarmerOne(age=-1)
        error_max_age = FarmerOne(age=151)
        valid = FarmerOne(age=32)

        # expect value errors for exceeding min and max
        with self.assertRaises(ValueError):
            error_min_age.age

        with self.assertRaises(ValueError):
            error_max_age.age

        # expect valid age
        self.assertEqual(valid.age, 32)


if __name__ == '__main__':
    unittest.main()

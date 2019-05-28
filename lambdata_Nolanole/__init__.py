#!/usr/bin/env python
"""
lambdata - a collection of Data Science helper functions
"""

import pandas as pd
import numpy as np
from . import example_module
from . import helper_functions

Y = example_module.increment(example_module.x)
TEST = pd.DataFrame(np.ones(10))
# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.distance import haversine
import pytest


def test_haversine():
    assert haversine(0, 0, 0, 0) == 0


# -*- coding: UTF-8 -*-

# Import from standard library
import mlproject
# Import from our lib
from mlproject.tools import haversine
import pytest


def test_haversine():
    coordinates = (48.865, 2.380, 48.235, 2.393)
    out = haversine(*coordinates)
    assert out == 70.00696965697475

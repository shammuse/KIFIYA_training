import pytest
from app.utils import load_data

def test_load_data():
   data = load_data()
   assert data is not None  # Check that data is loaded.
   assert 'GHI' in data.columns  # Check that 'GHI' column exists.

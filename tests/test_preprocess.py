import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocess import replace_tokens
def test_grocer_replacement():
    raw = "POS Purchase Woolworths Bryanston * 15 Oct"
    expected = "pos purchase [grocers] bryanston [date]"
    result = replace_tokens(raw, label="Groceries")
    assert result == expected


def test_restaurant_location_inference():
    raw = "POS Purchase Marble Pantry Arcadia * 12 Sep"
    expected = "pos purchase [restaurant] [location] [date]"
    result = replace_tokens(raw, label="Eating Out")
    assert result == expected


def test_fuel_location_extraction():
    raw = "Fuel Purchase Engen Mitchell Park * 07 Oct"
    expected = "fuel purchase [garage] [location] [date]"
    result = replace_tokens(raw, label="Fuel")
    assert result == expected

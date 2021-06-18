from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

given_name = "Spencer"
family_name = "Callister-Stecklein"
full_name = "Callister-Stecklein; Spencer"

def test_make_full_name():
    assert make_full_name(given_name, family_name) == "Callister-Stecklein; Spencer"

def test_extract_family_name():
    assert extract_family_name(full_name) == "Callister-Stecklein"

def test_extract_given_name():
    assert extract_given_name(full_name) == "Spencer"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])
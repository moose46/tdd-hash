# https://realpython.com/python-hash-table/
import pytest
from pytest_unordered import unordered

from hashtable import BLANK, HashTable


@pytest.fixture
def hash_table():
    sample_data = HashTable(capacity=100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data


def test_always_pass():
    pass


def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None


def _slots():
    assert len(HashTable(capacity=100)) == 0


def test_should_create_empty_value_slots():
    assert HashTable(capacity=3)._slots == [None, None, None]


def test_should_insert_key_value_slots():
    hash_table = HashTable(capacity=100)

    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    assert ("hola", "hello") in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs
    assert len(hash_table) == 3


@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass


def test_should_insert_none_value():
    hash_table = HashTable(capacity=100)
    hash_table["key"] = None
    assert ("key", None) in hash_table.pairs


def test_case_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=100).values


def test_should_find_value_by_key(hash_table: HashTable):
    assert hash_table["hola"] == "hello"
    assert hash_table[98.6] == 37
    assert hash_table[False] == True


def test_should_raise_error_on_missing_key():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing key"]
    assert exception_info.value.args[0] == "missing key"


def test_should_find_key(hash_table: HashTable):
    assert "hola" in hash_table


def test_not_should_find_key(hash_table: HashTable):
    assert "missing_key" not in hash_table


def test_should_get_value(hash_table: HashTable):
    assert hash_table.get("hola") == "hello"


def test_should_get_none_when_missing_key(hash_table: HashTable):
    assert hash_table.get("missing_key") is None


def test_should_get_default_value_when_missing_key(hash_table: HashTable):
    assert hash_table.get("missing_key", "default") == "default"


def test_should_get_value_with_default(hash_table: HashTable):
    assert hash_table.get("hola", "default") == "hello"


def test_should_delete_key_value_pair(hash_table: HashTable):
    assert "hola" in hash_table
    assert ("hola", "hello") in hash_table.pairs
    assert len(hash_table) == 3

    del hash_table["hola"]

    assert "hola" not in hash_table
    assert "hello" not in hash_table.pairs
    assert len(hash_table) == 2


# https://realpython.com/python-hash-table/#build-a-hash-table-prototype-in-python-with-tdd
def test_should_not_contain_none_value_when_created():
    hash_table = HashTable(capacity=100)
    values = [pair.value for pair in hash_table.pairs if pair]
    assert None not in values


def test_should_raise_key_error_when_deleting(hash_table: HashTable):
    with pytest.raises(KeyError) as exception_info:
        del hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"


def test_should_update_value(hash_table: HashTable):
    assert hash_table["hola"] == "hello"

    hash_table["hola"] = "hallo"

    assert hash_table["hola"] == "hallo"
    assert hash_table[98.6] == 37
    assert hash_table[False] == True
    assert len(hash_table) == 3


# def test_should_return_slots(hash_table: HashTable):
#     assert ("hola", "hello") in hash_table.pairs
#     assert (98.6, 37) in hash_table.pairs
#     assert (False, True) in hash_table.pairs


def test_should_return_copy_of_slots(hash_table: HashTable):
    assert hash_table.pairs is not hash_table.pairs


def test_should_not_include_blank_slots(hash_table: HashTable):
    assert None not in hash_table.pairs


def test_should_return_duplicate_values():
    hash_table = HashTable(capacity=100)
    hash_table["Alice"] = 24
    hash_table["Bob"] = 42
    hash_table["Joe"] = 42
    assert [24, 42, 42] == sorted(hash_table.values)


def test_should_get_values(hash_table: HashTable):
    assert unordered(hash_table.values) == ["hello", 37, True]


def test_should_get_values_of_empty_hash_table():
    assert HashTable(capacity=100).values == []


def test_should_return_copy_of_values(hash_table: HashTable):
    assert hash_table.values is not hash_table.values


def test_should_get_keys(hash_table: HashTable):
    assert hash_table.keys == {"hola", 98.6, False}


def test_should_get_keys_of_empty_hash_table():
    assert HashTable(capacity=100).keys == set()


def test_should_return_copy_of_keys(hash_table: HashTable):
    assert hash_table.keys is not hash_table.keys


def test_should_return_slots(hash_table: HashTable):
    assert hash_table.pairs == {("hola", "hello"), (98.6, 37), (False, True)}


def test_should_get_slots_of_empty_hash_table():
    assert HashTable(capacity=100).pairs == set()


def test_should_convert_to_dict(hash_table: HashTable):
    dictionary = dict(hash_table.pairs)
    assert set(dictionary.keys()) == hash_table.keys
    assert set(dictionary.items()) == hash_table.pairs
    assert list(dictionary.values()) == unordered(hash_table.values)


def test_should_report_length_of_empty_hash_table():
    assert len(HashTable(capacity=100)) == 0


def test_should_not_create_hashtable_with_zero_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=0)


def test_should_not_create_hashtable_with_negative_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=-100)


def test_should_report_length(hash_table):
    assert len(hash_table) == 3


def _slots_of_empty_hash_table():
    assert HashTable(capacity=100).capacity == 100


# def test_should_report_capacity(hash_table):
#     assert hash_table.capacity == 100


def test_should_create_empty_pair_slots():
    assert HashTable(capacity=3)._slots == [None, None, None]


# Make the Hash Table Iterable


def test_should_iterate_ver_keys(hash_table):
    for key in hash_table.keys:
        assert key in ("hola", 98.6, False)


def test_should_iterate_over_values(hash_table):
    for value in hash_table.values:
        assert value in ("hello", 37, True)


def test_should_iterate_over_pairs(hash_table):
    for key, value in hash_table.pairs:
        assert key in hash_table.keys
        assert value in hash_table.values


def test_should_iterate_over_instance(hash_table):
    for key in hash_table:
        assert key in ("hola", 98.6, False)

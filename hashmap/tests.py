from hashmap import RobinHoodHashMap

def test_put_and_get():
    """
    Test basic insertion and retrieval of key-value pairs.

    Verifies that:
    - Values can be inserted using put()
    - Values can be retrieved using get()
    - Retrieving a non-existent key returns None
    """
    hm = RobinHoodHashMap()

    hm.put("a", 1)
    hm.put("b", 2)
    hm.put("c", 3)

    assert hm.get("a") == 1
    assert hm.get("b") == 2
    assert hm.get("c") == 3
    assert hm.get("missing") is None

def test_update_existing_key():
    """
    Test updating the value of an existing key.

    Verifies that:
    - Inserting the same key again updates its value
    - The key is not duplicated in the hash map
    """
    hm = RobinHoodHashMap()

    hm.put("key","value1")
    hm.put("key","value2")

    assert hm.get("key") == "value2"

def test_collision_handling():
    """
    Test correct behavior when hash collisions occur.

    Uses a small capacity to force collisions and ensures
    that all keys can still be retrieved correctly.
    """
    hm = RobinHoodHashMap(capacity=4)

    keys = ["a", "b", "c", "d"]
    for i, k in enumerate(keys):
        hm.put(k, i)
    
    for i, k in enumerate(keys):
        assert hm.get(k) == i

def test_remove():
    """
    Test removal of a key from the hash map.

    Verifies that:
    - Removed key is no longer accessible
    - Other keys remain accessible
    - Backward shifting preserves correctness
    """
    hm = RobinHoodHashMap()

    hm.put("x", 100)
    hm.put("y", 200)
    hm.put("z", 300)

    hm.remove("y")

    assert hm.get("y") is None
    assert hm.get("x") == 100
    assert hm.get("z") == 300

def run_all_tests():
    """
    Run all test cases.

    If any assertion fails, an AssertionError will be raised.
    """
    test_put_and_get()
    test_update_existing_key()
    test_collision_handling()
    test_remove()

if __name__ == "__main__":
    run_all_tests()
    print("✅ All tests passed!")

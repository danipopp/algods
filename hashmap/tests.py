from hashmap import RobinHoodHashMap

def test_put_and_get():
    hm = RobinHoodHashMap()

    hm.put("a", 1)
    hm.put("b", 2)
    hm.put("c", 3)

    assert hm.get("a") == 1
    assert hm.get("b") == 2
    assert hm.get("c") == 3
    assert hm.get("missing") is None

def test_update_existing_key():
    hm = RobinHoodHashMap()

    hm.put("key","value1")
    hm.put("key","value2")

    assert hm.get("key") == "value2"

def test_collision_handling():
    hm = RobinHoodHashMap(capacity=4)

    keys = ["a", "b", "c", "d"]
    for i, k in enumerate(keys):
        hm.put(k, i)
    
    for i, k in enumerate(keys):
        assert hm.get(k) == i

def test_remove():
    hm = RobinHoodHashMap()

    hm.put("x", 100)
    hm.put("y", 200)
    hm.put("z", 300)

    hm.remove("y")

    assert hm.get("y") is None
    assert hm.get("x") == 100
    assert hm.get("z") == 300

def run_all_tests():
    test_put_and_get()
    test_update_existing_key()
    test_collision_handling()

if __name__ == "__main__":
    run_all_tests()
    print("✅ All tests passed!")

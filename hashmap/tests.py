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

def run_all_tests():
    test_put_and_get()

if __name__ == "__main__":
    run_all_tests()
    print("✅ All tests passed!")

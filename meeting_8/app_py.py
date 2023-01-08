def f(x):
    #if x == 0:
    #    return 1
    return x * 2

if __name__ == "__main__":
    assert 'H' in "Hello World"
    assert 2 * 2 == 4
    assert 5 > 3 and 10 < 11

    assert f(2) == 4, "Functia trebuia sa returneze 4"
    assert f(10) == 20, "Functia trebuia sa returneze 20"

    print("Hello World")
    print(f"f(2)={f(2)}")
    print(f"f(100)={f(100)}")
    print(f"f(-5)={f(-5)}")
    print(f"f(3.14)={f(3.14)}")

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return (temp)

def test_temperature():
    test1 = "25"
    test2 = "abc"

    print("=== Garden Temperature ===")

    try:
        print(f"Input data is '{test1}'")
        temp1 = input_temperature(test1)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught: {e}")

    try:
        print(f"Input data is '{test2}'")
        temp2 = input_temperature(test2)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught: {e}")

    print("All tests completed - program didn't crash!")

if __name__ == __main__:
    test_temperature()
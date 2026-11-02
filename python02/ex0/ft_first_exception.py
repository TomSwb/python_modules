
def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return (temp)

def test_temperature():
    test1 = 25
    test2 = abc
    
    try:
        print(f"Input temperature is '{input_temperature(test1)}'")
    except:
    
    print("All tests completed - program didn't crash!")


if __name__ == __main__:
    test_temperature()
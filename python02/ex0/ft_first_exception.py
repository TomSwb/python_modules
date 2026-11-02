
def input_temperature(temp_str: str):
    temp = (int)(input)
    return (temp)

def test_temperature():
    input_temperature(25)
    print("Input temperature is '25'")
    
    print("All tests completed - program didn't crash!")


if __name__ == __main__:
    test_temperature()
#not working 

def byte_size(something):
    try:
        byte_size=len(something.encode('utf-8'))
        print(f"byte size of {something}: {byte_size}")
    except TypeError:
        print(f"Error: {something} is not a string and cannot be encoded.")
    except Exception as e:
        print(f"An error occurred: {e}")

byte_size('a')
byte_size("A")
byte_size("@")
byte_size("sri")
byte_size(123)
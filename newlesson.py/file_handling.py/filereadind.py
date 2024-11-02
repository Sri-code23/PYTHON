#txt file reading

file_name="C:\\Users\\vaath\\OneDrive\\Desktop\\sampler.txt"

try:
    with open(file_name,"r") as file:
        content=file.read()
        print(content)

except FileNotFoundError :
    print("file not found")        
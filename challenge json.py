import json

def generate_array():
    result = []

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result.append("BIG BANG")
        elif i % 3 == 0:
            result.append("BIG")
        elif i % 5 == 0:
            result.append("BANG")
        else:
            result.append(str(i))

    return result

output = generate_array()

with open('output.json', 'w') as file:
    json.dump(output, file)

print("Array generated and saved in output.json")

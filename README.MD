CODING:

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



STEP:
from 1 to 100

if the number can be divided by 3, it will display "BIG"
if the number can be divided by 5, it will display "BANG"
if the number can be divided by both at once, it will display "BIG BANG"

that's why the results came out BIG, BANG, BIGBANG if it can devide with 3 or 5 or both number.

and it will save in the array

after the forloop is finished, he will save the array value in the json file

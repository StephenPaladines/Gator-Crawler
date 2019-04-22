'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


import json
import jsonlines
import geocoder

def save_obj_json(obj, name):
    with open(name + '.json', 'w') as f:
        json.dump(obj,f)
def create_jsonlines(original):

    if isinstance(original, str):
        original = json.loads(original)

    return '\n'.join([json.dumps(original[outer_key], sort_keys=True) 
                      for outer_key in sorted(original.keys(),
                                              key=lambda x: int(x))])

# Added fake record to prove order is sorted
inp = {
    "3168494915": {
        "Rating": "3.5",
        "Position": "data engineer",
        "Company": "Wintrust Financial",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 71,
        "Salary High": 97,
        "Size": "1001to5000Employees",
        "Industry": "Banks&CreditUnions",
        "HQ": "Rosemont",
        "HQ State": "IL",
        "Size Low": 1001,
        "Size High": 5000
    },
    "3125653622": {
        "Rating": "3.6",
        "Position": "big data software engineer",
        "Company": "Verizon",
        "City": "Temple Terrace",
        "State": "FL",
        "Salary Low": 63,
        "Salary High": 111
    },
    "3185555588": {
        "Rating": "4.3",
        "Position": "data scientist",
        "Company": "Elutions",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 71,
        "Salary High": 107,
        "Size": "1to50Employees",
        "Industry": "ComputerHardware&Software",
        "HQ": "Tampa",
        "HQ State": "FL",
        "Size Low": 1,
        "Size High": 50
    }
}
#print(inp["3168494915"]["Rating"])
for key in inp:
    inputLoc = inp[key]["City"] + ', ' + inp[key]["State"]
    print(inputLoc) 
    location = geocoder.google([45.15, -75.14], method='reverse')
    print(location)

# output = create_jsonlines(inp)
# # with jsonlines.open('output.json', mode='w') as reader:
# with jsonlines.open('output.json', mode='a') as writer:     # Mode 'a' for appending
#     for keys in inp:
#         writer.write(inp[keys])
#     writer.close()
# with open('madeup.ndjson', 'w') as file:
#     json.dumps(inp)
#print(output)
#save_obj_json(inp,'newNDJSON')

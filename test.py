'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


import json
import jsonlines

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
    "3181747098": {
        "Rating": "",
        "Position": "sr. data analyst",
        "Company": "",
        "City": "",
        "State": "",
        "Salary Low": 0,
        "Salary High": 0,
        "Size": "51to200Employees",
        "Industry": "Internet",
        "HQ": "SanFrancisco",
        "HQ State": "CA",
        "Size Low": 51,
        "Size High": 200
    },
    "3032554997": {
        "Rating": "3.4",
        "Position": "test engineer - automation",
        "Company": "Willis Towers Watson",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 50,
        "Salary High": 67
    },
    "3173097800": {
        "Rating": "3.2",
        "Position": "software engineer, senior-onsite/tampa office",
        "Company": "Healthesystems",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 93,
        "Salary High": 156,
        "Size": "201to500Employees",
        "Industry": "ITServices",
        "HQ": "Tampa",
        "HQ State": "FL",
        "Size Low": 201,
        "Size High": 500
    },
    "3017011907": {
        "Rating": "3.7",
        "Position": "data scientist",
        "Company": "ReliaQuest",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 86,
        "Salary High": 127,
        "Size": "201to500Employees",
        "Industry": "EnterpriseSoftware&NetworkSolutions",
        "HQ": "Tampa",
        "HQ State": "FL",
        "Size Low": 201,
        "Size High": 500
    },
    "2908993835": {
        "Rating": "3.4",
        "Position": "software engineer iii",
        "Company": "UMA Education",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 52,
        "Salary High": 94,
        "Size": "1001to5000Employees",
        "Industry": "EducationTrainingServices",
        "HQ": "Tampa",
        "HQ State": "FL",
        "Size Low": 1001,
        "Size High": 5000
    },
    "3191121257": {
        "Rating": "2.9",
        "Position": "data scientist intern",
        "Company": "Gerdau",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 0,
        "Salary High": 0
    },
    "3187588188": {
        "Rating": "3.1",
        "Position": "senior database administrator",
        "Company": "Community Brands",
        "City": "Saint Petersburg",
        "State": "FL",
        "Salary Low": 66,
        "Salary High": 99,
        "Size": "1001to5000Employees",
        "Industry": "EnterpriseSoftware&NetworkSolutions",
        "HQ": "SaintPetersburg",
        "HQ State": "FL",
        "Size Low": 1001,
        "Size High": 5000
    },
    "3184172547": {
        "Rating": "3.3",
        "Position": "junior big data engineer for strategic data platform",
        "Company": "Citibank",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 73,
        "Salary High": 93,
        "Size": "5001to10000Employees",
        "Industry": "Lending",
        "HQ": "ElkGroveVillage",
        "HQ State": "IL",
        "Size Low": 5001,
        "Size High": 10000
    },
    "3183057246": {
        "Rating": "1.7",
        "Position": "data engineer",
        "Company": "GEX",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 53,
        "Salary High": 75,
        "Size": "51to200Employees",
        "Industry": "Publishing",
        "HQ": "Atkinson",
        "HQ State": "NH",
        "Size Low": 51,
        "Size High": 200
    },
    "3188627118": {
        "Rating": "3.6",
        "Position": "data scientist",
        "Company": "DTCC",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 76,
        "Salary High": 110,
        "Size": "1001to5000Employees",
        "Industry": "BrokerageServices",
        "HQ": "NewYork",
        "HQ State": "NY",
        "Size Low": 1001,
        "Size High": 5000
    },
    "3152544320": {
        "Rating": "4.1",
        "Position": "entry level software engineer (no coding experience required)",
        "Company": "Revature",
        "City": "Saint Petersburg",
        "State": "FL",
        "Salary Low": 34,
        "Salary High": 60,
        "Size": "1001to5000Employees",
        "Industry": "ITServices",
        "HQ": "Reston",
        "HQ State": "VA",
        "Size Low": 1001,
        "Size High": 5000
    },
    "3191782863": {
        "Rating": "5.0",
        "Position": "data engineer",
        "Company": "Clearly Agile, Inc",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 0,
        "Salary High": 0,
        "Size": "1to50Employees",
        "Industry": "ITServices",
        "HQ": "Tampa",
        "HQ State": "FL",
        "Size Low": 1,
        "Size High": 50
    },
    "3184579228": {
        "Rating": "3.6",
        "Position": "data engineer",
        "Company": "Amgen",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 79,
        "Salary High": 106
    },
    "3193527175": {
        "Rating": "3.0",
        "Position": "systems engineer iii - remedy developer - spectrum enterprise",
        "Company": "Spectrum",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 58,
        "Salary High": 115
    },
    "3026392183": {
        "Rating": "3.6",
        "Position": "software engineer i",
        "Company": "Raytheon",
        "City": "Saint Petersburg",
        "State": "FL",
        "Salary Low": 54,
        "Salary High": 83
    },
    "3156943515": {
        "Rating": "3.1",
        "Position": "data engineer",
        "Company": "Modis",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 0,
        "Salary High": 0,
        "Size": "5001to10000Employees",
        "Industry": "Staffing&Outsourcing",
        "HQ": "Jacksonville",
        "HQ State": "FL",
        "Size Low": 5001,
        "Size High": 10000
    },
    "3130521210": {
        "Rating": "3.5",
        "Position": "intern, data science",
        "Company": "Nielsen",
        "City": "Oldsmar",
        "State": "FL",
        "Salary Low": 0,
        "Salary High": 0
    },
    "3182896025": {
        "Rating": "3.9",
        "Position": "systems engineer",
        "Company": "Novetta",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 63,
        "Salary High": 117,
        "Size": "501to1000Employees",
        "Industry": "EnterpriseSoftware&NetworkSolutions",
        "HQ": "McLean",
        "HQ State": "VA",
        "Size Low": 501,
        "Size High": 1000
    },
    "3132632957": {
        "Rating": "4.8",
        "Position": "order processor/administrative assistant/data entry",
        "Company": "KnowBe4",
        "City": "Clearwater",
        "State": "FL",
        "Salary Low": 0,
        "Salary High": 0,
        "Size": "501to1000Employees",
        "Industry": "SecurityServices",
        "HQ": "Clearwater",
        "HQ State": "FL",
        "Size Low": 501,
        "Size High": 1000
    },
    "3180719502": {
        "Rating": "3.5",
        "Position": "junior big data engineer for strategic data platform",
        "Company": "Citi",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 97,
        "Salary High": 122
    },
    "3178324053": {
        "Rating": "4.0",
        "Position": "data engineer",
        "Company": "Misource",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 73,
        "Salary High": 101,
        "Size": "51to200Employees",
        "Industry": "Staffing&Outsourcing",
        "HQ": "Tampa",
        "HQ State": "FL",
        "Size Low": 51,
        "Size High": 200
    },
    "3192520071": {
        "Rating": "5.0",
        "Position": "data analyst",
        "Company": "Technology Hub Inc.",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 0,
        "Salary High": 0,
        "Size": "1to50Employees",
        "Industry": "Consulting",
        "HQ": "RoyalOak",
        "HQ State": "MI",
        "Size Low": 1,
        "Size High": 50
    },
    "3181153158": {
        "Rating": "3.6",
        "Position": "data engineer",
        "Company": "Ozark",
        "City": "Saint Petersburg",
        "State": "FL",
        "Salary Low": 0,
        "Salary High": 0,
        "Size": "501to1000Employees",
        "Industry": "Sports&Recreation",
        "HQ": "Houston",
        "HQ State": "TX",
        "Size Low": 501,
        "Size High": 1000
    },
    "3087478355": {
        "Rating": "4.3",
        "Position": "big data engineer (hadoop/spark/kafka)",
        "Company": "Haneke Design",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 0,
        "Salary High": 0,
        "Size": "1to50Employees",
        "Industry": "ITServices",
        "HQ": "Tampa",
        "HQ State": "FL",
        "Size Low": 1,
        "Size High": 50
    },
    "3186793580": {
        "Rating": "3.6",
        "Position": "data analyst",
        "Company": "New York Life",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 46,
        "Salary High": 72
    },
    "3116061175": {
        "Rating": "4.4",
        "Position": "mid-level software engineer",
        "Company": "Tradepmr",
        "City": "Saint Petersburg",
        "State": "FL",
        "Salary Low": 70,
        "Salary High": 85,
        "Size": "51to200Employees",
        "Industry": "InvestmentBanking&AssetManagement",
        "HQ": "Gainesville",
        "HQ State": "FL",
        "Size Low": 51,
        "Size High": 200
    },
    "3191020396": {
        "Rating": "",
        "Position": "big data engineer with spark streaming",
        "Company": "Emonics LLC",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 0,
        "Salary High": 0,
        "Size": "1to50Employees",
        "Industry": "Electrical&ElectronicManufacturing",
        "HQ": "Langhorne",
        "HQ State": "PA",
        "Size Low": 1,
        "Size High": 50
    },
    "3152162933": {
        "Rating": "4.8",
        "Position": "data scientist",
        "Company": "Barbaricum",
        "City": "Tampa",
        "State": "FL",
        "Salary Low": 65,
        "Salary High": 94,
        "Size": "51to200Employees",
        "Industry": "Consulting",
        "HQ": "Washington",
        "HQ State": "DC",
        "Size Low": 51,
        "Size High": 200
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
output = create_jsonlines(inp)
# with jsonlines.open('output.json', mode='w') as reader:
with jsonlines.open('output.json', mode='a') as writer:     # Mode 'a' for appending
    for keys in inp:
        writer.write(inp[keys])
    writer.close()
# with open('madeup.ndjson', 'w') as file:
#     json.dumps(inp)
#print(output)
#save_obj_json(inp,'newNDJSON')

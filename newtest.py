from helper import load_obj_json,load_obj_ndjson, get_csv, save_obj_json, save_obj_ndjson

jobDict = []
jobDict = load_obj_ndjson('glassDoorDict')
try:
	# jobDict = load_obj_json('glassDoorDict')
	jobDict = load_obj_json('glassDoorDict')
	link =    load_obj_json('glassDoorlink')
except:
	# save_obj_json({}, 'glassDoorDict')
	save_obj_json([], 'glassDoorlink')
	# save_obj_ndjson([], 'glassDoorDict')

	# jobDict = load_obj_json('glassDoorDict')
	link =    load_obj_json('glassDoorlink')
	# jobDict =    load_obj_json('glassDoorDict')

print(jobDict)

for x in range(0,10):
	jobDict.append('Name') 

print(jobDict)
save_obj_ndjson(jobDict, 'glassDoorDict')
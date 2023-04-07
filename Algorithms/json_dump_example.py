# json.dumps() - convert python object into a JSON sting.
import json
    
# Data to be written
dictionary ={
  "id": "04",
  "name": "sunil",
  "department": "HR"
}
    
# Serializing json 
json_object = json.dumps(dictionary, indent = 4)
print(json_object)

#json.dump() -- used for writing to JSON file. 

dictionary ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}
  
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)

#json load() - takes a file object and return the json object.    

with open("sample.json", "r") as read_content:
    print(json.load(read_content))

#json loads() is used to parse a valid JSON string and convert it to python dictionary.It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary. 

    import json 
    
# JSON string: 
# Multi-line string 
data = """{ 
    "Name": "Jennifer Smith", 
    "Contact Number": 7867567898, 
    "Email": "jen123@gmail.com", 
    "Hobbies":["Reading", "Sketching", "Horse Riding"] 
    }"""
    
# parse data: 
res = json.loads( data ) 
    
# the result is a Python dictionary: 
print( res )
import json

testData_path = r"data\testData.json"
class FileReader:
    def json_fileReader(self):
        with open(testData_path) as f:
            jsonTest_data = json.load(f)
            test_data = jsonTest_data["purchageOrder"]
            return test_data
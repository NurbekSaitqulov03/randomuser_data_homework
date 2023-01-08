import json

def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    x = filename.values()
    for i in x:
        if type(i) == list:
            return i
f = open('randomuser_data.json', 'r')
a = f.read()
b = json.loads(a)
print(get_data(b))
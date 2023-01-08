from webbrowser import get
import get_data
import json

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    return len(data.get('results'))
f = open('randomuser_data.json', 'r')
d = f.read()
a = json.loads(d)
print(get_count_users(a))
import get_data
import json
def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    results = data['results']
    for user in results:
        print(user['name']['first'],user['name']['last'])



f= open('randomuser_data.json').read()
data = json.loads(f)
get_users_data(data)
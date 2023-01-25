from get_data import get_data

import json
def get_users_data(data:dict) -> list:
    lst = []
    results = data['results']
    for user in results:
        a = user['name']['first']
        b = user['name']['last']
        c = user['phone']
        ans = {"first_name":a,"last_name":b,"phone_number":c}
        lst.append(ans)
    return lst
data = get_data('randomuser_data.json')
print(get_users_data(data))
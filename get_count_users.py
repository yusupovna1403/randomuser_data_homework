from webbrowser import get
from get_data import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    sum_users = 0
    results = data['results']
    for user in range(len(results)):
        if 'gender' in results[user]:
            sum_users+=1

        
        return sum_users
data = get_data('randomuser_data.json')
print(get_count_users(data))

    






    
    
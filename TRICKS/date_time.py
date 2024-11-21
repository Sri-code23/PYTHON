from datetime import datetime

def get_time() ->str:
    """_summary_

    Returns:
        str: _description_
    """
    now=datetime.now()
    return f'{now:%H:%M:%S}'

print(get_time())
#how to see the current version of a library in python using pip command



"""
CMSC 14100, Autumn 2022
Homework #6

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""
import math
import json

ENCODINGS = ['x', 'y', 'row', 'column']
OPERATIONS = ['filters', 'transforms', 'models']

### Exercise 1
def count_user_events(filename):
    """
    Takes a filename, opens it, and the complex events inside it a list of
    dictionaries.  Makes this data into another dictionary where each user_id
    is the key and the value is the number of complex views that user_id has
    
    Input:
        filename(str): string representing the name of a file
    Output:
        d(dictionary): dictionary with each user_id(str) as a key and
        the number of complex views of each user as a value(int)
    """

    f = open(filename)

    data = json.load(f)
    
    d = {}
    for log in data:
        u = "user_id"
        d[log[u]] = d.get(log[u], 0) + 1
    
    return d


### Exercise 2
def convert_complex_to_simple_event(complex_event):
    """
    Takes a complex event and returns a simple event, which is the variables
    in the encoding key in the vis key.  Only the value associated with the
    field key of each variable should be in the simple event.  It also includes
    any operations.  The keys are the variables and the values is the field
    value.
    
    Input:
        complex_event(dictionary): dictionary with many keys and values that
        are dictionaries as well
        
    Output:
        simple event (dictionary): dictionary with the attributes specified
        above
    """

    d = {key: None for key in ["x", "y", "row", "column", "operations"]}
    d["operations"] = []

    enc = complex_event["vis"]["encoding"]

    for var, items in enc.items():
        f = "field"
        d[var] = items[f]

    fil = complex_event["filters"]

    if fil == True:
        d["operations"].append("filters")

    tra = complex_event["transforms"]

    if tra == True:
        d["operations"].append("transforms")

    mod = complex_event["models"]

    if mod == True:
        d["operations"].append("models")

    return d

### Exercise 3
def load_user_data(filename):
    """
    Takes a filename and returns a new dictionary where the keys are the
    user_ids and the values are a list of the simple events associate with
    that user
    
    Input:
        filename(str): string representing the name of a file
        
    Output:
        d (dictionary): dictionary with details specified above
    """
    
    f = open(filename)

    data = json.load(f)

    keys = []

    for event in data:
        u = "user_id"
        keys.append(event[u])

    d = {key: [] for key in keys}

    for event in data:
        u = "user_id"
        d[event[u]].append(event)

    for user in d:
        for idx, event in enumerate(d[user]):
            d[user][idx] = convert_complex_to_simple_event(event)
    
    return d


def simple_event_to_list(event):
    """
    This is a helper function.  It takes a simple event and returns a list
    of all the variables in that event.

    Input:
        event (dictionary): simple event of the form specified in previous
        exercises
    Output:
        variables (list): list of variables in that simple event
    """

    variables = []
    for val in event:
        if val != "operations":
            variables.append(event[val])

    variables = list(set(variables))

    return variables


### Exercise 4
def count_variable_views_per_user(user_events):
    """
    Takes the dictionary of simple events to users found in exercise 3 and
    makes a new dictionary with the user_id as keys and the number of variable
    views each user has.  Each variable is only counted once per event, even
    if it shows up in more than one encoding.  Does not count operations.
    
    Input:
        user_event (dictionary): dictionary with details specified above
        
    Output:
        final_d (dictionary): dictionary with details specified above
    """

    keys = []
    for user in user_events:
        keys.append(user)

    d = {key: [] for key in keys}
    
    for val in user_events:
        for event in user_events[val]:
            var = simple_event_to_list(event)
            d[val].append(var)

    new_d = {key: [] for key in keys}

    for users, lists in d.items():
        for sublist in lists:
            for value in sublist:
                new_d[users].append(value)

    final_d = {}

    for users in new_d:
        count = {}
        for val in new_d[users]:
            if val != None:
                count[val] = count.get(val, 0) + 1
        final_d[users] = final_d.get(users, count)

    return final_d

    
def simple_event_to_event_complexity(event):
    """
    This is a helper function.  Takes a simple event and returns the number
    of variables viewed plus the number of operations.
    
    Input:
        event (dictionary): simple event
    Output:
        len(variables) (int): number of variables and operations
    """

    variables = []

    for val in event:
        if val != "operations":
            variables.append(event[val])

    variables = list(set(variables))

    for val in event:
        if val == "operations":
            for op in event["operations"]:
                variables.append(op)

    for val in variables:
        if val == None:
            variables.remove(val)

    return len(variables)



### Exercise 5
def most_complex_view_per_user(user_events):
    """
    Takes the dictionary of simple events to users found in exercise 3 and
    makes a new dictionary with the keys as the user_id and the value being
    the simple event with the most complex view ie which simple event
    had the most variable views and operations.
    
    Input:
        user_event (dictionary): dictionary with details specified above
    Output:
        final_d (dictionary): dictionary with details specified above
    """

    keys = []
    for user in user_events:
        keys.append(user)

    d = {key: [] for key in keys}
    
    for val in user_events:
        for event in user_events[val]:
            var = simple_event_to_event_complexity(event)
            d[val].append(var)

    final_d = {}

    for user, list in d.items():
        idx = list.index(max(list))
        final_d[user] = final_d.get(user, idx)

    return final_d


### Exercise 6
def compute_max_gap(user_events, user, variable):
    """
    Takes the dictionary of simple events to users found in exercise 3 and
    a user and a variable returns and the maximum number of events between
    which a variable was viewed.  If the variable is not viewed more than
    once, returns -1
    
    Input:
        user_events: dictionary with details specified above
        user (str): user_id which is a key in user_events
        variable (str): key in the simple event of user
    Output:
        max gap (int): maximum gap between views of variable"""

    events = user_events[user]

    variables = []

    for event in events:
        var = simple_event_to_list(event)
        variables.append(var)

    index = []

    for idx, list in enumerate(variables):
        if variable in list:
            index.append(idx)

    differences = []

    if len(index) == 0:
        differences.append(-1)
    else:
        for i in range(len(index) - 1):
            dif = index[i + 1] - index[i]
            differences.append(dif)
        
    if len(differences) > 0:
        return (max(differences) - 1)
    else:
        return -1
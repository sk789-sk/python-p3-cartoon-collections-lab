def roll_call_dwarves(dwarf_list):
    for idx, val in enumerate(dwarf_list):
        print(f"{idx+1}. {val}")
    pass

def summon_captain_planet(planeteer_call):
    new_list = []
    for val in planeteer_call:
        new_list.append(f"{val.capitalize()}!")
    return new_list

def long_planeteer_calls(calls):
    for val in calls:
        if len(val) > 4:
            return True
    return False

def find_the_cheese(str_list):
    for val in str_list:
        if val in ['cheddar', 'gouda', 'camembert']:
            return val
    return None

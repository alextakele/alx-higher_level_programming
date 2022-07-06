<<<<<<< HEAD
#!/usr/bin/python3i
def best_score(my_dict):
    return max(my_dict) if my_dict else None
=======
#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest = 0
    for key, value in a_dictionary.items():
        if value > biggest:
            biggest = value
    for key, value in a_dictionary.items():
        if value == biggest:
            return key
>>>>>>> 497518a11b6b805fe9cd56d9ccd272fb921ed2b5

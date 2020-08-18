def select_dates(potential_dates):
    people = None
    for names in potential_dates:
        if names['age'] > 30 and 'art' in names['hobbies'] and names['city'] == 'Berlin':
            if people is None:
                people = names['name']
            else:
                people += ", " + names['name']
    return people

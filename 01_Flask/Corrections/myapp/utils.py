

def is_term_exist(term, users):
    for user in users :
        if term in user.values():
            return True
        
    return False
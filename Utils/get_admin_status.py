def get_admin_status(name_str: str):
    split_str = name_str.split('_')
    for elem in split_str:
        if elem == 'admin':
            return True
    return False

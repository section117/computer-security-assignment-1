from config_handler import get_user_by_username, register_user
import hashlib

user_types = ["patient", "staff"]
privilege_levels = ["patient", "pharmacist", "nurse", "doctor", "chemist"]

allowed_actions_for_privilege_levels = {
    "patient": ["View my records", "Add personal details"],
    "pharmacist": ["View all drug prescription", "View drug prescriptions by username"],
    "nurse": ["View all records by username", "Add sickness details"],
    "doctor": ["View all records by username", "Add sickness details", "Add drug prescription",
               "Add lab test prescription"],
    "chemist": ["View all lab test prescriptions", "View lab test prescriptions by username"]
}

read_access_of_records = {
    "patient": ["personal", "sickness", "drugs", "lab"],
    "pharmacist": ["drugs"],
    "nurse": ["personal", "sickness", "drugs", "lab"],
    "doctor": ["personal", "sickness", "drugs", "lab"],
    "chemist": ["lab"],
}

write_access_of_records = {
    "patient": ["personal"],
    "pharmacist": [],
    "nurse": ["sickness"],
    "doctor": ["personal", "sickness", "drugs", "lab"],
    "chemist": [],
}

data_access_sensitivity_levels_for_privilege_levels = {
    "patient": ["low", "medium", "high"],
    "pharmacist": ["low"],
    "nurse": ["low", "medium"],
    "doctor": ["low", "medium", "high"],
    "chemist": ["low"],
}


def hash_string(s):
    return hashlib.md5(s.encode()).hexdigest()


def login(username, password):
    user = get_user_by_username(username)
    if user is None:
        return False

    hashed_password = hash_string(password)
    if hashed_password == user["password"]:
        return user
    else:
        return None


def register(username, password, user_type, priv_level):
    if user_type not in user_types:
        print("Invalid User type.")
        exit()
    if priv_level not in privilege_levels:
        print("Invalid privilege level.")
        exit()

    try:
        user = register_user(username, hash_string(password), user_type, priv_level)
    except:
        print("Username already exists.")
        exit()
    else:
        print("Successfully registered.")
        return user


def check_security_access(user, want_read_access, want_write_access):
    priv_level = user["priv_level"]
    allowed_read_access = read_access_of_records[priv_level]
    allowed_write_access = write_access_of_records[priv_level]

    for wa in want_read_access:
        if wa not in allowed_read_access:
            print("This record is not allowed to read - " + wa)
            return None

    for wa in want_write_access:
        if wa not in allowed_write_access:
            print("This record is not allowed to write - " + wa)
            return None

    return data_access_sensitivity_levels_for_privilege_levels[priv_level]

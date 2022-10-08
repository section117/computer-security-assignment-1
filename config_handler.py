import json
from json import JSONDecodeError


def get_file(mode):
    file = open("./files/config.data", mode)
    return file


def decode_record(record):
    try:
        return json.loads(record)
    except JSONDecodeError:
        raise Exception("Invalid config file")


def read_all_users():
    all_users = {}
    file = get_file("r")
    try:
        for line in file:
            user = decode_record(line)
            if not user["username"] in all_users:
                all_users[user["username"]] = user
    except:
        return {}
    finally:
        file.close()

    print(all_users)
    return all_users


def get_user_by_username(username):
    file = get_file("r")
    try:
        for line in file:
            user = decode_record(line)
            if user["username"] == username:
                return user
    except:
        return None
    finally:
        file.close()

    return None


def register_user(username, password, user_type, priv_level):
    if get_user_by_username(username) is not None:
        raise Exception("Username already exists")

    user = {
        "username": username,
        "password": password,
        "user_type": user_type,
        "priv_level": priv_level
    }
    encoded_user = json.dumps(user)
    file = get_file("a")
    file.write(encoded_user + "\n")
    file.close()

    return user

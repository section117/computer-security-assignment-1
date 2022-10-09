import auth_hanlder
import print_helper
import security_layer


def handle_login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    user_obj = auth_hanlder.login(username, password)
    if user_obj is None:
        print("Wrong credentials!")
        exit()
    print("Hello " + user_obj["username"] + ",")
    return user_obj


def handle_register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user_type = input("Enter your type (patient or staff): ")
    priv_level = input("Enter your password (patient, pharmacist, nurse, doctor or chemist): ")

    return auth_hanlder.register(username, password, user_type, priv_level)


if __name__ == '__main__':
    print("Welcome!\nEnter 1 to Login\nEnter 2 to Register")

    main_action = input("Enter your action: ")
    user = None
    if main_action == "1":
        user = handle_login()
    else:
        user = handle_register()

    allowed_actions = auth_hanlder.allowed_actions_for_privilege_levels[user["priv_level"]]

    while True:
        action_id = print_helper.print_actions_for_user_and_get_action(allowed_actions)
        if action_id < 0:
            print("Invalid action")
            exit()
        action_name = allowed_actions[action_id]
        print(action_name)
        security_layer.execute_action(action_name, user)

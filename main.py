import data_handler
import auth_hanlder
import print_helper

from datetime import date


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


def view_my_records(username):
    all_records = data_handler.read_all_records_by_username(username)
    print_helper.pretty_print(all_records)


def view_all_drug_prescriptions():
    drug_records = data_handler.read_all_records("drugs")
    print_helper.pretty_print(drug_records)


def view_drug_prescriptions_by_username():
    un = input("Enter the username of patient: ")
    all_records = data_handler.read_all_records_by_username(un, "drugs")
    print_helper.pretty_print(all_records)


def view_all_lab_test_prescriptions():
    drug_records = data_handler.read_all_records("lab")
    print_helper.pretty_print(drug_records)


def view_lab_test_prescriptions_by_username():
    un = input("Enter the username of patient: ")
    all_records = data_handler.read_all_records_by_username(un, "lab")
    print_helper.pretty_print(all_records)


def view_all_records_by_username():
    un = input("Enter the username of patient: ")
    all_records = data_handler.read_all_records_by_username(un)
    print_helper.pretty_print(all_records)


def add_sickness_details():
    patient_id = input("Enter patient's username: ")
    sickness = input("Enter sickness: ")
    symptoms = input("Enter symptoms: ")
    data_handler.add_sickness_details(patient_id, sickness, symptoms, str(date.today()))


def add_drug_prescription():
    patient_id = input("Enter patient's username: ")
    drugs = input("Enter drugs (as a comma separated string): ")
    data_handler.add_drug_prescription(patient_id, drugs.split(","), str(date.today()))


def add_lab_test_prescription():
    patient_id = input("Enter patient's username: ")
    test_name = input("Enter test name: ")
    data_handler.add_lab_test_prescription(patient_id, test_name, str(date.today()))


if __name__ == '__main__':
    print("Welcome!\nEnter 1 to Login\nEnter 2 to Register")

    main_action = input("Enter your action: ")
    user = None
    if main_action == "1":
        user = handle_login()
    else:
        user = handle_register()

    allowed_actions = auth_hanlder.allowed_actions_for_privilege_levels[user["priv_level"]]
    action_id = print_helper.print_actions_for_user_and_get_action(allowed_actions)
    if action_id < 0:
        print("Invalid action")
        exit()
    action_name = allowed_actions[action_id]
    print(action_name)
    match action_name:
        case "View my records":
            view_my_records(user["username"])
        case "View all drug prescription":
            view_all_drug_prescriptions()
        case "View drug prescriptions by username":
            view_drug_prescriptions_by_username()
        case "View all records by username":
            view_all_records_by_username()
        case "Add sickness details":
            add_sickness_details()
        case "Add drug prescription":
            add_drug_prescription()
        case "Add lab test prescription":
            add_lab_test_prescription()
        case "View all lab test prescriptions":
            view_all_lab_test_prescriptions()
        case "View lab test prescriptions by username":
            view_lab_test_prescriptions_by_username()
        case default:
            print("Invalid action")

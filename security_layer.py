import data_handler
import auth_hanlder
import print_helper

from datetime import date


def view_my_records(username, sensitivty_levels):
    all_records = data_handler.read_all_records_by_username(username=username, sensitivity_levels=sensitivty_levels)
    print_helper.pretty_print(all_records)


def view_all_drug_prescriptions(sensitivty_levels):
    drug_records = data_handler.read_all_records("drugs", sensitivty_levels)
    print_helper.pretty_print(drug_records)


def view_drug_prescriptions_by_username(sensitivty_levels):
    un = input("Enter the username of patient: ")
    all_records = data_handler.read_all_records_by_username(un, "drugs", sensitivty_levels)
    print_helper.pretty_print(all_records)


def view_all_lab_test_prescriptions(sensitivty_levels):
    drug_records = data_handler.read_all_records("lab", sensitivty_levels)
    print_helper.pretty_print(drug_records)


def view_lab_test_prescriptions_by_username(sensitivty_levels):
    un = input("Enter the username of patient: ")
    all_records = data_handler.read_all_records_by_username(un, "lab", sensitivty_levels)
    print_helper.pretty_print(all_records)


def view_all_records_by_username(sensitivty_levels):
    un = input("Enter the username of patient: ")
    all_records = data_handler.read_all_records_by_username(username=un, sensitivity_levels=sensitivty_levels)
    print_helper.pretty_print(all_records)


def add_personal_details(username):
    address = input("Enter address: ")
    phone = input("Enter phone: ")
    sl = get_sensitivity_level_from_input()
    data_handler.add_personal_details(username, sl, address, phone)


def add_sickness_details():
    patient_id = input("Enter patient's username: ")
    sickness = input("Enter sickness: ")
    symptoms = input("Enter symptoms: ")
    sl = get_sensitivity_level_from_input()
    data_handler.add_sickness_details(patient_id, sl, sickness, symptoms, str(date.today()))


def add_drug_prescription():
    patient_id = input("Enter patient's username: ")
    drugs = input("Enter drugs (as a comma separated string): ")
    sl = get_sensitivity_level_from_input()
    data_handler.add_drug_prescription(patient_id, sl, drugs.split(","), str(date.today()))


def add_lab_test_prescription():
    patient_id = input("Enter patient's username: ")
    test_name = input("Enter test name: ")
    sl = get_sensitivity_level_from_input()
    data_handler.add_lab_test_prescription(patient_id, sl, test_name, str(date.today()))


def get_sensitivity_level_from_input():
    levels = ["low", "medium", "high"]
    print("Select the desired sensitivity level. \n1) low \n2) medium \n3)high")
    while (True):
        sl = input("Enter the desired sensitivity level number: ")
        try:
            sl = int(sl)
            if sl < 1 or sl > 3:
                raise Exception("Invalid level.")
            return levels[sl - 1]
        except:
            print("Invalid level. Try again.")


def secure_action(user, want_read_access, want_write_access):
    sense_levels = auth_hanlder.check_security_access(user, want_read_access, want_write_access)
    if sense_levels is None:
        print("Not sufficient permissions")
        exit()
    print("Allowed sensitivity levels are " + str(sense_levels))

    return sense_levels


def execute_action(action_name, user):
    match action_name:
        case "View my records":
            sense_levels = secure_action(user, ["personal", "sickness", "drugs", "lab"], [])
            view_my_records(user["username"], sense_levels)
        case "Add personal details":
            sense_levels = secure_action(user, [], ["personal"])
            add_personal_details(user["username"])
        case "View all drug prescription":
            sense_levels = secure_action(user, ["drugs"], [])
            view_all_drug_prescriptions(sense_levels)
        case "View drug prescriptions by username":
            sense_levels = secure_action(user, ["drugs"], [])
            view_drug_prescriptions_by_username(sense_levels)
        case "View all records by username":
            sense_levels = secure_action(user, ["personal", "sickness", "drugs", "lab"], [])
            view_all_records_by_username(sense_levels)
        case "Add sickness details":
            sense_levels = secure_action(user, [], ["sickness"])
            add_sickness_details()
        case "Add drug prescription":
            sense_levels = secure_action(user, [], ["drugs"])
            add_drug_prescription()
        case "Add lab test prescription":
            sense_levels = secure_action(user, [], ["lab"])
            add_lab_test_prescription()
        case "View all lab test prescriptions":
            sense_levels = secure_action(user, ["lab"], [])
            view_all_lab_test_prescriptions(sense_levels)
        case "View lab test prescriptions by username":
            sense_levels = secure_action(user, ["lab"], [])
            view_lab_test_prescriptions_by_username(sense_levels)
        case default:
            print("Invalid action")

def print_actions_for_user_and_get_action(all_actions):
    print("Please select an action to continue")
    i = 1
    for a in all_actions:
        print(str(i) + " - " + a)
        i += 1
    try:
        action_id = int(input())
        if action_id > len(all_actions):
            return -1
        return action_id - 1
    except:
        return -1


def pretty_print(records):
    for r in records:
        print("patient Name - " + r["patient_username"])
        p = r["payload"]
        match r["type"]:
            case "personal":
                print("Personal record: \nAddress - " + p["address"] + "\nPhone No - " + p["phone"] + "\n")
            case "sickness":
                print("Sickness Record: \nSickness - " + p["sickness"] + "\nSymptoms - " + p["symptoms"] + "\nDate - " + p[
                    "date"] + "\n")
            case "drugs":
                print("Drug prescription record: \nDrugs - " + ", ".join(p["drugs"]) + "\nDate - " + p["date"] + "\n")
            case "lab":
                print("Lab test prescription record \nTest name - " + p["test_name"] + "\nDate - " + p["date"] + "\n")
            case default:
                print("Unknown record!")

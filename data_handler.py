import json
from json import JSONDecodeError


def get_file(mode):
    file = open("./files/data.data", mode)
    return file


def decode_record(record):
    try:
        return json.loads(record)
    except JSONDecodeError:
        raise Exception("Invalid data file")


def read_all_records(filter_type=None):
    all_records = []
    file = get_file("r")
    try:
        for line in file:
            r = decode_record(line)
            if filter_type is None or filter_type == r["type"]:
                all_records.append(r)
    except:
        return []
    finally:
        file.close()

    return all_records


def read_all_records_by_username(username, filter_type=None):
    all_records = []
    file = get_file("r")
    try:
        for line in file:
            r = decode_record(line)
            if r["patient_username"] == username:
                if filter_type is None or filter_type == r["type"]:
                    all_records.append(r)
    except:
        return []
    finally:
        file.close()

    return all_records


def write_a_record(sensitivity_level, patient_id, record_type, payload):
    w = {
        "sens_level": sensitivity_level,
        "patient_username": patient_id,
        "type": record_type,
        "payload": payload
    }
    ww = json.dumps(w)

    file = get_file("a")
    file.write(ww + "\n")
    file.close()


def add_personal_details(patient_id, address, phone):
    payload = {
        "address": address,
        "phone": phone
    }
    write_a_record("high", patient_id, "personal", payload)


def add_sickness_details(patient_id, sickness, symptoms, date):
    payload = {
        "sickness": sickness,
        "symptoms": symptoms,
        "date": date
    }
    write_a_record("medium", patient_id, "sickness", payload)


def add_drug_prescription(patient_id, drugs_list, date):
    payload = {
        "drugs": drugs_list,
        "date": date
    }
    write_a_record("medium", patient_id, "drugs", payload)


def add_lab_test_prescription(patient_id, test_name, date):
    payload = {
        "test_name": test_name,
        "date": date
    }
    write_a_record("medium", patient_id, "lab", payload)

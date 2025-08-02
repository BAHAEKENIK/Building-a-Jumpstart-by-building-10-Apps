import os


def load(name):
    # TODO: populate from file if it exists.
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print("....... saving to: {}".format(filename))
    with open(filename, "w", encoding="utf-8") as fout:
        for entry in journal_data:
            fout.write(entry + "\n")


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join("./journals/", name + ".jrl"))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)

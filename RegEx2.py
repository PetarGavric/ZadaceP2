import re

def provjeri_email(email):
    regex_email = r'^[a-zA-Z0-9._%+-]+?@[a-zA-Z0-9.-]+?\.(sum\.ba)$'
    if re.match(regex_email, email):
        return True
    else:
        return False

def provjeri_eduid(eduid):
    regex_eduid = r'^i[a-zA-Z]+?[0-9]*?@sum\.ba$'
    if re.match(regex_eduid, eduid):
        return True
    else:
        return False

def main():
    email = input("Unesite e-mail: ")
    eduid = input("Unesite eduId: ")

    if provjeri_email(email):
        print("E-mail je ispravan.")
    else:
        print("E-mail nije ispravan.")

    if provjeri_eduid(eduid):
        print("EduId je ispravan.")
    else:
        print("EduId nije ispravan.")

if __name__ == "__main__":
    main()

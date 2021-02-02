import io
import json
import quopri



file_location = input("Please enter your telegram json location:\n")

contact_file = io.open(file_location, 'r', encoding='utf-8')

contact_raw = ''.join(contact_file.readlines())

contact_file.close()

contacts_dict = json.loads(contact_raw)['contacts']['list']
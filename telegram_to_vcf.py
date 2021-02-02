import io


file_location = input("Please enter your telegram json location:\n")

contact_file = io.open(file_location, 'r', encoding='utf-8')

contact_raw = ''.join(contact_file.readlines())

contact_file.close()
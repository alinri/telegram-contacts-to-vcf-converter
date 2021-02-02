import io
import json
import quopri
from os import path


def decode_quoted(name: str):
    return quopri.encodestring(name.encode('utf-8')).decode('utf-8')

file_location = input("Please enter your telegram json location:\n")

contact_file = io.open(file_location, 'r', encoding='utf-8')

contact_raw = ''.join(contact_file.readlines())

contact_file.close()

contacts_dict = json.loads(contact_raw)['contacts']['list']

result_vcf = io.open('result.vcf', 'w', encoding='utf-8')

for contact in contacts_dict:
    result_vcf.write('BEGIN:VCARD\n')
    result_vcf.write('VERSION:2.1\n')
    result_vcf.write(f'N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:{decode_quoted(contact["last_name"])};{decode_quoted(contact["first_name"])};;;\n')
    result_vcf.write(f'FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:{decode_quoted(contact["first_name"])} {decode_quoted(contact["last_name"])}\n')
    result_vcf.write(f'TEL;CELL:{contact["phone_number"]}\n')
    result_vcf.write('END:VCARD\n')

result_vcf.close()
print('done')
print(f'Your vcf file Stored in in {path.dirname(__file__)+path.sep}result.vcp')
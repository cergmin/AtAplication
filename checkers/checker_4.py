import sys
import json
from os import path

output_data = {
    'verdict': 'NP',
    'console_output': ''
}

inp, out, file_path = sys.argv[1:4]

file_name = path.split(file_path)[1]
module_name = file_name[:-3] + file_name[-3:].replace('.py', '')

exec('from ' + module_name + ' import *')

try:
    sol_out = eval(inp.encode(encoding='windows-1251'))

    if str(out).strip() == str(sol_out).strip():
        output_data['verdict'] = 'OK'
        output_data['console_output'] = str(sol_out).strip()
    else:
        output_data['verdict'] = 'WA'
        output_data['console_output'] = str(sol_out).strip()
except Exception as E:
    output_data['verdict'] = 'RE'
    output_data['console_output'] = str(E)

print(json.dumps(output_data))
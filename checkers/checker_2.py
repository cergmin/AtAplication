import sys
import json
import subprocess
from os import path, remove

output_data = {
    'verdict': 'NP',
    'console_output': ''
}

inp, out, file_path = sys.argv[1:4]

out_data = ''
out_filename = path.split(out)[1]

with open(out, 'r') as f:
    out_data = f.read()

process = subprocess.Popen(
    [
        sys.executable, 
        file_path
    ],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
process.stdin.write(inp.encode(encoding='windows-1251'))
sol_out, sol_error = process.communicate()

if not path.exists(out_filename):
    output_data['verdict'] = 'PE'
    output_data['console_output'] = sol_out.strip().decode('windows-1251')
    output_data['console_output'] += '\n\n---[ error ]---\n'
    output_data['console_output'] += '\nФайл "' + out_filename + '" не существует'
else:
    sol_data = ''
    with open(out_filename, 'r') as f:
        sol_data = f.read()
    
    remove(out_filename)
    
    output_data['console_output'] = sol_data + '\n\n'

    if sol_error != b'':
        output_data['verdict'] = 'RE'
        output_data['console_output'] = sol_error.strip().decode('windows-1251')
    elif str(out_data.strip()) == str(sol_data.strip()):
        output_data['verdict'] = 'OK'
        output_data['console_output'] = sol_out.strip().decode('windows-1251')
        output_data['console_output'] += '\n\n'
        output_data['console_output'] += '---[ ' + str(out_filename) + ' ]---\n'
        output_data['console_output'] += str(sol_data)
    else:
        output_data['verdict'] = 'WA'
        output_data['console_output'] = sol_out.strip().decode('windows-1251')
        output_data['console_output'] += '\n\n'
        output_data['console_output'] += '---[ ' + str(out_filename) + ' ]---\n'
        output_data['console_output'] += str(sol_data)

print(json.dumps(output_data))
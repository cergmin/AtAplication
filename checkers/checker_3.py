import sys
import json
import subprocess

output_data = {
    'verdict': 'NP',
    'console_output': ''
}

inp, out, file_path = sys.argv[1:4]

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

if out.encode('windows-1251').strip() in sol_error.strip():
    output_data['verdict'] = 'OK'
    output_data['console_output'] = sol_out.strip().decode('windows-1251')
    output_data['console_output'] += '\n\n'
    output_data['console_output'] += sol_error.strip().decode('windows-1251')
else:
    output_data['verdict'] = 'WA'
    output_data['console_output'] = sol_out.strip().decode('windows-1251')
    output_data['console_output'] += '\n\n'
    output_data['console_output'] += sol_error.strip().decode('windows-1251')

print(json.dumps(output_data))
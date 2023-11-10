import os
import subprocess
import sys

python_interpreter = sys.executable

venv_name = 'venv'
venv_path = './' + venv_name
path = './'

if sys.platform == 'win32':
    python_interpreter = os.path.join(venv_path, 'Scripts/python.exe')
    pip_path = os.path.join(venv_path, 'Scripts/pip.exe')
else:
    python_interpreter = os.path.join(venv_path, 'bin/python')
    pip_path = os.path.join(venv_path, 'bin/pip')

subprocess.check_call([sys.executable, '-m', 'venv', venv_path])

subprocess.check_call([pip_path, 'install', '-r', os.path.join(path, 'requirements.txt')])


subprocess.check_call([python_interpreter, 'db.py'])


print("Установка завершена")

subprocess.check_call([python_interpreter, 'bot.py'])

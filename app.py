import os
import datetime
import subprocess
import platform
from flask import Flask

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Venkatesh V" 
    username = os.getenv("USER", os.getenv("USERNAME", "codespace"))  
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30) 

    if platform.system() == "Windows":
        top_output = subprocess.getoutput("wmic process get ProcessId,CommandLine,WorkingSetSize")
    else:
        top_output = subprocess.getoutput("top -b -n 1 | head -20")

    return f"""
    <pre>
    Name: {name}
    user: {username}

    Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S.%f')}

    TOP output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

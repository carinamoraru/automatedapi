import shlex
import subprocess
import json

def call_curl(curl):
    args = shlex.split(curl)
    process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return json.loads(stdout.decode('utf-8'))


curl = '''curl -L -X
POST 'https://demo-api-capital.backend-capital.com/' \
-H 'X-CAP-API-KEY: 5EFyhzf6jExtdIRi' \
-H 'Content-Type: application/json' \
--data-raw '{
"encryptedPassword": "false" 
"identifier": "baberoad@gmail.com",
 "password": "010191Qqzbbmm$"
}' '''
output = call_curl(curl)
print(output)


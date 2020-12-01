import requests,json
while True:
 r = requests.post('http://api.guerrillamail.com/ajax.php?f=get_email_address&ip=127.0.0.1&agent=Mozilla_foo_bar')
 print(r.text)
 mail = r.json()['email_addr']
 payload={'email':mail,'password':'burgernamedmecool'}
 r = requests.post('https://json.psty.io/signup',payload)
 print(r.text)
 a=open('a.txt','a')
 a.write('\n'+payload.rjson()['username'])

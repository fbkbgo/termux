import os, getpass, sys
from time import sleep

arquivo = 'password.txt'

if os.path.isfile(arquivo):
	with open(arquivo, 'r') as arq:
		password = ''
		p = arq.read()
		while True:
			try:
				password = getpass.getpass('\n\033[7mPASSWORD:\033[m ', sys.stdout)
			except (KeyboardInterrupt, EOFError):
				print('\n\033[33m You are not allowed to interrupt the password.\033[m')
			if password == p:
				os.system('clear')
				print('''



                  \033[1;32m ACCESS ALLOWED!\033[m''')
				sleep(2)
				os.system('clear')
				break
			elif password != p and password != '':
				print('\n\033[31m Incorrect password!\033[m\n')

else:
	with open(arquivo, 'w') as arq:
		while True:
			password = input('\n\033[7m Type your password  :\033[m ')
			repete = input('\033[7m Repeat your password:\033[m ')
			if password == repete:
				arq.write(password)
				print('\n\033[32m Password saved successfully!\033[m')
				break
			else:
				print('\n\033[31m Passwords entered are not the same!\n Try again.\033[m\n')

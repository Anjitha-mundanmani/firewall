import os

def menu():
	print("1.Get firewall status")
	print("2.Set firewall rules")
	print("3.Delete rules")
	print("4.Reload rules")

def rules_menu()
	print("\t\t1.Enable firewall")
	print("\t\t2.Disable firewall")
	print("\t\t3.Block host/IP")
	print("\t\t4.Allow host/IP")
	print("\t\t5.Check rules")
	print("\t\t6.Exit")
	
def rules():
	rules_menu()
	choice = input("Enter your choice")
	if ch == '1':
		command = 'sudo ufw enable'
		result = os.popen(command).read()
		print(result)
	elif ch == '2':
		command = 'sudo ufw disable'
		result = os.popen(command).read()
		print(result)
	elif ch == '3':
		ip = input("Enter the IP to block")
		command = f'sudo ufw deny from {ip}'
		result = os.popen(command).read()
		print(result)
	elif ch == '4'
		ip = input("Enter the IP to block")
		command = f'sudo ufw allow from {ip}'
		result = os.popen(command).read()
		print(result)
	elif ch == '5':
		command = 'sudo ufw status numbered'
		result = os.popen(command).read()
		print(result)
	elif ch == '6':
		break
	else:
		print("Invalid input")	
def delete_rules():
	command = 'sudo ufw status numbered'
	result = os.popen(command).read()
	print(result)
	indx = input("Enter the index number of the rule to be deleted :  ")
	command = f'sudo ufw delete {indx}'
	result = os.popen(command).read()
	print(result)
while True:
	menu()
	ch = input("Enter your choice")
	if ch == '1':
		command = 'sudo ufw status'
		result = os.popen(command).read()
		print(result)
	elif ch == '2':
		rules()
	elif ch == '3':
		delete_rules()
	elif ch == '4':
		command = 'sudo ufw reload'
		result = os.popen(command).read()
		print(result)
	elif ch == '5':
		break
	else:
		print("Invalid input")
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

import os
from rich.console import Console
from rich.text import Text
console = Console()


def rich_func(res):
    console.print(Text(res, style="bold blue"))


def Status_of_firewall():
    ram = os.popen("sudo ufw status").read()
    rich_func(ram)


def Delete_rules():
    res = os.popen("sudo ufw status numbered").read()
    rich_func(res)
    index = input("Enter the index number of the rule to be deleted :  ")
    res1 = os.popen(f"sudo ufw delete {index}").read()
    rich_func(res1)


def Reload_rules():
    res = os.popen("sudo ufw reload").read()
    rich_func(res)


def rule_menu():

    console.print("1.Disable firewall", style="bold cyan")
    console.print("2.Block the Host IP", style="bold cyan")
    console.print("3.Alow the Host IP", style="bold cyan")
    console.print("4.Alow Port", style="bold cyan")
    console.print("5.Block Port", style="bold cyan")
    console.print("6.Alow a subnet", style="bold cyan")
    console.print("7.Get Firewall app list", style="bold cyan")
    console.print("8.Show Rules Added", style="bold cyan")
    console.print("9.Exit", style="bold cyan")


def activate_ufw():
    res = os.popen("sudo ufw enable").read()
    result = print(res)
    return result


def Exit():
    console.print("Successfully Exited",style="bold green")
    exit()


def set_rules():
	rule_menu()
	ch = input("Enter your choice")
	if ch == '1':
		res = os.popen("sudo ufw disable").read()
		rich_func(res)

	elif ch == '2':
		ip = input("Enter the IP to block : ")
		print(ip)
		res = os.popen(f"sudo ufw deny from {ip}").read()
		rich_func(res)

	elif ch == '3':
		ip = input("Enter the IP to allow")
		res = os.popen(f"sudo ufw allow from {ip}").read()
		rich_func(res)

	elif ch == '4':
		port = input("Enter the Port Number to allow: ")
		res = os.popen(f"sudo ufw allow {port}").read()
		rich_func(res)

	elif ch == '5':
		port = input("Enter the Port Number to block")
		res = os.popen(f"sudo ufw deny {port}").read()
		rich_func(res)

	elif ch == '6':
		subnet = input("Enter the subnet to allow")
		res = os.popen(f"sudo ufw allow from {subnet}").read()
		rich_func(res)

	elif ch == '7':
		res = os.popen("sudo ufw app list").read()
		rich_func(res)
        	
	elif ch == '8':
		res = os.popen("sudo ufw status numbered").read()
		rich_func(res)
        	
	elif ch == '9':
		exit()


def main_menu():
    console.print("1.Status of firewall", style="bold cyan")
    console.print("2.Set Rules", style="bold cyan")
    console.print("3.Delete Rules", style="bold cyan")
    console.print("4.Reload Rules", style="bold cyan")
    console.print("5.Exit", style="bold cyan")


operations = {
    "1": Status_of_firewall,
    "2": set_rules,
    "3": Delete_rules,
    "4": Reload_rules,
    "5": Exit
}

while True:
    main_menu()
    choice = input("Enter Choice: ")
    activate_ufw()
    operations[choice]()

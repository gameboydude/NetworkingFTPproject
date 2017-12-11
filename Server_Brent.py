"Gold Team"
"Brent Greenwald and Ben Strong"
"FTP"
"CSC 311"

#to use code run in cmd "telnet localhost" then run code
import socket
import os

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
argumants = {}
#host = '10.20.148.229'
host = '0.0.0.0'
#Login stuff. Will be added to it's own .py file for decluttering
password1 = 'bks1324@jagmail.southalabama.edu'
password2 = 'beg1321@jagmail.southalabama.edu'


good_login = "ACCESS GRANTED"


lets_go=True

# create and bind server socket
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host, and a well-known port
try:
	s.bind((host, 4000))
except socket.error as e:
	print(str(e))

# become a server socket
s.listen(5)
conn,addr = s.accept()
def finished():
	conn.send("done".encode())

def valid_login(password):
#Reads password info. checks to see that the user input is valid. If password ==True, function returns true.
	if  password == '12':#'beg1321@jagmail.southalabama.edu':#password1 or password2:
		print("Access GRANTED")
		return True
	else:
		print("Access DENIED")
		return False

def login():
#Allows user to input password. Info fed into valid_login(pass). If valid_login == true, it breaks + allows user access
	while True:
		#clientsocket.send("Password: ".encode())
		conn.send("Password: ".encode())
		#password = clientsocket.recv(1024)
		password = conn.recv(1024)
		if valid_login(password) == True:
			conn.send(good_login.encode())
			#conn.send("What would you like to do?".encode())
			#clientsocket.send(good_login.encode())
			#clientsocket.send("What woudld you like to do?".encode())
			break


def ls():
	directory_contents = os.listdir(directory)
	directory_contents = '\n'.join(directory_contents)
	conn.send("print")
	conn.send(str(directory_contents).encode())
	conn.send("Q")
	

def dir():
	directory_contents = os.listdir(directory)
	directory_contents = '\n'.join(directory_contents)
	conn.send("print")
	conn.send(str(directory_contents).encode())
	conn.send("Q")

"""`````````````````````````````````````````````````````````````````````````````````````````````````````````"""
"""WHAT BEN STRONG EDITED ON THANKSGIVING"""
def put(): 								#http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
#	conn, addr = s.accept()
#	data = conn.recv(1024)
	singleFile = 'Fellowship.txt' #file.txt is what is referred to in client...
	file = open(singleFile, 'rb')
	putDo = file.read(1024)

	while(putDo):
		conn.send(putDo)
		print(repr(putDo), 'has been sent to the client.')
		putDo = file.read(1024)
	file.close()

	print('Done didly did, Homer."')
	conn.send('Thanks for doing the thing. Have a nice day.')
	conn.close()


def mput():		#https://gist.github.com/ericksond/10304575
#	conn, addr = s.accept()
#	data = conn.recv(1024)


	"""````````````````````````````````````````````````````````````````````````````````````````````````````````"""
	
def cd():
	global directory
	global root_directory
	conn.send("in")
	conn.send("Type in the name of a folder (include \\folderName)".encode())

	path_name = conn.recv(1024).decode()
	new_directory = directory

	if path_name[0] == "r" and path_name[1] == "o" and path_name[2] == "o" and path_name[3] == "t":
		directory = root_directory
		print(len(path_name))
		if len(path_name) > 4:
			for x in range(4, len(path_name)):
				new_directory += path_name[x]
				print(path_name[x])
			directory = new_directory
			print(directory)
		else:
			directory = root_directory

	new_directory = directory + path_name

	if os.path.exists(new_directory):
		directory = new_directory
		conn.send("Q")
		
	else:
		conn.send("print")
		conn.send("That directory path does not exist.".encode())
		conn.send("Q")
def handler(data):
	command = data.split()
	#conn.send("Ok")
	
	for key in commands:
		if key == command[0]:
			print(key)
			commands[key]()
    

commands = {"ls":ls, "dir":dir, "cd":cd} #"get":get, "mget":mget, "mput":mput,"put":put}


print ('Got connected to: '+addr[0]+':'+str(addr[1]))
#shows sucessfull connection
login()
directory = os.getcwd()

#time to be a server
while True:
	data = conn.recv(1024).decode()
	if data !="":
		handler(data)


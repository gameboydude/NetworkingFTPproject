"Gold Team"
"Brent Greenwald and Ben Strong"
"FTP"
"CSC 311"

"`````````````````````````````````````````````````````````````````````````````````"
import socket, os, gzip, re, glob, select
                                                        #https://docs.python.org/2/library/gzip.html
not_logged_in = True
reciving = True


port = 4000
host = 'localhost'
#host = '10.20.123.251'
"""BenStrong laptop: 10.20.148.229"""
                                                        #error picking out whether to have s or server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#login
#login_counter = 0;
def login():
	not_logged_in = True
	while not_logged_in == True:
		#print ('Connecting\n')
		data = server.recv(1024).decode()
		if data.decode() =="Password: ":
			password = raw_input("Enter password:")
			server.send(password.encode())
			
		# if the decoded data equals ACCESS GRANTED
		elif data.decode() == "ACCESS GRANTED":
			not_logged_in = False
			print('Access GRANTED')
			
			

		else:# data.decode() == "ACCESS DENIED":
			not_logged_in = True
			print('true')
	print("1")
			
	#        login_counter+1
	#        if login_counter == 5:
	#          print("You used up your tries!!")
	#        return
	#    else:
	#		login()
def reciving():
	check = True
	print("a")
	while check == True:
		print("b")
		try:
			print("c")
			data = server.recv(1024)
			print(data)
			#message = input(": ").strip()
		except:
			print("d")
			check = False
	#Send the entered command
	s.send(message.encode())  					#HEY_HEY!!! I think s should be server
	#Execute the get command
	data = s.recv(1024)
	handler(message)
		#if data == "done":
		#	print('woot')
		#	check = False
	
		#print(data.decode())
	#while reciving == True:
		#try:
		#	data = s.recv(1024)
		#if data != "":
		#	reciving = False
		#	return(data.decode())
		#else:
		#	reciving = True


while True:
	try:
		print ('Connecting')
		server.connect((host,port))
		break
	except:
		print ("server not found")
		
login()
print('2')
while True: #reciving == True:
	data = "l"
	print("3")
	user_input = str(raw_input('Enter a command:\n>> '))	
	input_array = user_input.split()
	server.sendall(user_input)
	while data != 'Q':
		data = server.recv(1024)
		if data == 'in':
			data = server.recv(1024)
			print(data)
			resp_input = raw_input('>>')
			server.send(resp_input.encode())
		elif data == 'print':
			data = server.recv(1024)
			print(data)
		
			
		#print('3')
		#Recieved and print any sent data
		#data = server.recv(1024)
		#print('4')
		#print(data.decode())
		#Error check to ensure something is entered
		#while True :
		#	print('5')
		#	try:
		#		print('6')
		#		message = input(": ").strip()
		#	except:
		#		break

		#Send the entered command
		#server.send(message.encode())
		#Execute the get command
		#data = server.recv(1024)

            
s.close() 

#while True: #reciving == True:
#	print("3")
#	user_input = str(raw_input('Enter a command:\n>> '))	
#	input_array = user_input.split()
#	server.sendall(user_input)
#	print(reciving())

# def compr_decompr():
    # choice = raw_input('is it compress or decompress? :')
    # if (choice == "compress"):
        # content = "insert som type of data here"
        # compress(content)
        # if compress(content) == True:
	        # print('It Worked!!!')
        # else:
            # print('ERROR. IT DID NOT WORK')
    # if(choice == "decompress"):
        # file = raw_input('enter file name :')
        # print(decompress(file))
    # else:
        # print ('Invalid Choice...')

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WHAT BEN STRONG DID ON THANKSGIVING~~~~~~~~~~~~~~~~~~~~~~~~~~"""

def get():    #http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
	with gzip.decompress('file.txt.gz', 'wb') as f:
		print('File opened')
		while True:
			print('...Getting that data...')
			data = server.recv(1024)
			print('data=%s', (data))
			if not data:
				break

			f.write(data)
	f.close()
	print('Objective complete. File recieved')
	server.close()

def mget(): 	#https://gist.github.com/ericksond/10304575


	"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WHAT BEN STRONG DID ON THANKSGIVING~~~~~~~~~~~~~~~~~~~~~~~~~~"""

def compress(content):
	with gzip.open('file.txt.gz','wb') as f:
		f.write(content)
		return(True)
def decompress (file):
	with gzip.open(file+'.txt.gz','rb') as f:
		file_content = f.read()
		return (file_content)
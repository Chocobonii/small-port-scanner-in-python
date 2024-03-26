import socket;

nmap = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

host = input('input host:');
maxport = int(input('enter max port:'));

nullbytes = '\x00\x00\x00\x00';

closed = 0;
has_failed = False;
index = 1
while index < maxport:
	try:
		nmap.connect((host, index));
	except Exception as err:
		# print ('closed', index)
		has_failed = True;
	if has_failed:
		# print ('closed: ', index);
		closed +=1;
	else:
		print ('open port', index)
		nmap.send(bytes(nullbytes.encode('utf-8')));
		print(nmap.recv(1024));
	has_failed = False;
	# nmap.disconnect()
	index += 1
print ('closed ports: ', closed)
print ('scanning complete')

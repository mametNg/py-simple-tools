
# IP Forwarding

IP Forwarding is a mechanism for forwarding packets originating from one network to another different network

![App Screenshot](https://raw.githubusercontent.com/mametNg/py-simple-tools/main/ip-forwarding/logic.png)



# How to use
Start the application

Open folder compile.

For 64 bit
```bash
  app.exe --listen-host 10.83.40.60 --listen-port 5000 --connect-host 10.83.44.81 --connect-port 5000
```

For 32 bit
```bash
  appx86.exe --listen-host 10.83.40.60 --listen-port 5000 --connect-host 10.83.44.81 --connect-port 5000
```

For script
```bash
  python app.py --listen-host 10.83.42.198 --listen-port 22 --connect-host 200.1.1.135 --connect-port 8888
```

Result
```bash
  	13:35:06 - app.py:68 - INFO: Server started ('200.1.1.135', 8888)
	13:35:06 - app.py:69 - INFO: Connect to ('200.1.1.135', 8888) to get the content of ('10.83.42.198', 22)
	13:35:15 - app.py:72 - INFO: [Establishing] ('200.1.1.115', 51916) -> ('200.1.1.135', 8888) -> ? -> ('10.83.42.198', 22)
	13:35:15 - app.py:76 - INFO: [OK] ('200.1.1.115', 51916) -> ('200.1.1.135', 8888) -> ('10.83.41.66', 3782) -> ('10.83.42.198', 22)
	13:35:27 - app.py:55 - ERROR: ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None)
	13:35:27 - app.py:57 - WARNING: Closing connect ('200.1.1.135', 8888)! 
	13:35:27 - app.py:59 - WARNING: Closing connect ('10.83.41.66', 3782)! 
	13:35:27 - app.py:55 - ERROR: ConnectionAbortedError(10053, 'An established connection was aborted by the software in your host machine', None, 10053, None)
	13:35:27 - app.py:57 - WARNING: Closing connect ('10.83.41.66', 3782)! 
	13:35:27 - app.py:59 - WARNING: Closing connect ('200.1.1.135', 8888)! 
```

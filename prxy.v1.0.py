import socket
import threading

def reply(lbl,s1,s2):
 print('.')
 while True:
  try:
   data = s1.recv(1024*1024)
   if not data: break
   #if lbl == 'req' : req.write(data)
   #if lbl == 'ret' : ret.write(data)
   print(lbl)
   print(data)
   #if(data == b'+\x00\x00\x00\x03SELECT * FROM ebidding.v_caizhaokanban_all') :
   s2.send(data)
  except:
   print('except')
   break
  
def TcpTunnel(listenport,tunnelhost,tunnelport):  
 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 sock.bind(('0.0.0.0', listenport))
 sock.listen(10)
 while True: 
  client_fd, client_addr = sock.accept() 
  target_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  target_fd.connect((tunnelhost,tunnelport))
  threading.Thread(target=reply,args=('req',client_fd,target_fd)).start()
  threading.Thread(target=reply,args=('ret',target_fd,client_fd)).start()
  
if __name__ == '__main__':
 import sys
 #print('Starting')
 # sys.argv[1] sys.argv[2] sys.argv[3] 
 TcpTunnel(3306,'proxymysql.whxd.com',3306)

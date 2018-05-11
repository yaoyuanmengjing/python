import socket
#导入python socket模块方法

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sk.settimeout(1)

try:
    sk.connect(('192.168.5.9',8896))
    print 'Server port 8896 OK!'

except Exception:
    print 'Server port 8896 not connect!'

sk.close()
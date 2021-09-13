import socket


_httpico = None

def get_httpico(address, port):
    if _httpico is not None:
        return _httpico
        
    
    s = socket.socket()
    s.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(address, port)
    s.listen(1)
    
    _httpico = {
        'address': address
        'port': port,
        'socket' = s
    }
    
    return _httpico
        
        


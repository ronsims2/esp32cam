import usocket


def get_httpico(address, port, timeout):

    s = usocket.socket()
    s.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
    s.settimeout(timeout)
    s.bind((address, port))
    s.listen(1)
    
    
    _httpico = {
        'address': address,
        'port': port,
        'socket': s
    }
    
    return _httpico


def start_server(_httpico, callback):
    if _httpico is None:
        return False
        
    while True:
        client_conn, client_addr = _httpico['socket'].accept()
        req = client_conn.recv(1024).decode()
        
        print(req)
        
        if callback is None:
            resp = 'HTTP/1.0 500 OK\n\nNo route handler specified.'
        else:
            filtered = callback('HTTP/1.0 200 OK\n\nHello World')
            client_conn.sendall(filtered)
            client_conn.close()
        


def httpico_callback(payload):
    return payload



h = get_httpico('192.168.50.151', 8080, 360)
start_server(h, httpico_callback)

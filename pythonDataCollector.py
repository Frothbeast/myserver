import socket
import mysql.connector

# Database Configuration
db_config = {
    'host' 'localhost',
    'user' 'your_user',
    'password' 'your_password',
    'database' 'frothbeast'
}

def start_server()
    # Set up TCP Socket on Port 1883
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 1883))
    server_socket.listen(5)
    print(Monitoring port 1883 for incoming ASCII data...)

    try
        conn_db = mysql.connector.connect(db_config)
        cursor = conn_db.cursor()
        
        while True
            # Accept incoming connection from ESP-01
            client_socket, addr = server_socket.accept()
            print(fConnection from {addr})
            
            # Receive data (1024 bytes buffer)
            data = client_socket.recv(1024).decode('ascii').strip()
            
            if data
                print(fReceived {data})
                # Insert into 'data' table. 'ID' is omitted to allow AUTO_INCREMENT
                query = INSERT INTO data (word) VALUES (%s)
                cursor.execute(query, (data,))
                conn_db.commit()
                print(Inserted into frothbeast.data)
            
            client_socket.close()

    except Exception as e
        print(fError {e})
    finally
        server_socket.close()

if __name__ == __main__
    start_server()
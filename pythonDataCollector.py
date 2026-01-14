import socket
import mysql.connector

# Database Configuration
db_config = {
    'host': '127.0.0.1',  # Added colon and comma
    'user': 'frothbeast',  # Added colon and comma
    'password': 'DBMyn3wl1f3!26',  # Added colon and comma
    'database': 'frothbeast'  # Added colon
}


def start_server():  # Added colon
    # Set up TCP Socket on Port 1883
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 1883))
    server_socket.listen(5)
    print("Monitoring port 1883 for incoming ASCII data...")  # Added quotes

    try:  # Added colon
        conn_db = mysql.connector.connect(**db_config)  # Added ** to unpack dict
        cursor = conn_db.cursor()

        while True:  # Added colon
            # Accept incoming connection from ESP-01
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")  # Added quotes

            # Receive data (1024 bytes buffer)
            data = client_socket.recv(1024).decode('ascii').strip()

            if data:  # Added colon
                print(f"Received {data}")  # Added quotes
                # Insert into 'data' table. 'ID' is omitted to allow AUTO_INCREMENT
                query = "INSERT INTO data (word) VALUES (%s)"  # Added quotes
                cursor.execute(query, (data,))
                conn_db.commit()
                print("Inserted into frothbeast.data")  # Added quotes

            client_socket.close()

    except Exception as e:  # Added colon
        print(f"Error {e}")  # Added quotes
    finally:  # Added colon
        server_socket.close()


if __name__ == "__main__":  # Added quotes and colon
    start_server()
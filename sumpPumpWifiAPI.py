import socket
import mysql.connector

# Database Configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'frothbeast',
    'password': 'DBMyn3wl1f3!26',
    'database': 'frothbeast'
}


def start_server():
    # Set up TCP Socket on Port 1883
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 1883))
    server_socket.listen(5)
    print("Monitoring port 1883 for incoming data...")

    try:
        conn_db = mysql.connector.connect(**db_config)  # Added ** to unpack dict
        cursor = conn_db.cursor()

        while True:
            # Accept incoming connection from PIC through ESP-01
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")

            # Receive data (1024 bytes buffer)
            data = client_socket.recv(1024).decode('ascii').strip()

            if data:
                print(f"Received {data}")  
                ### decide if the data is valid enough to parse use CRC?
                ### if not then communicate back to sump to reject the packet
                data_list = data.split(',')
                parsed_data = (data_list[0].strip(), data_list[1].strip(), data_list[2].strip())  # Result: ('John Doe', '123 Main St')
                sql = "INSERT INTO sumpData (timeOn, timeOff, hoursOn) VALUES (%s, %s, %s)"
                cursor.execute(sql, parsed_data)
                conn_db.commit()
                print(f"Inserted {parsed_data[0]}, {parsed_data[1]}, {parsed_data[2]}  into frothbeast.sumpData")  # Added quotes

            client_socket.close()

    except Exception as e:
        print(f"Error {e}")
    finally:  # Added colon
        server_socket.close()


if __name__ == "__main__":
    start_server()
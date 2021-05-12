import socket
import json
import time
import traceback
from threading import Thread

class CommandListener:

    def __init__(self, local_ip_address: str, listener_port: int, write_function, read_function):
        self.write_function = write_function
        self.read_function = read_function
        for a in range(1, 4):
            try:
                self.socket = socket.socket()
                self.socket.bind((local_ip_address, listener_port))
                print("Web socket listener registered on port: " + str(listener_port))
                break
            except Exception as e:
                self.socket.close()
                print(e)
                print("trying to establish a socket. --" + str(a))
                time.sleep(5)
                if a == 3:
                    raise e
        self.listening_thread = Thread(target=self.__start_listening)
        self.listening = False

    def start_listening(self):
        self.listening = True
        self.listening_thread.start()
        print("Web socket is listening for commands.")

    def stop_listening(self):
        self.listening = False

    def __start_listening(self):
        self.socket.listen()
        while self.listening:
            try:
                c, addr = self.socket.accept()
                data = c.recv(2048)
                if data:
                    data = json.loads(data.decode())
                    print(f"Connection: {addr}")
                    print(data)
                    print("----------")
                    if data["mode"] == "write":
                        Thread(target=self.write_function, args=(data,)).start()
                        c.close()
                    elif data["mode"] == "read":
                        Thread(target=self.__wait_for_response, args=(c, data,)).start()
                else:
                    c.close()
            except Exception as e:
                print("ERROR:")
                traceback.print_exc()
            except KeyboardInterrupt:
                print("application is forced to stop.")
                exit(0)

    def __wait_for_response(self, c: socket, data):
        c.send(json.dumps(self.read_function(data)).encode())
        c.close()
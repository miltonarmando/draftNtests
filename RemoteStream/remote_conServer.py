from vidstream import StreamingServer

server = StreamingServer("127.0.0.1", 4444)
server.start_server()

while  input("command:> ") != "stop":
    continue

server.stop_server()
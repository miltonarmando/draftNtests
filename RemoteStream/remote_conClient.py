import sys
from vidstream import ScreenShareClient

server_ip = sys.argv[1]
client = ScreenShareClient(server_ip if server_ip != "" else "192.168.8.104", 4444)
client.start_stream()
import socket
import signal
import sys
# 使用 signal 模塊來設置信號處理器，捕獲 SIGINT 和 SIGTERM 信號，並在捕獲到信號時執
# 使用鍵盤中斷：
# 最簡單的方法是使用鍵盤中斷（例如 Ctrl + C）來停止服務器。這會引發一個 KeyboardInterrupt，你可以捕獲這個異常來進行清理工作。

# 使用信號處理：
# 在更高級的實現中，可以使用 Python 的 signal 模塊來捕獲終止信號（如 SIGINT 或 SIGTERM），並優雅地關閉服務器。
def signal_handler(sig, frame):
    print('Interrupt received, shutting down...')
    sock.close()
    sys.exit(0)

# 設置信號處理器
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# ------以上這一沒好像沒用----------

host='localhost'
port=12345
# IPv4 ocket.AF_INET  =>SOCK_STREAM=>TCP  ，socket.SOCK_DGRAM=> UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (host, port)
sock.bind(server_address)
print(f"UDP server is up and listening on {host}:{port}")
# sock.listen(5) #等待連接數

try:
    while True:
        print("\nWaiting to receive message...")
        data, address = sock.recvfrom(4096)

        print(f"Received {len(data)} bytes from {address}")
        print(f"Data: {data.decode('utf-8')}")

        if data:
            sent = sock.sendto(data, address)
            print(f"Sent {len(data)} bytes back to {address}")
# 這一沒 CTRL+C 好像也沒作用
except KeyboardInterrupt:
    print('Interrupt received, shutting down...')
    sock.close()

# 參考語法
#  try:
#     a = int(input('輸入 0～9：'))
#     if a>10:
#         raise
#     print(a)
# except :
#     print('有錯誤喔～')
# else:
#     print('沒有錯！繼續執行！')       # 完全沒錯才會執行這行
# finally:
#     print('管他有沒有錯，繼續啦！')    # 不論有沒有錯都會執行這行
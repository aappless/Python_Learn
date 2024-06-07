import socket
import signal
import sys
import time
import getdata as gg
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

try:
    while True:
        print("\nWaiting to receive message...")
        data, address = sock.recvfrom(4096)

        print(f"Received {len(data)} bytes from {address}")

        print(f"Data: {data.decode('utf-8')}")

        if data:

            # 回傳原值
            # sent = sock.sendto(data, address)
            # 回傳OK表示收到
            # 收到是byte 傳成字串二法1. str(data,encoding='utf-8') 2.data.decode()

            sent = sock.sendto(b'OK', address)
            print(f"Sent OK bytes back to {address}")
            time.sleep(0.1) # 應該是收資料的問題因為一次只會收一筆
            sent = sock.sendto(data, address)
            print(f"Sent {len(data)} bytes back to {address}")
            print(data)
            print(type(data))
            # byte格式
            # if data==b'CLOSEME':
            #     sock.close()
            #     sys.exit(0)
            # ASCII 只能儲英文或特殊字符，只占一個字節
            # Unicode 不管是中文或英文，都是占二個字節，一個字節8bit
            # UTF-8 是一種針對Unicode的可變長度字元編碼，英文字符一樣會依照ASCII碼規範，只占一個字節8bit，而中文字符的話，統一就占三個字節
            # Python3因為字串已經全部統一成 unicode ，所以不必在字符串前加上 u
            key=str(data,encoding='ansi')
            print(f'keyis:{key}')
            if key == 'CLOSEME':
                sock.close()
                sys.exit(0)
            elif key == 'NAME':
                sent = sock.sendto(b'I am HelloKitty', address)
            elif key == 'GETDATA':
                sent = sock.sendto(b'GG...', address)
                num=gg.getdata('HELLO')
                print(num)
                sock.sendto(bytes(str(num), 'utf-8'), address)
                sent = sock.sendto(b'num', address)

            # key=str(data)
            # print(key)
            # match   key:     # data.decode():
            #     case 'NAME':
            #           sent = sock.sendto(b'I am HelloKitty', address)
            #     case 'GETDATA':
            #            sent = sock.sendto(b'chrno', address)




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
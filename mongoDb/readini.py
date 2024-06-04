import configparser
import os

# 獲取當前工作目錄
current_directory = os.path.dirname(os.path.abspath(__file__))

# 拼接 config.ini 文件的完整路徑
config_path = os.path.join(current_directory, 'config.ini')

# 創建 ConfigParser 對象
config = configparser.ConfigParser()

# 讀取 config.ini 文件
config.read(config_path, encoding='utf-8')

# 初始化 eform 變量
eform = ''

# 嘗試從配置文件中獲取 EFORM_SERVER 的值
try:
    eform = config['SYSTEM']['EFORM_SERVER']
except KeyError:
    print('發生錯誤：未找到 EFORM_SERVER 配置')

# 打印 eform 變量
print(eform)
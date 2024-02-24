# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
from scapy.all import ICMP, IP, send

# 创建ICMP数据包
icmp_packet = ICMP()
icmp_packet.type = 8  # 类型8表示echo request
icmp_packet.data = "Hello, Scapy!"

# 将ICMP数据包放入IP数据包内
ip_packet = IP()
ip_packet.src = "192.168.1.1"  # 源IP地址
ip_packet.dst = "192.168.1.2"  # 目标IP地址
ip_packet.ttl = 64
ip_packet /= icmp_packet

# 发送数据包
result = send(ip_packet)

# 打印结果
print(result.show())
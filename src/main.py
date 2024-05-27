from gurux_dlms import GXDLMSClient

def main():
    client = GXDLMSClient()
    client.serverAddress = 1
    client.clientAddress = 16
    client.useLogicalNameReferencing = True

    # 假设你已经配置了连接设置
    # connection = GXDLMSConnection(client)
    # connection.connect()

    # 读取一个特定对象，例如电能表的读数
    # object = client.getObjects().findByLN("0.0.1.0.0.255")
    # value = client.read(object, 2)
    # print(f"Value: {value}")

if __name__ == "__main__":
    main()

import requests
import time

# 秒级时间戳
timestamp_seconds = int(time.time())

# 毫秒级时间戳
timestamp_milliseconds = int(time.time() * 1000)

print("秒级时间戳:", timestamp_seconds)
print("毫秒级时间戳:", timestamp_milliseconds)

# 替换成自己的ID和KEY（注册地址：https://www.apihz.cn/user/）
params = {
    "id": "10005902",      # 用户ID
    "key": "123456",# 用户KEY
    "type": "1"            # 返回标准时间格式
}

# 发送GET请求
response = requests.get(
    url="https://cn.apihz.cn/api/time/getapi.php",
    params=params
)

print("请求URL:", response.url)
print("请求方法:", response.request.method)
print("请求头:", response.text)  


# 处理响应
if response.status_code == 200:
    data = response.json()
    if data["code"] == 200:
        print("当前北京时间:", data["msg"])
    else:
        print("错误:", data["msg"])
else:
    print("请求失败，状态码:", response.status_code)
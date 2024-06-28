import requests
from datetime import datetime

# 从命令行获取用户输入的token和courseId
token = input("请输入Token: ")
courseId = input("请输入CourseId: ")

# 获取当前日期，格式为YYYY-MM-DD
current_date = datetime.now().strftime('%Y-%m-%d')

# 请求的URL，将endTime替换为当前日期
url = f'https://zjy2.icve.com.cn/prod-api/spoc/courseFaceTeachInfo/student/list?pageNum=1&pageSize=50&startTime=2022-05-31&endTime={current_date}&courseId={courseId}'

# 设置请求的headers，包括User-Agent和其他一些常见的请求头
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

# 发送GET请求
response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 将响应内容写入文件
    with open('课程.txt', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print('内容已成功写入课程.txt文件。')
else:
    print('请求失败，状态码：', response.status_code)

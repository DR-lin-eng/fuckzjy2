import json
import requests

# 从课程.txt文件中读取内容
with open('课程.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 用户输入的token
token = input("请输入您的token: ")

# 初始化请求URL和头部信息
url = 'https://zjy2.icve.com.cn/prod-api/spoc/courseFaceTeachInfo/student/info'
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 打开题目.txt文件用于写入
with open('题目.txt', 'w', encoding='utf-8') as file:
    # 遍历每个课程
    for course in data['rows']:
        # 获取所需的三个ID
        class_id = course['classId']
        course_id = course['courseId']
        id_value = course['id']

        # 设置请求参数
        params = {
            'classId': class_id,
            'courseId': course_id,
            'id': id_value,
            'requireType': '2'
        }

        # 发送请求并获取响应
        response = requests.get(url, headers=headers, params=params)
        
        # 检查请求是否成功
        if response.status_code == 200:
            # 将响应内容写入文件
            file.write(f"课程ID: {course_id}\n")
            file.write(f"班级ID: {class_id}\n")
            file.write(f"具体课程ID: {id_value}\n")
            file.write("题目内容:\n")
            file.write(response.text)
            file.write("\n\n")
        else:
            # 输出错误信息
            file.write(f"课程ID: {course_id}\n")
            file.write(f"班级ID: {class_id}\n")
            file.write(f"具体课程ID: {id_value}\n")
            file.write("题目获取失败\n")
            file.write("\n\n")

print("所有课程的题目内容已保存到题目.txt")

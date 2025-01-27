from wxauto import WeChat
from openai import OpenAI
import time

# 创建微信实例化对象
wx = WeChat()

# 监听列表
listen_list = [
    '爸爸',
    '妈妈',
    '？',
    '文件传输助手',
    "姐姐"
]

# 初始化 OpenAI 客户端
client = OpenAI(api_key="sk-98894fe5c0df47238dd1638bb550ef0b", base_url="https://api.deepseek.com")

# 获取会话消息
while True:
    sessions = wx.GetSession()  # 获取最新会话
    for session in sessions:
        # 判断是否是新消息，并且消息来自监听列表中的人物
        if session.isnew and session.name in listen_list:
            # 获取会话消息内容
            user_message = session.content

            # 调用 OpenAI 接口获取回复
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message},
                    {"role": "assistant", "content": ""}
                ],
                stream=False
            )

            # 获取返回的回复消息
            return_msg = response.choices[0].message.content

            # 发送消息给指定的人
            wx.SendMsg(msg=return_msg, who=session.name)

    # 每隔一段时间检查新的消息
    time.sleep(1)


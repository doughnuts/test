from wxauto import WeChat

# 初始化微信
wx=WeChat()

# 登录微信
msgs = wx.GetAllMessage(
    # savepic   = True,   # 保存图片
    savefile  = True,   # 保存文件
    # savevoice = True    # 保存语音转文字内容
)
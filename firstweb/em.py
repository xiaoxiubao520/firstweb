psd = 'wokobkmttkspeaab'

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

def emile_yz(to_addrs,code):
# 邮件发送者邮箱账号
    from_addr = '2247961872@qq.com'
    password = psd  # 或者应用专用密码

    # SMTP服务器及端口
    smtp_server = 'smtp.qq.com'
    port = 465  # 对于Gmail, 通常是587；对于其他服务商，可能是其他端口

    # 邮件接收者列表

    # 邮件主题
    subject = '白熊网站注册接收验证码'

    # 邮件正文
    body = f'您的邮箱验证码是:{code}\n请尽快填写'

    # 创建邮件对象
    msg = MIMEMultipart()
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    msg['From'] = formataddr((from_addr, from_addr))  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr((to_addrs, to_addrs))  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = Header(subject, 'utf-8')
    # filename = 'Db.py'  # 附件的文件名
    # with open(filename, 'rb') as attachment:
    #     part = MIMEBase('application', 'octet-stream')
    #     part.set_payload(attachment.read())
    #     encoders.encode_base64(part)
    #     part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    #     msg.attach(part)


    server = smtplib.SMTP_SSL(smtp_server, port)
    try:
        # 创建SMTP连接

        server.login(from_addr, password)  # 登录

        # 发送邮件
        server.sendmail(from_addr, to_addrs, msg.as_string())
        print("邮件发送成功")
        a = True
    except smtplib.SMTPException as e:
        print(f"邮件发送失败: {e}")
        a = ""
    finally:
        server.quit()
    return a



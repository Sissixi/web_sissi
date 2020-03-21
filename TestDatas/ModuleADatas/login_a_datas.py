"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/20 0020 下午 10:19
"""
# A端登录成功账号密码
success_a_data = {
    "username": "luckyxi",
    "password": "wbyxixi123",
    "code": "1234"
}
fail_a_data = [
    {"username": "luckyxi", "password": "wbyxixi", "code": "1234", "check": "登录失败!密码错误,或者用户名不存在!"},
    {"username": "luckyxi123", "password": "wbyxixi", "code": "1234", "check": "登录失败!密码错误,或者用户名不存在!"},
    {"username": "luckyxi", "password": "wbyxixi", "code": "4567", "check": "验证码错误或未填写!"}]

data = {
    "username": "luckyxi",
    "password": "wbyxixi123",
    "code": "",
    "check": "请输入验证码"
}

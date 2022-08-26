# 统一code回复
from flask import jsonify


def success(data=None):
    """ 操作正确执行后的返回函数"""
    resp = dict(code=success_code, message=success_desc)
    if data:
        resp['data'] = data
    else:
        resp['data'] = None
    response = jsonify(resp)
    return response


success_code = 200
success_desc = "success"

error_code = 500
error_desc = "未知错误"

invalid_access_token_code = 2008
invalid_access_token_desc = "令牌已过期，请重新登录"

no_login_code = 2009
no_login_desc = "请登录"

invalid_param_code = 2401
invalid_param_desc = "参数验证错误"

bad_request_code = 2400
bad_request_desc = "客户端数据有误"

# 2100 - 2150 之间，用户相关
invalid_login_code = 2100
invalid_login_desc = "用户名或密码错误"

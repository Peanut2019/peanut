from peanut.core import resp


class AppBaseException(Exception):
    """ 自定义异常的父异常，所有自定义异常都继承本异常，以区分系统异常 """

    def __init__(self, message=resp.error_desc, code=resp.error_code):
        super().__init__()
        self.message = message
        self.code = code

    def to_dict(self):
        rv = dict()
        rv['code'] = self.code
        rv['message'] = self.message
        return rv


class ClientError(AppBaseException):
    """
    客户端操作有误
    """

    def __init__(self, message=resp.bad_request_desc, code=resp.bad_request_code):
        super().__init__(message, code)

# -*- encoding:utf-8-*-

__name__ = "controller"


def myresponse(func):
    def encode_response(*args, **kwargs):
        body = func(*args, **kwargs)
        res = body.encode('utf-8')
        return res
    return encode_response


def template(template_name):
	template_file = os.path.join("../views", template_name)
	with open(template_file) as f:
		page = f.read()
	return page
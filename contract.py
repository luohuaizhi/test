import requests


def generate_contract(appId):
	url = "http://123.57.48.237:7082/webservice/loanService?wsdl"
	client = suds.client.Client(url)
	service = client.service
	body = client.factory.create("ns0:generateContract")
	body.appId = appId
	res = service.generateContract(body)
    print res
    return res["returnCode"] == "000"


def sign_contract(appId, isCompanyStamps):
	url = "http://123.57.48.237:7086/micro_kh/SealController/getSealCommon"
	data = {
		"appId": appId,  # String 必填；工单号
		"isCompanyStamps": isCompanyStamps,  # String 必填；0为签公章 1为不签公章
	}
	"""
	0000 该工单对应全部合同盖章成功！
	0001 合同状态为未读！
	0003 用户已经处于已盖章状态.
	0008 未获取到用户基本信息！！
	0009 签章失败！
	0011 系统异常
	0012 工单下合同为0.
	0020 更新用户签章状态失败！
	0021 写入签署时间失败！！
	0022 更新工单表状态失败！
	02 上传合同文件失败！
	9000 调用公章方法签章失败！
	8000 合同数量与已签约合同数量不符，不能
	签公章！
	"""
	res = requests.post(url, data)
	print res["resp_code"]


def query_contract(appId, productId, saleChannel):
	url = "http://123.57.48.237:7082/httpIntf/contractIntf/contract/queryContract.intf"
	secretKey = """MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKgAG7/hqF7XbkvVa4
	PayoNJrrnU5pw21jkNlPbdHniNL50T+4ZxjGklGtdBHp0j/V2RgMNvXlBElnWDlUMAsQ1dgk
	3U2M9H7FmV2RAMqFjXOz93DW3i1ugze0gr28dkzFe8Ht37IrMDy3FG0NHc+OocnWRWHU
	p7mv/CxNQ/TSMDAgMBAAECgYBGoB0KUnQ0wr4kdSkIuk7OWIhyqPT1kPwH6hTInvZz
	WW89yqu/vjZ38VhSS5byGrIlxshp4IS2m87gwhtamozTToiS/aQvejlOSIapyZutkMOHlyjPBOAF
	PYLk5kun+NzFJ/Ql2uWmCY+POYiE4MJBo8WnD7DHwuLpKAka2f4l8QJBAP5y0AolAVCS
	Ws8+nJ/ZWtyRrgbEY+j+N+hMVyYmrqB34t2zY+1+XcbLTMMH8DszqARJfWrbexvsDBuX
	1LL1tmkCQQCpBlpEW+lpGsAHiQtYKsHDiGu3cEugOeFjDYrwrx6dr/2N/Jbp05BoKjybkw
	Db+TbtCyX4aBHZzzGx/TOz11iLAkBPfZrUsH7apv5LpGnV3ldudOyDHLOBxHm+zqqjNo5
	zf0CWtkZPmZy+UCDpBP/d3uNsg3D1AyBQtsuJi0NdrTmRAkBK2ZNTvlgIwV3UeG3bp2OT
	EXCSFVqII9mZob+rggFO10azf+3csmG6nymjw1+YCi62nj88V+m/yK87IOOqemytAkEAxLY
	nOTPjT563NahT7wat3EF8x41Fynlo2DEYPSkuzqv8FQqCxMU2FDZ0zuO/w+pd2bv/8g4ZHf
	AS7YZCrcsBXQ=="""
	data = {
		"jsonHead":{
			"secretKey": secretKey,
			"isSecret": 2  #  [1、是,2、否]
		},
		"jsonContent":{
			"saleChannel":saleChannel # String *必填渠道号
			"productId": productId  # String *必填产品ID
			"appId": appId #  String *必填工单号
		}
	}
	res = requests.post(url, data)
	print res["resp_code"]
	print res["resp_msg"]
	print res["resp_result"]["contractUrl"]


def main():
	appId = ""
	if generate_contract(appId):
		sign_contract(appId, 0)
	print query_contract(appId, productId, saleChannel)


if __name__ == '__main__':
	main()
# encoding=utf-8
import requests
from datetime import datetime

url = "http://ip1:port1/ams/bankpage/intf/server.intf"
SYS_CODE = "3019"


class TRANS_TYPE:
    QUERY = "Q"
    TRANS = "T"


class CERT_TYPE:
    IDENTITY_CARD = "01",       # "居民身份证"
    HK_MO_PASS = "02",          # "港澳居民往来内地通行证"
    TW_PASS = "03",             # "台湾居民来往大陆通行证"
    FOREIGNER_PASS = "04",      # "外国公民护照或外国人永久居留证"
    OC_PASS = "05",             # "定居国外的中国公民中国护照"
    MILITARY_LICENSE = "08",    # "军官证"


class TRADE_TYPE:
    PASSWORD_RECHARGE = "00"    # 验密充值
    OFFLINE_RECHARGE = "B1" # 线下充值
    BORROWER_RECHARGE = "B3"    # 代扣（借款人充值）
    SUB_ACCOUNT_RECHARGE = "02" # 子账户跨行充值入金
    FIRST_PAY_RECHARGE = "08"   # 首笔支付认证入金
    USER_RECHARGE = "A0"    # 费用户充值
    RISK_RECHARGE = "A1"    # 风险金充值
    MARKETING_RECHARGE = "A2"   # 营销户充值
    CLIENT_APPLY_CASH = "01"    # 客户提现
    USER_APPLY_CASH = "A3"  # 费用户提现
    RISK_APPLY_CASH = "A4"  # 风险金提现
    MARKETING_APPLY_CASH = "A5" # 营销户提现
    MONEY_FREEZE = "DJ"  # 资金冻结
    MONEY_UNFREEZE = "JD"   # 资金解冻
    LOAN_WARRANT = "03"  # 放款授权
    LOAN_RETURN = "11"  # 放款退回
    REPAY_WARRANT = "04"    # 还款授权
    INSTEAD_REPAY_WARRANT = "15"    # 代偿授权
    INSTEAD_REPAYMENTS = "18"   # 代偿回款
    CLAIMS_ASSIGNMENT = "06"    # 债权受让
    PLATFORM_MARKETING = "16"   # 平台营销
    MARKETING_RETURN = "26"  # 营销退回
    CONSUME_LOAN = "21"  # 消费金融放款
    CONSUME_RETURN = "22"   # 消费金融退回
    ADJUST = "17"   # 尾差调整
    ADJUST = "12"   # 利差调整
    BROKERAGE_WARRANT = "F8"    # 佣金收取授权
    BROKERAGE_RETURN = "F9"     # 佣金退回
    CREDIT_MANAGE_FEE_WARRANT = "20"    # 信用管理费收取授权
    CREDIT_MANAGE_FEE_RETURN = "30" # 信用管理费退回
    PARTNER_REPAY_WARRANT = "19"    # 合作机还款授权



def generate_serial_no(sys_code, trans_date, trans_code, self_code):
    """
    交易流水号共24位数字，组成规则为：
    系统编码（4位）+日期（6位，YYMMDD）+接口类型（3位，接口编号）+自定义序号（11位）
    例：100118010501234567890123
    :param sys_code:系统编码
    :param trans_date:日期
    :param trans_code:接口编号
    :param self_code:自定义序号
    :return:
    """
    serial_no_regex = "{sys_code}{trans_date}{trans_code}{self_code}"
    serial_no = serial_no_regex.format(sys_code=sys_code, trans_date=trans_date, trans_code=trans_code, self_code=self_code)
    return serial_no


def generate_head(trans_type, trans_code):
    """
    创建报文头
    :param trans_type:交易类型（T:交易，Q:查询）
    :param trans_code:交易码（具体接口中指定）
    :return:
    """
    sys_code = SYS_CODE
    channel_no = ""
    dt = datetime.now()
    trans_date = str(dt.year)+str(dt.month)+str(dt.day)
    trans_time = str(dt.hour)+str(dt.minute)+str(dt.second)
    trans_serial_no = generate_serial_no(sys_code, trans_date, trans_code)
    data = {
        "transType": trans_type,
        "transCode": trans_code,
        "transDate": trans_date,  # 交易日期（yyyyMMdd）
        "transTime": trans_time,  # 交易时间(HHmmss)
        "transSerialNo": trans_serial_no,  # 交易流水号（详见统一报文流水号规则）
        "channelNo": channel_no,
        "sysCode": sys_code,
    }
    return data


def company_open_account(custNo, userRole, userName, certType, certNo,
                         phoneNo, bankNo, regBank, legalName, legalCertType,
                         legalCertNo, busiLiceNo, taxNo, backUrl, asynBackUrl,
                         initiatorType, note=""):
    """
    企业开户接口
    :param custNo:客户编号
    :param userRole:用户角色 [00：出借人,01：借款人,02：担保公司,04：商户,05：保险公司,06：合作机构]
    :param userName:企业名称
    :param certType:证件类型[06：统一社会信用代码,07：组织机构代码,09：其他（企业）]
    :param certNo:证件号码
    :param phoneNo:手机号(企业用户填法人手机号)
    :param bankNo:银行结算账户
    :param regBank:开户行编码
    :param legalName:法人姓名
    :param legalCertType:法人证件类型
        [01:居民身份证,02：港澳居民往来内地通行证,03：台湾居民来往大陆通行证,
        04：外国公民护照或外国人永久居留证,05：定居国外的中国公民中国护照]
    :param legalCertNo:法人证件号码
    :param busiLiceNo:营业执照编号
    :param taxNo:税务登记号
    :param backUrl:返回URL地址
    :param asynBackUrl:统一账户异步回调前端和业务系统地址
    :param initiatorType:（请求发起方）终端类型[01：移动端,02：PC端,]
    :param note:备注
    :return:{
        "resultType":"银行端开户状态1:未开户；2:已开户",
        "url":"未开户时返回跳转地址",
        "phoneNo":"已开户时返回手机号",
        "bankNoFlag":"已开户时返回银行卡一致性(是否与入参银行卡一致，判断入参银行卡是否已经绑定)0一致；1不一致",
        "depositAcct":"已开户时返回存管账户",
        "subAcct":"已开户时返回存管子账户",
        "bankSubAcct":"已开户时返回银行端账户",
        "firstRegChannel":"首次开户渠道（参考渠道编码）",
        "depositTime":"存管时间(yyyyMMddHHmmss)",
        "dealStatus":"8：请求页面成功1：失败",
        "bankNote":"银行摘要",
    }
    """
    header = generate_head(TRANS_TYPE.TRANS, "HX02")
    body = {
        "custNo": custNo,
        "userRole": userRole,
        "userName": userName,
        "certType": certType,
        "certNo": certNo,
        "phoneNo": phoneNo,
        "bankNo": bankNo,
        "regBank": regBank,
        "legalName": legalName,
        "legalCertType": legalCertType,
        "legalCertNo": legalCertNo,
        "busiLiceNo": busiLiceNo,
        "taxNo": taxNo,
        "backUrl": backUrl,
        "asynBackUrl": asynBackUrl,
        "initiatorType": initiatorType,
        "note": note,
    }
    data = {
        "head": header,
        "body": body
    }
    res = requests.post(url, data)
    print res
    return res


def company_account_update(subAcct, depositAcct, userName, phoneNo, legalName,
                        custNo, changeType, legalCertType, legalCertNo, backUrl,
                        asynBackUrl, initiatorType, note=""):
    """
    企业开户信息变更
    :param subAcct:存管子账户
    :param depositAcct:存管账户
    :param userName:企业名称
    :param phoneNo:手机号
    :param legalName:法人姓名(如果修改类型为03，该字段必输)
    :param custNo:客户编号
    :param changeType:变更类型：[01：姓名,02：手机号,03: 法人信息]
    :param legalCertType:法人证件类型
        [01:居民身份证,02：港澳居民往来内地通行证,03：台湾居民来往大陆通行证,
        04：外国公民护照或外国人永久居留证,05：定居国外的中国公民中国护照]
        (如果修改类型为03，该字段必输)
    :param legalCertNo:法人证件号码(如果修改类型为03，该字段必输)
    :param backUrl:返回URL地址
    :param asynBackUrl:统一账户异步回调前端和业务系统地址
    :param initiatorType:(请求发起方）终端类型 [01：移动端,  02：PC端]
    :param note:备注
    """
    header = generate_head(TRANS_TYPE.TRANS, "HX03")
    body = {
        "subAcct": subAcct,
        "depositAcct": depositAcct,
        "userName": userName,
        "phoneNo": phoneNo,
        "legalName": legalName,
        "custNo": custNo,
        "changeType": changeType,
        "legalCertType": legalCertType,
        "legalCertNo": legalCertNo,
        "backUrl": backUrl,
        "asynBackUrl": asynBackUrl,
        "initiatorType": initiatorType,
        "note": note,
    }
    data = {
        "head": header,
        "body": body
    }
    res = requests.post(url, data)
    print res
    return res
    pass


def company_bind_card(regBank, custNo, depositAcct, subAcct, bankNo,
                      backUrl, asynBackUrl, initiatorType, note=""):
    """
    企业绑卡
    :param regBank: 开户行编码（参考字典《统一账户字典编码V*.*.xlsx》）
    :param custNo: 客户编号
    :param depositAcct: 存管账户
    :param subAcct: 存管子账户
    :param bankNo: 银行卡号
    :param backUrl: 返回URL地址
    :param asynBackUrl: 统一账户异步回调前端和业务系统地址
    :param initiatorType: （请求发起方）终端类型[01：移动端,02：PC端]
    :param note: 备注
    :return:
    """
    header = generate_head(TRANS_TYPE.TRANS, "HX07")
    body = {
        "regBank": regBank,
        "custNo": custNo,
        "depositAcct": depositAcct,
        "subAcct": subAcct,
        "bankNo": bankNo,
        "backUrl": backUrl,
        "asynBackUrl": asynBackUrl,
        "initiatorType": initiatorType,
        "note": note,
    }
    data = {
        "head": header,
        "body": body
    }
    res = requests.post(url, data)
    print res
    return res
    pass


# TODO 9    企业银行卡解绑
def company_unbind_card(custNo, depositAcct, subAcct, bankNo, initiatorType, note=""):
    """

    :param custNo: 客户编号
    :param depositAcct: 存管账户
    :param subAcct: 存管子账户
    :param bankNo: 银行卡号
    :param initiatorType: （请求发起方）终端类型[01：移动端,02：PC端]
    :param note:  备注
    :return:
    """
    header = generate_head(TRANS_TYPE.TRANS, "HX09")
    body = {
        "custNo": custNo,
        "depositAcct:": depositAcct,
        "subAcct": subAcct,
        "bankNo": bankNo,
        "initiatorType": initiatorType,
        "note": note,
    }
    data = {
        "head": header,
        "body": body
    }
    res = requests.post(url, data)
    print res
    return res
    pass


def personal_open_account(custNo, userRole, userName, certType, certNo, phoneNo,
                          bankNo, regBank, cardPhoneNo, backUrl, asynBackUrl,
                          city, professional, initiatorType, note=""):
    """
    1   个人开户接口
    :param custNo:客户编号
    :param userRole:用户角色[00：出借人,01：借款人,04：商户]
    :param userName:姓名
    :param certType:证件类型
        01:居民身份证
        02：港澳居民往来内地通行证
        03：台湾居民来往大陆通行证
        04：外国公民护照或外国人永久居留证
        05：定居国外的中国公民中国护照
        08：军官证
    :param certNo:证件号码
    :param phoneNo:手机号（接收华夏银行存管验证码）
    :param bankNo:银行卡号（识别华夏银行卡）
    :param regBank:开户行编码
    :param cardPhoneNo:银行卡预留手机号
    :param backUrl:返回URL地址
    :param asynBackUrl:统一账户异步回调前端和业务系统地址
    :param city:地区
    :param professional:职业
    :param initiatorType:终端类型
    :param note:备注
    :return:
    """
    header = generate_head(TRANS_TYPE.TRANS, "HX00")
    body = {
        "custNo": custNo,
        "userRole": userRole,
        "userName": userName, 
        "certType": certType, 
        "certNo": certNo, 
        "phoneNo": phoneNo,
        "bankNo": bankNo, 
        "regBank": regBank, 
        "cardPhoneNo": cardPhoneNo, 
        "backUrl": backUrl,
        "asynBackUrl": asynBackUrl, 
        "city": city, 
        "professional": professional, 
        "initiatorType": initiatorType, 
        "note": note

    }
    data = {
        "head": header,
        "body": body
    }
    res = requests.post(url, data)
    print res
    return res
    pass
    pass


def personal_account_update(custNo, subAcct, depositAcct, changeType, userName,
                            phoneNo, backUrl, asynBackUrl, initiatorType, note=""):
    """
    2   个人开户信息变更
    :param custNo:客户编号
    :param subAcct:存管子账户
    :param depositAcct:存管账户
    :param changeType:变更类型：[01：姓名,02：手机号]
    :param userName:姓名
    :param phoneNo:手机号
    :param backUrl:返回URL地址
    :param asynBackUrl:统一账户异步回调前端和业务系统地址
    :param initiatorType:终端类型
    :param note:备注
    :return:
    """
    header = generate_head(TRANS_TYPE.TRANS, "HX01")
    body = {
        "custNo": custNo,
        "subAcct": subAcct,
        "depositAcct": depositAcct,
        "changeType": changeType,
        "userName": userName,
        "phoneNo": phoneNo,
        "backUrl": backUrl,
        "asynBackUrl": asynBackUrl,
        "initiatorType": initiatorType,
        "note": note
    }
    data = {
        "head": header,
        "body": body
    }
    res = requests.post(url, data)
    print res
    return res
    pass


def personal_bind_card(custNo, depositAcct, subAcct, bankNo, cardPhoneNo, cardType,
                      regBank, backUrl, asynBackUrl, initiatorType, note=""):
    """
    5   个人绑卡
    :param custNo: 客户编号
    :param depositAcct: 存管账户
    :param subAcct: 存管子账户
    :param bankNo: 银行卡号
    :param cardPhoneNo: 银行预留手机号
    :param cardType: 银行卡类型（B10借记卡,B11贷记卡,默认B10借记卡）
    :param regBank: 开户行编码
    :param backUrl: 返回URL地址
    :param asynBackUrl: 统一账户异步回调前端和业务系统地址
    :param initiatorType: （请求发起方）终端类型[01：移动端,02：PC端]
    :param note: 备注
    :return:
    """
    header = generate_head(TRANS_TYPE.TRANS, "HX04")
    body = {
        "custNo": custNo,
        "depositAcct": depositAcct,
        "subAcct": subAcct,
        "bankNo": bankNo,
        "cardPhoneNo": cardPhoneNo,
        "cardType": cardType,
        "regBank": regBank,
        "backUrl": backUrl,
        "asynBackUrl": asynBackUrl,
        "initiatorType": initiatorType,
        "note": note,
    }
    data = {
        "head": header,
        "body": body
    }
    res = requests.post(url, data)
    print res
    return res
    pass


def personal_unbind_card(custNo, depositAcct, subAcct, bankNo, initiatorType, note=""):
    """
    7   个人银行卡解绑
    :param custNo:客户编号
    :param depositAcct:客户编号
    :param subAcct:存管子账户
    :param bankNo:银行卡号
    :param initiatorType:
    :param note:
    :return:
    """
    header = generate_head(TRANS_TYPE.TRANS, "HX06")
    body = {
        "custNo": custNo,
        "depositAcct": depositAcct,
        "subAcct": subAcct,
        "bankNo": bankNo,
        "initiatorType": initiatorType,
        "note": note
    }
    data = {
        "head": header,
        "body": body
    }
    res = requests.post(url, data)
    print res
    return res
    pass


def personal_phone_change(custNo, depositAcct, subAcct, cardPhoneNo, oldBankNo,
                          cardType, backUrl, asynBackUrl, initiatorType, note=""):
    """
    6   个人预留手机号变更
    :param custNo:客户编号
    :param depositAcct:客户编号
    :param subAcct:存管子账户
    :param cardPhoneNo:银行预留手机号
    :param oldBankNo:银行卡号
    :param cardType:银行卡类型（B10借记卡,B11贷记卡,默认B10借记卡）
    :param backUrl:
    :param asynBackUrl:
    :param initiatorType:
    :param note:
    :return:
    """
    header = generate_head(TRANS_TYPE.TRANS, "HX05")
    body = {
        "custNo": custNo,
        "depositAcct": depositAcct,
        "subAcct": subAcct,
        "cardPhoneNo": cardPhoneNo,
        "oldBankNo": oldBankNo,
        "cardType": cardType,
        "backUrl": backUrl,
        "asynBackUrl": asynBackUrl,
        "initiatorType": initiatorType,
        "note": note
    }
    data = {
        "head": header,
        "body": body
    }
    res = requests.post(url, data)
    print res
    return res


def personal_tran_pwd_change(tradeType, custNo, depositAcct, subAcct, backUrl, asynBackUrl, note=""):
    """
    10  用户交易密码变更
    :param tradeType:操作类型
        U4：存管交易密码变更（修改交易密码）
        U5：存管交易密码重置（忘记交易密码）
    :param custNo:客户编号
    :param depositAcct:客户编号
    :param subAcct:存管子账户
    :param backUrl:
    :param asynBackUrl:
    :param note:
    :return:
    """
    header = generate_head(TRANS_TYPE.TRANS, "HX10")
    body = {
        "tradeType": tradeType,
        "custNo": custNo,
        "depositAcct": depositAcct,
        "subAcct": subAcct,
        "backUrl": backUrl,
        "asynBackUrl": asynBackUrl,
        "note": note
    }
    data = {
        "head": header,
        "body": body
    }
    res = requests.post(url, data)
    print res
    return res


def platform_open_account(custNo, accType, userName, certType, certNo,
                         bankNo, bankPhoneNo, legalName, legalCertType,
                         legalCertNo, legalPhoneNo, note=""):
    """
    11  平台开户
    :param custNo:客户编号
    :param accType:账户类型 [E：费用子账户,R：风险金子账户,M：营销子账户]
    :param userName:企业名称
    :param certType:企业证件类型
    :param certNo:企业证件号码
    :param bankNo:企业银行账户（仅支持华夏银行）
    :param bankPhoneNo:预留手机号
    :param legalName:法人姓名
    :param legalCertType:法人证件类型
    :param legalCertNo:法人证件号码
    :param legalPhoneNo:法人手机号
    :param note:
    :return:
    """
    header = generate_head(TRANS_TYPE.TRANS, "HX11")
    body = {
        "custNo": custNo,
        "accType": accType,
        "userName": userName,
        "certType": certType,
        "certNo": certNo,
        "bankNo": bankNo,
        "bankPhoneNo": bankPhoneNo,
        "legalName": legalName,
        "legalCertType": legalCertType,
        "legalCertNo": legalCertNo,
        "legalPhoneNo": legalPhoneNo,
        "note": note
    }
    data = {
        "head": header,
        "body": body
    }
    res = requests.post(url, data)
    print res
    return res


def register_customer(idCardNo, realName, key, idType="1"):
    """
    实名注册新接口
    :param idCardNo:用户身份证号
    :param realName:用户真实姓名
    :param key:渠道的key，用户中心会分发
    :param idType:判断客户类型(这里1表示个人身份证注册，2表示企业注册)
    :return: {
        "result":"success",
        "custNo":"201703071229507083536936463",
        "status":"0",
        "uuid":"53e24587-7330-428e-bfaf-c0e5df5052d7"}
    """
    url = "http://101.200.87.116:9190/usercenter/special/realNameRegistNew.do"
    data = {
        "idCardNo": idCardNo,
        "realName": realName,
        "key": key,
        "idType": idType,
    }
    try:
        res = requests.post(url, data)
        cust_no = res.get("custNo")
    except Exception as e:
        print e
    return cust_no



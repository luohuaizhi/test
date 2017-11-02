# -*- encoding:utf-8 -*-
import ConfigParser
import urllib2
import urllib
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA, MD5
from Crypto.Signature import PKCS1_v1_5 as pk
import base64
# import rsa
import json
import hashlib


def md5_encode(content):
    h = MD5.new()
    h.update(content)
    md5_content = h.hexdigest().lower()
    return md5_content


class SSQClient(object):
    def __init__(self, config_file, logger=None):
        self.logger = logger
        conf = ConfigParser.ConfigParser()
        conf.read(config_file)
        # self.private_key = conf.get("general", "private_key")
        # self.private_key = rsa.PrivateKey.load_pkcs1(self.private_key, "DER")
        with open(conf.get("general", "private_key"), "r") as f:
            file_content = f.read().encode()
        self.private_key = RSA.importKey(file_content)
        # self.private_key = rsa.PrivateKey.load_pkcs1(file_content)
        self.server = conf.get("general", "server")
        self.account = conf.get("general", "account")
        self.mid = conf.get("general", "mid")
        self.phone = conf.get("general", "phone")

        self.reg_user_fn = conf.get("interface", "register_user")
        self.send_contract_fn = conf.get("interface", "contract_send")

    def get_sign(self, *args):
        """
        获取签名
        Args:
            args: 签名内容
        Returns:签名
        """
        content = '\n'.join([str(i) for i in args])
        h = SHA.new(content)
        signer = pk.new(self.private_key)
        sign = signer.sign(h)
        sign = base64.b64encode(sign)
        # sign = rsa.sign(content, self.private_key, 'SHA-1')
        return sign
        # sha1 = SHA.new()
        # sha1.update(content)
        # key_der = base64.b64decode(self.private_key)
        # rsa_key = RSA.importKey(key_der)
        # rsa = pk.new(rsa_key)
        # return base64.b64encode(rsa.sign(sha1))

    def send_contract(self, file_name, user_list, send_user, file_data):
        """
        发送合同
        Args:
            file_name: 合同名称
            user_list: 签约用户
            send_user: 发送用户
            file_data: 合同内容
        Returns:
            响应结果
        """
        user_list = json.dumps(user_list)
        send_user = json.dumps(send_user)
        file_data = md5_encode(file_data)
        sign = self.get_sign(self.send_contract_fn, self.mid, file_data, file_name, user_list, send_user)
        # sign = urllib.urlencode(sign)
        header = {
            "mid": self.mid,
            "filename": file_name,
            "userlist": user_list,
            "sign": urllib.quote(sign),
            "senduser": send_user,
            "Content-Type": "application/json; charset=UTF-8",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Connection": "keep-alive"
        }
        req = urllib2.Request(self.server+"/open/"+self.send_contract_fn, file_data, header)
        rsp = urllib2.urlopen(req).read()
        rsp_data = json.loads(rsp)
        return rsp_data

    def reg_user(self, mobile, name, user_type):
        body = {
            "content": {
                "mobile": mobile,
                "name": name,
                "userType": user_type
            }
        }
        sign = self.get_sign(self.reg_user_fn, self.mid, md5_encode(json.dumps(body["content"])))
        header = {
            "mid": self.mid,
            "sign": urllib.quote(sign)
        }
        req = urllib2.Request(self.server+"/open/"+self.reg_user_fn, body["content"], header)
        rsp = urllib2.urlopen(req).read()
        rsp_data = json.loads(rsp)
        return rsp_data

    def apply_key(mobile, username, identity, address):
        apply_user = {
            'userType': "1",  # 默认用户类型：个人
            'name': username,
            'password': mobile[-6:],  # 电话号码后六位
            'identityType': '0',  # 默认证件类型：身份证
            'identity': identity,
            'address': address,
            'duration': duration,
            'mobile': mobile
        }
        sign = self.get_sign('certificateApply.json', self.mid, md5_encode(json.dumps(body["content"])))
        header = {
            "mid": self.mid,
            "sign": urllib.quote(sign)
        }
        req = urllib2.Request(self.server+"/open/certificateApply.json", body["content"], header)
        rsp = urllib2.urlopen(req).read()
        rsp_data = json.loads(rsp)
        return rsp_data


if __name__ == "__main__":
    import traceback
    try:
        ssq = SSQClient(r"../../ssqsign.conf")
        receiver = {
            "name": "lhz",
            "isvideo": 0,
            "mobile":"18780661484",
            "usertype": 1,
            "Signimagetype": 0
        }
        sender = {
            "email": "bycxyw@163.com",
            "emailtitle": "title-test",
            "emailcontent": "boyacx-test",
            "sxdays": 2,
            "selfsign": 0,
            "name": "bycxyw@163.com",
            "mobile": "18683448261",
            "usertype": 2,
            "Signimagetype": 0,
            "UserfileType": 1
        }
        res = ssq.reg_user("18780661484", "lhz", "1")
        print res
        res = ssq.apply_key("18780661484", "lhz", "510525199011010052", "qwertyui")
        print res
        file_content = ""
        with open(r"D:\MyTest\TestContract.pdf", "r") as f:
            file_content = f.read()
        res = ssq.send_contract("TestContract.pdf", [receiver], sender, file_content)
        print res
        
    except Exception as e:
        print e.message
        print traceback.format_exc()

import requests
from Cryptodome.PublicKey import RSA
from base64 import b64encode
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256
import json
import random
import string
import time


def get_sign(sign_str):
    rsa_key = RSA.importKey(open('apiclient_key.pem').read())
    signer = pkcs1_15.new(rsa_key)
    digest = SHA256.new(sign_str.encode('utf8'))
    sign = b64encode(signer.sign(digest)).decode('utf-8')
    return sign

    
def create_payment_order(request):

    url = 'https://api.mch.weixin.qq.com/v3/pay/transactions/jsapi'
    data = {
        'appid': 'wxe228b2d8087cd3f0',     # appid
        'mchid': '1512281721',     # 商户号
        'description': '测试商品',     # 商品描述
        'out_trade_no': '123459000000',     # 你自己系统里的唯一订单号
        'notify_url': 'https://https://www.weixin.qq.com/wxpay/pay.php',    # 支付结果回调url
        "amount": {
            "total": 1,
            "currency": "CNY"
        },
        "payer": {"openid": 'of7oQ5br-GfSk5DG36ufsRuxw1vA'},    # 用户的openid
            
    }
    appid = 'wxe228b2d8087cd3f0'
    data = json.dumps(data)    # 只能序列化一次

    random_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))
    time_stamps = str(int(time.time()))    
    
    sign_str = f"POST\n{'/v3/pay/transactions/jsapi'}\n{time_stamps}\n{random_str}\n{data}\n"
    sign = get_sign(sign_str)
    serial_no = '197D07A690C41FE614F993ADD336FF491D80972B'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept': 'application/json',
        'User-Agent': 'python/3.8',
        'Authorization': 'WECHATPAY2-SHA256-RSA2048 ' + f'mchid="{1512281721}",nonce_str="{random_str}",signature="{sign}",timestamp="{time_stamps}",serial_no="{serial_no}"'
    }
    response = requests.post(url, data=data, headers=headers)
    # 还要使用平台证书对response进行验签，项目上线运行一定要写
    print(response.text)     # 返回{"prepay_id":"wx*************************"}

    res = {
        "message": dict(
            package='prepay_id='+response.json()['prepay_id'],
            timeStamp=time_stamps,
            nonceStr=random_str,
            paySign=get_sign(f"{appid}\n{time_stamps}\n{random_str}\n{'prepay_id='+response.json()['prepay_id']}\n"),
            signType='RSA',
        ),
        "meta": {
            "msg": "",
            "status": 200
        }
    }
    return res



# coding:utf-8
# python3.x

import rsa
# 生成秘钥
(pubkey,privkey) = rsa.newkeys(1024);

# 保存密钥
#with open('public.pem','w+') as f:
#    f.write(pubkey.save_pkcs1().decode())


#with open('private.pem','w+') as f:
#    f.write(privkey.save_pkcs1().decode())


# 导入密钥
#with open('public.pem','r') as f:
#    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

#with open('private.pem','r') as f:
#    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())


message = 'message'

# 公钥加密私钥解密
encrypt_message = rsa.encrypt(message.encode(), pubkey)
print(encrypt_message)
decode_message = rsa.decrypt(encrypt_message,privkey).decode()
print(decode_message)

message = '这是重要指令：...'
# 签名
crypto_email_text = rsa.sign(message.encode(), privkey, 'SHA-1')
print(crypto_email_text)
# 业务员同时收到指令明文、密文，然后用公钥验证，进行身份确认
sign = rsa.verify(message.encode(), crypto_email_text, pubkey)
print(sign)
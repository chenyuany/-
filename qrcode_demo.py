#coding=utf-8
#__author__ = 'chenyuanyuan'
import qrcode
from PIL import Image
# a = qrcode.make("http://www.baidu.com")
# a.save("百度.png")
qr =qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_Q,
    box_size=4,
    border=2
)
qr.add_data("http://www.baidu.com")
qr.make(fit=True)
# img = qr.make_image()
# img = img.convert("RGBA")
# icon = Image.open("E:/python小案例/2.jpg")
# # 计算logo的尺寸
# img_w,img_h = img.size
# size_w = int(img_w/2)
# size_h = int(img_h/2)
# # 比较并重新设置logo文件的尺寸
# icon_w,icon_h = icon.size
# if icon_w >size_w:
#     icon_w = size_w
# if icon_h > size_h:
#     icon_h = size_h
# icon = icon.resize((icon_w,icon_h),Image.ANTIALIAS)
# #计算logo的位置，并复制到二维码图像中
# w = int((img_w - icon_w)/2)
# h = int((img_h - icon_h)/2)
# icon = icon.convert("RGBA")
# img.paste(icon,(w,h),icon)
img = qr.make_image(fill_color="yellow", back_color="blue" )
#保存二维码
img.save("支付宝.png")
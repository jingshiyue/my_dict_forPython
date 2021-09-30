import random
#导入Image,ImageDraw,ImageFont模块
from PIL import Image,ImageDraw,ImageFont   # pip install Pillow
#定义使用Image类实例化一个长为120px,宽为30px,基于RGB的(255,255,255)颜色的图片

def drawYZM(font):
    img1=Image.new(mode="RGB",size=(90,30),color=(255,255,255))
    #实例化一支画笔
    draw1=ImageDraw.Draw(img1,mode="RGB")
    #定义要使用的字体
    font1=ImageFont.truetype(font,28)
    yzm = []
    for i in range(4):
        #每循环一次,从a到z中随机生成一个字母或数字
        #65到90为字母的ASCII码,使用chr把生成的ASCII码转换成字符
        #str把生成的数字转换成字符串
        char1=random.choice([chr(random.randint(65,90)),str(random.randint(0,9))])
        #每循环一次重新生成随机颜色
        yzm.append(char1)
        color1=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        #把生成的字母或数字添加到图片上
        #图片长度为120px,要生成5个数字或字母则每添加一个,其位置就要向后移动24px
        draw1.text([i*24,0],char1,color1,font=font1)
    #把生成的图片保存为"pic.png"格式
    try:
        with open("static/yzm.png","wb") as f:
            img1.save(f,format="png")
            yzmFilePath = "static/yzm.png"
    except:
        yzmFilePath = ''
    return "".join(yzm),yzmFilePath

r = drawYZM("C:\\WINDOWS\\Fonts\\SIMYOU.TTF")
print(r)
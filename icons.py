from PIL import Image

def convertImage(new_width, new_height, img,name):
   imagem = Image.open(img)
   imagem = imagem.resize((new_width, new_height), Image.ANTIALIAS)
   imagem.save('img' + str(name) + str(img)) # format may what u want ,*.png,*jpg,*.gif

#This one needs to be 1024 to 1024
icon = "birdIcon.png"


# IPHONE Notification 20x
convertImage(40,40,icon,"20@2x")
convertImage(60,60,icon,"20@3x")

#Iphone SpotLight 29
convertImage(58,58,icon,"29@2x")
convertImage(87,87,icon,"29@3x")


#Iphone SpotLight 40
convertImage(80,80,icon,"40@2x")
convertImage(120,120,icon,"40@3x")


#Iphone SpotLight 60
convertImage(120,120,icon,"60@2x")
convertImage(180,180,icon,"60@3x")


#Ipad Notifications 20
convertImage(20,20,icon,"20@1x")
convertImage(40,40,icon,"20@2x")

#Ipad Setthings 29
convertImage(29,29,icon,"29@1x")
convertImage(58,58,icon,"29@2x")


#Ipad SpotLight 40
convertImage(80,80,icon,"40@2x")
convertImage(40,40,icon,"40@1x")


#Ipad SpotLight 76
convertImage(76,76,icon,"76@1x")
convertImage(152,152,icon,"76@2x")

#Ipad Pro app 83.5
convertImage(167,167,icon,"83_5@2x")


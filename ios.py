from PIL import Image

def convertImage(new_width, new_height, img):
   imagem = Image.open(img)
   imagem = imagem.resize((new_width, new_height), Image.ANTIALIAS)
   imagem.save('img' + str(new_height) + str(img)) # format may what u want ,*.png,*jpg,*.gif


icon = "icon.png"

or1 = 'img1.png'
or2 = 'img2.png'
or3 = 'img3.png'
or4 = 'img4.png'
or5 = 'img.png'

#SPLASH
convertImage(750,1134,icon) # IPHONE 6
convertImage(1242,2208,icon) # IPHONE 6S
convertImage(2048,2732,icon) # IPAD PRO


#ICON
convertImage(1024,1024,icon) # IPAD PRO
convertImage(60,60,icon) # IPAD PRO
convertImage(120,120,icon) # IPAD PRO
convertImage(152,152,icon) # IPAD PRO
convertImage(76,76,icon) # IPAD PRO
convertImage(512,512,icon) # IPAD PRO
convertImage(180,180,icon) # IPAD PRO


#Iphone 4 inch
convertImage(640,1136,or1)
convertImage(640,1136,or2)
convertImage(640,1136,or3)
convertImage(640,1136,or4)
convertImage(640,1136,or5)

#Iphone 4.7 inch

convertImage(750,1334,or1)
convertImage(750,1334,or2)
convertImage(750,1334,or3)
convertImage(750,1334,or4)
convertImage(750,1334,or5)

#Iphone 5.5 inch

convertImage(1242,2208,or1)
convertImage(1242,2208,or2)
convertImage(1242,2208,or3)
convertImage(1242,2208,or4)
convertImage(1242,2208,or5)

#Iphoneair

convertImage(1536,2048,or1)
convertImage(1536,2048,or2)
convertImage(1536,2048,or3)
convertImage(1536,2048,or4)
convertImage(1536,2048,or5)

#apple watch

convertImage(312,390,or1)
convertImage(312,390,or2)
convertImage(312,390,or3)
convertImage(312,390,or4)
convertImage(312,390,or5)

#Ipad pro

convertImage(2048,2732,or1)
convertImage(2048,2732,or2)
convertImage(2048,2732,or3)
convertImage(2048,2732,or4)
convertImage(2048,2732,or5)
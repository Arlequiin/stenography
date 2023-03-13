from util import *
################################################################################################################
array = " abcdefghijklmnopqrstuvwxyz•&-–—@#!%^*()=+1234567890éèëēėùçïîà,.:'¶"
################################################################################################################
def encode_text(text,pic1):
   text_encoded = encode(text,array)
   text_encoded=to_list_of_indexes(text_encoded,array)
   l=[i for i in range(256) if i%3==0]
   d = {}
   for i in range(len(l)):  #creation of a dict \mathbb{N} -> 3n ; there is 86 solution of n%3=0 in [0;255], so enough to fit all the 61 indexes
      d[i]=l[i]
   for i in range(len(text_encoded)):
      text_encoded[i]=d[text_encoded[i]]
   from PIL import Image
   img=Image.open(pic1)
   pixels=img.load()
   width,height=img.size
   output=Image.new('RGB',(width,height))
   pixels_out=output.load()
   #print("Max char = ",width*height)
   if len(text)>width*height:
      print("Image is too small to handle all this text, max char allowed :",width*height,"\nHow many you have :",len(text))
   count=0
   for y in range(height):
      for x in range(width):
         #print(1,pixels[x,y])
         try:
            id=text_encoded[count]
         except:
            id=0
         value=pixels[x,y][0]+(id//3)
         if value>255:
           pixels[x,y][0]-(id//3)
         l_temp=list(pixels[x,y])
         l_temp[0]=value
         pixels_out[x,y]=tuple(l_temp)
         #print(2,pixels_out[x,y])
         count+=1
   #print(text_encoded)
   #output.show()
   output.save(pic1.replace(".png"," copy.png"))
   return pic1.replace(".png"," copy.png")

def decode_text(pic1):
   array = " abcdefghijklmnopqrstuvwxyz•&-–—@#!%^*()=+1234567890éèëêėùçïîà,.:'¶"
   l=[i for i in range(256) if i%3==0]
   from PIL import Image
   img=Image.open(pic1)
   pixels=img.load()
   width,height=img.size
   output=Image.open(pic1.replace(".png"," copy.png"))
   pixels_out=output.load()
   output_textm3=[]
   for y in range(height):
      for x in range(width):
         if pixels_out[x,y][0]!=pixels[x,y][0]:
            output_textm3.append(3*abs(pixels_out[x,y][0]-pixels[x,y][0]))
   #print(output_textm3)
   out = (multiple3_to_text(output_textm3,array))
   return out

text = """
Bonjour, Opération 451 :\n
• Rencontre demain 8h devant le portail
• Apportez des explosifs
• De l'essence
• Gants
• Cagoule
L'explosion aura lieu à 8h15, nous laissant donc 5 min pour nous échapper après les 10 min d'installation.
L'explosion sera déclenchée dès lors que la corde sera consumée par le feu. Il faudra préparer une corde de 10 m au moins et de 3 cm d'épaisseur dans l'objectif d'avoir au moins 5 min pour nous échapper.
Ensuite nous nous empresserons de prendre un train en direction de Tanger, bien-entendu ticket non-nominatif afin de ne laisser aucune traçabilité, annulant ainsi toute possible suspicion, nous payerons l'hotel avec trois jours d'avance pour faire croire que nous y sommes depuis le début de la semaine.
En comptant sur votre sérieux, votre rigueur et votre fidélité
— Membre 001
Projet NSI 2
"""
#print(encode_text(text,"static/3.png"))
#print(decode_text("static/3.png"))
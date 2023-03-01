array = "abcdefghijklmnopqrstuvwxyz•&-–—@#!%^*()=+ 1234567890éèëēėùçïî"

def to_list_of_indexes(charset):
   charset=charset.lower()
   list_of_indexes=[]
   for char in charset:
      if char in array:
       list_of_indexes.append(array.index(char))
      else:
         list_of_indexes.append(char)
   return list_of_indexes
def encode(charset,cesar_degree=3):
   indexes=to_list_of_indexes(charset)
   output=[]
   for index in indexes:
    if type(index)==int:
      diff=index+cesar_degree
      if diff>len(array)-1:
         diff=0+(diff-(len(array)))
      output.append(array[diff])
    else:
      output.append(index)
   output=''.join(output).capitalize()
   return output
def decode(charset,cesar_degree=-3):
   return encode(charset,cesar_degree)


text = """
Bonjour, Opération 451 :
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
print(decode(encode(text)))

from PIL import Image
img=Image.open("1.jpg")
pixels=img.load()
x,y=img.size
output=Image.new('RGB',(x,y))
pixels_out=output.load()

output.save("1 copy.jpg")
print("Done")
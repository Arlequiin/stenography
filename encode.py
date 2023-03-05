array = " abcdefghijklmnopqrstuvwxyz•&-–—@#!%^*()=+1234567890éèëēėùçïîà,.:'"

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
   charset=charset.replace("\n","ß")
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
   return encode(charset,cesar_degree).replace("ß","\n")

def multiple3_to_text(liste):
   l=[i for i in range(256) if i%3==0]
   for i in range(len(liste)):
         liste[i]=array[l.index(liste[i])]
   return decode(''.join(liste))
################################################################################################################
text = """Hello world"""
################################################################################################################
text_encoded = encode(text)
array+="ß"
text_encoded=to_list_of_indexes(text_encoded)
l=[i for i in range(256) if i%3==0]
d = {}
for i in range(len(l)):  #creation of a dict \mathbb{N} -> 3n ; there is 86 solution of n%3=0 in [0;255], so enough to fit all the 61 indexes
   d[i]=l[i]
for i in range(len(text_encoded)):
   text_encoded[i]=d[text_encoded[i]]
from PIL import Image
img=Image.open("1.png")
pixels=img.load()
width,height=img.size
output=Image.new('RGB',(width,height))
pixels_out=output.load()
print("Max char = ",width*height)
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
      l_temp=list(pixels[x,y])
      l_temp[0]=value
      pixels_out[x,y]=tuple(l_temp)
      #print(2,pixels_out[x,y])
      count+=1
print(text_encoded)
output.show()
output.save("1 copy.png")
print("Done")
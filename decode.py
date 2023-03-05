array = " abcdefghijklmnopqrstuvwxyz•&-–—@#!%^*()=+1234567890éèëēėùçïîà,.:'ß"

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
l=[i for i in range(256) if i%3==0]
from PIL import Image
img=Image.open("1.png")
pixels=img.load()
width,height=img.size
output=Image.open("1 copy.png")
pixels_out=output.load()
output_textm3=[]
for y in range(height):
   for x in range(width):
      if pixels_out[x,y][0]!=pixels[x,y][0]:
         output_textm3.append(3*(pixels_out[x,y][0]-pixels[x,y][0]))
print(output_textm3)
out = (multiple3_to_text(output_textm3))
print(out)
#[33, 24, 45, 45, 54, 9, 78, 54, 63, 45, 21]
array = "abcdefghijklmnopqrstuvwxyz•&-–—@#!%^*()=+ 1234567890éèëēėùçïîà,.:'"

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


text = """
Hello world
"""
text_encoded = encode(text)
print(text_encoded)
array+="ß"
text_encoded=to_list_of_indexes(text_encoded)
l=[i for i in range(256) if i%3==0]
d = {}
for i in range(len(l)):  #creation of a dict \mathbb{N} -> 3n ; there is 86 solution of n%3=0 in [0;255], so enough to fit all the 61 indexes
   d[i]=l[i]
for i in range(len(text_encoded)):
   text_encoded[i]=d[text_encoded[i]]
print(text_encoded)
from PIL import Image
img=Image.open("1.jpg")
pixels=img.load()
width,height=img.size
output=Image.new('RGB',(width,height))
pixels_out=output.load()
matrix=[]
matrix_indexes=[]
for y in range(height):
    matrix.append([])
    matrix_indexes.append([])
    for x in range(width):
        matrix[y].append(pixels[x,y])
        try:
          matrix_indexes[y].append(text_encoded[x])
        except:
           matrix_indexes[y].append(41)
for y in range(height):
   for x in range(width):
      pixels_out[x,y]=tuple([matrix[y][x][i]+(matrix_indexes[y][x]//3) for i in range(3)])
output.show()
output.save("1 copy.jpg")
print("Done")
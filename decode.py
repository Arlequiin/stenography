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


from PIL import Image
img,referentiel=Image.open("1 copy.jpg"),Image.open("1.jpg")
pixels,pixels_ref=img.load(),referentiel.load()
width,height=img.size
l=[]
for y in range(height):
    for x in range(width):
        print([pixels[x,y],pixels_ref[x,y]],[(pixels[x,y][i]-pixels_ref[x,y][i]) for i in range(3)])
        l.append(sum([(pixels[x,y][i]-pixels_ref[x,y][i]) for i in range(3)]))
#print(l)
print("Done")
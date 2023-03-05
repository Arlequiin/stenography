#array = " abcdefghijklmnopqrstuvwxyz•&-–—@#!%^*()=+1234567890éèëēėùçïîà,.:'"

def to_list_of_indexes(charset,array):
   charset=charset.lower()
   list_of_indexes=[]
   for char in charset:
      if char in array:
       list_of_indexes.append(array.index(char))
      else:
         list_of_indexes.append(char)
   return list_of_indexes
def encode(charset,array,cesar_degree=3):
   charset=charset.replace("\n","ß")
   indexes=to_list_of_indexes(charset,array)
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
def decode(charset,array,cesar_degree=-3):
   return encode(charset,array,cesar_degree).replace("ß","\n")

def multiple3_to_text(liste,array):
   l=[i for i in range(256) if i%3==0]
   for i in range(len(liste)):
         liste[i]=array[l.index(liste[i])]
   return decode(''.join(liste),array)
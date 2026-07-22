class ticket_codec:

    def encode(self,ticket_id):
      self.id=ticket_id
      self.x=list(ticket_id)
      self.checksum=0
      for i in range(len(self.x)):
         self.checksum+=ord(self.x[i])    ### here i have done a checksum that adds the asci of all letters and numbers then adds the sum after (-)  example abc123c-444
      self.barcode=ticket_id+'-'+str(self.checksum)
      return self.barcode
      

    def decode(self,barcode):
      self.test=barcode.split('-')
      self.target=(self.test[1])
      self.x=0
      for i in range(len(barcode)):
         if barcode[i]=='-':
            break
         else:
            self.x+=ord((barcode[i]))

      if(str(self.x)==self.target):  
         return "id is "+self.test[0]+" valid"
      else:
         return "not valid"      
      

# user 1
user1_id="ab1"
user1=ticket_codec()
x=user1.encode(user1_id)
print("user 1 barcode is ",x)
barcode=input("Enter barcode to enter ")
print(user1.decode(barcode))

# user 2
user2_id="ds1"
user2=ticket_codec()
y=user2.encode(user2_id)
print("user 2 barcode is ",y)
barcode=input("Enter barcode to enter ")
print(user2.decode(barcode))

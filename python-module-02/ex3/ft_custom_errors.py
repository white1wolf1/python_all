class GardenError(Exception):
   def  __init__(self,error_message = "hatanın bos olduğu hata mesajı"):
       super().__init__(error_message)



class Deneme:
    def deneme():
        try:
            raise GardenError(" verilen mesaj") 
        except GardenError as e:
            print(e)


    
if __name__ == "__main__":
    Deneme.deneme()
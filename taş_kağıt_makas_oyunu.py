import random
taş= """   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""" 
kağıt="""   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
makas="""    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
oyun_görselleri=[taş,kağıt,makas]
oyuncunun_yanıtı=int(input("Hangisini seçersiniz? Taş için 0, Kağıt için 1 veya Makas için 2 yazın\n"))

bilgisayarın_yanıtı=random.randint(0, 2)

if oyuncunun_yanıtı<=2 or oyuncunun_yanıtı>=0:
    print ("oyuncunun yanıtı:")
    print(oyun_görselleri[oyuncunun_yanıtı])
    print("bilgisayarın yanıtı")  
    print(oyun_görselleri[bilgisayarın_yanıtı])  


if oyuncunun_yanıtı== bilgisayarın_yanıtı:
    print ("Berabere")
elif oyuncunun_yanıtı==0 and bilgisayarın_yanıtı==1:
    print("Kaybettin:)")    
elif oyuncunun_yanıtı==0 and bilgisayarın_yanıtı==2:
    print("Kazandınnn:(")

elif oyuncunun_yanıtı==1 and bilgisayarın_yanıtı==2:
    print("Kaybettin:)")    
elif oyuncunun_yanıtı==1 and bilgisayarın_yanıtı==0:
    print("Kazandınnn:(")

elif oyuncunun_yanıtı==2 and bilgisayarın_yanıtı==0:
    print("Kaybettin:)")    
elif oyuncunun_yanıtı==2 and bilgisayarın_yanıtı==1:
    print("Kazandınnn:(")    
else:
    print("Geçersiz sayı girdiniz.")    
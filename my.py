meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
             "ROFL": "bir şakaya karşılık cevap",
             "SHEESH": "onaylamak",
             "CREEPY": "korkunç",
             "AGGRO": "agresifleşmek/sinirlenmek",
 }

word = input("Merhaba bilmediğiniz yeni nesil bir kelime var mı?Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
   print (word,"Kelimesinin anlamı,",meme_dict)
else:
    print ("Başka bir kelime deneyin")

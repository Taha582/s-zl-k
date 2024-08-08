meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "FAKE":"gerçek olmayan, sahte",
            "TROLL":"ironik bir şey",
            "ROFL":"bir şakaya karşılık cevap",
            "SHEESH":"onaylamamak",
            "CREEPY":"korkunç",
            "AGGRO":"agresifleşmek/sinirlenmek",
            }
while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print("girdiğiniz kelimenin anlamı:",meme_dict[word])
    else:
        print("Malesef aradığınız kelimeyi bulamadım")

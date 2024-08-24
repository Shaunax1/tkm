import random

def tas_kagit_makas_Eyüp_Kavak():
  print("Taş,Kağıt,Makas Oyununa Hoşgeldiniz")
  print("Oyun 3 turdan oluşur. İlk iki turu kazanan oyunu kazanır.")
  print("Oyundan çıkmak için 'e' tuşuna basınız.")

  tkm = ["taş","kağıt","makas"]

  while True:
      player1_score = 0
      player2_score = 0
      round_counter = 0

      while player1_score < 2 and player2_score < 2:
          player1_choice = input("Lütfen taş, kağıt veya makas seçin: ").lower()

          if player1_choice == 'e':
                print("Oyundan çıkılıyor...")
                return

          if player1_choice not in tkm:
                print("Listede olmayan bir değer girdiniz, tekrar deneyin.")
                continue

          player2_choice = random.choice(tkm)
          print(f"Bilgisayarın Seçimi : {player2_choice}")

          if player1_choice == player2_choice:
            print("İkinizde aynı değeri seçtiniz")

          elif player1_choice == "taş" and player2_choice == "makas":
            print("Kazanan Oyuncu")
            player1_score +=1

          elif player1_choice == "kağıt" and player2_choice == "taş":
            print("Kazanan Oyuncu")
            player1_score +=1

          elif player1_choice == "makas" and player2_choice == "kağıt":
            print("Bu turun kazananı oyuncu")
            player1_score +=1

          else:
            print("Bu turun kazananı bilgisayar")
            player2_score +=1

          round_counter +=1
          print(f"Tur : {round_counter} Oyuncu : {player1_score} - Bilgisayar : {player2_score}")

      if player1_score == 2:
            print("Tebrikler, oyunu kazandınız!")
      else:
            print("Bilgisayar oyunu kazandı!")


      player1_NewGame = input("Başka bir oyun oynamak ister misiniz? evet/hayır: ").lower()
      if player1_NewGame != 'evet':
          print("Oyundan çıkılıyor...")
          break

      player2_NewGame = random.choice(['evet', 'hayır'])
      print(f"Bilgisayar başka bir oyun oynamak istiyor mu? {player2_NewGame}")
      if player2_NewGame != 'evet':
          print("Bilgisayar oyunu sonlandırmak istedi. Oyundan çıkılıyor...")
          break

tas_kagit_makas_Eyüp_Kavak()
import random

def guess_it():
    print("=== SAYI TAHMİN OYUNU ===")
    number = random.randint(1,100)
    guess_time = 0
    guesses = []
    
    while True:
        guess_time += 1
        guess = int(input("Your guess: "))
        print( f"{guess_time}. denemen.")
        guesses.append(guess)

        if guess > number:
            print("Daha küçük bir sayı dene.")
        elif guess < number:
            print("Daha büyük bir sayı dene.")
        else:
            n = 1
            print("🎉 Tebrikler!")
            print(f"Toplam deneme sayısı: {guess_time}")
            print("Doğru sayı: ", number, "\n")
            print("Senin tahminlerin:\n")
            for i in guesses:
                print(n,")",i,sep="")
                n += 1
            break
    
while True:
    guess_it()
    answer = input("Tekrar oynamak ister misin? (e/h)")
    if answer.lower() == "h":
        break
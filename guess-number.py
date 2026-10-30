import random

x = True
while x == True:
    random_number = random.randint(1 , 100)
    i = 1
    while i <= 5:
#کنترل حدس ورودی
        try:
            guess = int(input("عدد مورد نظر خود را واردکنید(بین 0 تا 100):"))
            if guess < 1 or guess > 100:
                print("حدست باید بین صفر و صد باشه!")
                continue
        except ValueError:
            print("فقط باید عدد وارد کنی!")
            continue
#نمایش تعداد تلاش ها
        print(f"تلاش {i} از 5")
        print(f"جان باقی مانده:{5 - i}")
#بزرگتر یا کوچکتر بودن حدس بر اساس عدد رندوم
        if guess > random_number:
            print("بزرگتر گفتی!")
        elif guess < random_number:
            print("کوچکتر گفتی!")
        elif guess == random_number:
            print("باریکلا!درست گفتی")
            break
#کمک بر اساس فاصله حدس و عدد رندوم
        difference = abs(guess - random_number)
    
        if difference <= 5:
            print("چقدر فاصله داری؟خیلی نزدیکی!")
        elif 5 < difference <= 15:
            print("چقدر فاصله داری؟نزدیکی!ولی فاصله داری")
        elif difference > 15:
            print("چقدر فاصله داری؟خیلی دووووری!")
        i += 1
#رتبه بندی
       
    if i == 1:
        print("رتبه شما : نمونه ای")
    elif i == 2:
        print("رتبه شما : بسیار خوبی")
    elif i == 3:
        print("رتبه شما : خوب")
    elif i == 4:
        print("رتبه شما : قابل قبولی")
    elif i == 5:
        print("رتبه شما : با شانس بردی")
    elif i > 5:
        print('باختی')
        print(f"عدد مخفی : {random_number}")
        
#بازی مجدد 
    while True:
        again = str(input("میخوای دوباره بازی کنی؟(y/n)")).lower()   
        if again == 'y':
            print("بریم دست بعد")
            break
        elif again == 'n':
            print("امیدوارم بهت خوش گذشته باشه")
            x = False
            break     
        else:
            print("فقط y یا n وارد کن")

        




        
        
    
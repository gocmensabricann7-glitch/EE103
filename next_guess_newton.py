# 1. Kullanıcıdan x değerini al
x = float(input("What x to find the square root of? "))

# 2. Kullanıcıdan başlangıç tahminini (g) al
g = float(input("What guess to start with? "))

# 3. Mevcut tahminin karesini yazdır
print("Current estimate square:", g ** 2)

# 4. Sonraki tahmini hesapla (Newton's method)
next_guess = g - (g**2 - x) / (2 * g)

# 5. Sonraki tahmini yazdır
print("Next guess:", next_guess)
import re

print("=" * 50)
print("      🔐 ŞİFRƏ GÜCÜ TEST EDİCİSİ")
print("=" * 50)

def sifre_gucunu_yoxla(sifre):
    """Şifrənin gücünü qiymətləndirir"""
    bal = 0
    mesajlar = []
    
    # Uzunluq yoxlaması
    if len(sifre) >= 12:
        bal += 2
        mesajlar.append("✅ Uzunluq: çox yaxşı (12+ simvol)")
    elif len(sifre) >= 8:
        bal += 1
        mesajlar.append("✅ Uzunluq: yaxşı (8-11 simvol)")
    else:
        mesajlar.append("❌ Uzunluq: çox qısa (minimum 8 simvol)")
    
    # Böyük hərf yoxlaması
    if re.search(r'[A-Z]', sifre):
        bal += 1
        mesajlar.append("✅ Böyük hərf: var")
    else:
        mesajlar.append("❌ Böyük hərf: yoxdur")
    
    # Kiçik hərf yoxlaması
    if re.search(r'[a-z]', sifre):
        bal += 1
        mesajlar.append("✅ Kiçik hərf: var")
    else:
        mesajlar.append("❌ Kiçik hərf: yoxdur")
    
    # Rəqəm yoxlaması
    if re.search(r'[0-9]', sifre):
        bal += 1
        mesajlar.append("✅ Rəqəm: var")
    else:
        mesajlar.append("❌ Rəqəm: yoxdur")
    
    # Xüsusi simvol yoxlaması
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', sifre):
        bal += 1
        mesajlar.append("✅ Xüsusi simvol: var")
    else:
        mesajlar.append("❌ Xüsusi simvol: yoxdur")
    
    # Ümumi şifrələr yoxlaması
    umumii_sifreler = ["123456", "password", "12345678", "qwerty", "abc123", "111111", "azerbaycan"]
    if sifre.lower() in umumii_sifreler:
        bal = 0
        mesajlar = ["⚠️ TƏHLÜKƏLİ! Bu çox tanınmış şifrədir!"]
    
    # Nəticə
    print("\n" + "-" * 40)
    for msg in mesajlar:
        print(msg)
    print("-" * 40)
    
    if bal >= 5:
        return "🔐 GÜCLÜ ŞİFRƏ!"
    elif bal >= 3:
        return "⚠️ ORTA SƏVİYYƏLİ ŞİFRƏ"
    else:
        return "❌ ZƏİF ŞİFRƏ! Daha təhlükəsiz şifrə seçin"

# Əsas proqram
while True:
    print("\n" + "=" * 50)
    sifre = input("🔑 Şifrə daxil edin (və ya 'çıx' yazın): ")
    
    if sifre.lower() == 'çıx':
        print("Proqram bağlanır. Təhlükəsiz qalın! 🔒")
        break
    
    if sifre == "":
        print("Xəta: Şifrə boş ola bilməz!")
        continue
    
    netice = sifre_gucunu_yoxla(sifre)
    print(f"\n{netice}")
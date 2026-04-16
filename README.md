# Qisqa Ko'paytirish Formulalari - Generator

Bu loyiha matematika: qisqa ko'paytirish formulalarini amaliyot qilish uchun misollar yaratadi. Har bir qo'lyozma 40 tadan misoldan iborat bo'lib, 4 ta qiyinlik darajasida: Oson, O'rtacha, Qiyin va Juda Qiyin.

---

## Nima uchun kerak?

Maktabda yoki mustaqil tayyorlanishda qisqa ko'paytirish formulalarini yodlash va amaliyot qilish muhim. Bu generator har safar yangi misollar yaratadi, shuning uchun cheksiz mashq qilish mumkin. Har bir formula uchun misollar avtomatik generated qilinadi.

---

## Loyiha tarkibi

```
math_worksheets/
├── generator.py          # Asosiy Python skript - barcha ishlarni shu yerdan boshqarasiz
├── generator_v4.py    # Variant generator (boshqa usulda misollar yaratadi)
├── template.tex        # LaTeX hujjat shabloni (sarlavha, sahifa tartibi)
├── README.md          # Hujjat (mana shu fayl)
├── output/            # AVTOMATIK yaratiladi - Generator ishganda paydo bo'ladi
│   ├── worksheet_1.pdf # Qo'lyozma N1 (savollar + javoblar)
│   ├── worksheet_1.tex
│   ├── worksheet_2.pdf
│   └── ... 10 ta qo'lyozmagacha
├── barcha_misollar.pdf    # AVTOMATIK - barcha 10 ta qo'lyozma bitta PDF faylda
├── Qisqa_kopaytirish_mashqlar.pdf # Mashqlar PDF
└── .git/              # Git repositoriyalar uchun
```

---

## Ishga tushirish

### Linux yoki macOS

```bash
cd /content/math_worksheets
python3 generator.py
```

### Windows

```cmd
cd C:\Users\Siz\content\math_worksheets
python generator.py
```

### Natija

Dastur ishga tushganda:
1. `output/` papkasi yaratiladi
2. 10 ta alohida PDF fayl yaratiladi (worksheet_1.pdf dan worksheet_10.pdf gacha)
3. `barcha_misollar.pdf` yaratiladi - barcha qo'lyozmalar bitta faylda

Terminalda shu xabarlar chiqadi:
```
Qo'shildi: Qo'lyozma N1 (40 ta misol)
Qo'shildi: Qo'lyozma N2 (40 ta misol)
...
Yaratildi: barcha_misollar.pdf (400 ta misol)
```

---

## Misollar tarkibi

Har bir qo'lyozmada **40 ta misol**, 4 ta darajada:

### Daraja 1 — Oson (10 ta misol)

| Formula | Misol | Yechim |
|---------|-------|--------|
| $(a+b)^2$ | $(3x+5)^2$ | $9x^2+30x+25$ |
| $(a-b)^2$ | $(7x-2)^2$ | $49x^2-28x+4$ |
| $a^2-b^2$ | $9^2-4^2$ | $(9+4)(9-4)$ |

Bu darajada faqat 2 hadli kvadrat formulalar. Sonlar 2 dan 9 gacha.

### Daraja 2 — O'rtacha (10 ta misol)

| Formula | Misol | Yechim |
|---------|-------|--------|
| $(a+b)^3$ | $(2x+3)^3$ | $8x^3+36x^2+54x+27$ |
| $(a-b)^3$ | $(4x-1)^3$ | $64x^3-48x^2+12x-1$ |
| $a^3+b^3$ | $2^3+5^3$ | $(2+5)(4-10+25)$ |
| $a^3-b^3$ | $7^3-3^3$ | $(7-3)(49+21+9)$ |
| $(x+a)(x+b)$ | $(x+4)(x-7)$ | $x^2-3x-28$ |

Bu darajada kub va uch hadli ko'paytirish formulalari. Sonlar -9 dan 9 gacha.

### Daraja 3 — Qiyin (10 ta misol)

| Formula | Misol | Yechim |
|---------|-------|--------|
| $(ax+by)^2$ | $(5x+2y)^2$ | $25x^2+20xy+4y^2$ |
| $(ax-by)^2$ | $(3x-4y)^2$ | $9x^2-24xy+16y^2$ |
| $(ax)^2-(by)^2$ | $(6x)^2-(2y)^2$ | $(6x+2y)(6x-2y)$ |
| $(a+b)^2+(a-b)^2$ | $(4+3)^2+(4-3)^2$ | $2(16+9)=50$ |
| $(a+b)^2-(a-b)^2$ | $(5+2)^2-(5-2)^2$ | $4*5*2=40$ |

Bu darajada ikki o'zgaruvchili formulalar. Harfli koeffitsientlar bor.

### Daraja 4 — Juda Qiyin (10 ta misol)

| Formula | Misol | Yechim |
|---------|-------|--------|
| $(ax+by)^3$ | $(2x+3y)^3$ | $8x^3+36x^2y+54xy^2+27y^3$ |
| $(ax-by)^3$ | $(3x-2y)^3$ | $27x^3-54x^2y+36xy^2-8y^3$ |
| $(x+a)(x+b)(x+c)$ | $(x+1)(x-3)(x+5)$ | $x^3+3x^2-13x-15$ |
| $(a+b+c)^2$ | $(2+3+4)^2$ | $4+9+16+12+16+24$ |

Bu darajada uch o'zgaruvchili va uch hadli ko'paytirish formulalari.

---

## Qanday ishlaydi?

### 1. generate_worksheet() funksiyasi

Bu funksiya tasodifiy misollar yaratadi.

```python
def generate_worksheet(seed_val, per_diff=10):
    # seed_val - har safar bir xil ketma-ketlik uchun
    # per_diff - har darajada nechta misol
    
    # 1. 4 ta daraja uchun alohida
    # 2. Har bir formuladan tasodifiy tanlab misol yaratadi
    # 3. Aralashtiradi (shuffle)
    return problems  # ro'yxat qaytaradi
```

### 2. make_problem() funksiyasi

Har bir formula uchun misol yaratadi.

```python
def make_problem(fkey, diff):
    # fkey - formula kaliti (masalan: "kvadrat_yigindi")
    # diff - qiyinlik darajasi (1-4)
    
    # 1. Tasodifiy sonlar tanlaydi
    # 2. Savolni yasalaydi
    # 3. Jordani hisoblaydi
    return {"question": q, "answer": javob, "difficulty": diff}
```

### 3. build_pdf_single() funksiyasi

PDF yaratadi.

```python
def build_pdf_single(problems, num, pdf=None):
    # 1. Yangi sahifa qo'shadi
    # 2. Sarlavha yozadi
    # 3. Misollarni chiqaradi (daraja bo'yicha guruhlangan)
    # 4. Javoblar sahifasini qo'shadi
    return pdf
```

---

## Moslashtirish

### Yangi formula qo'shish

`generator.py` da `FORMULA_TEMPLATES` ro'yxatiga qo'shing:

```python
("mening_formulam", r"formula LaTeX ko'rinishi", daraja),
```

Keyin `make_problem()` funksiyasida ishlov qo'shing:

```python
elif fkey == "mening_formulam":
    q = f"({a}x + {b})^2"  # savol
    ans = f"{a**2}x^2 + {2*a*b}x + {b**2}"  # javob
```

### Misollar sonini o'zgartirish

```python
# generator.py da
for n in range(1, 11):  # 10 o'rniga 20 ta qo'lyozma
    problems = generate_worksheet(seed_val=n * 777, per_diff=10)
```

### Seed o'zgartirish

```python
seed_val=n * 777  # boshqa son qo'ying
# yoki
seed_val=None  # to'liq tasodifiy har safar
```

---

## Talablar

### Python

Python 3.6+ kerak.

```bash
# Ubuntu/Debian
sudo apt-get install python3

# macOS
brew install python3

# Windows
# https://www.python.org/download/
```

Python paketlari:

```bash
pip install fpdf2
```

### LaTeX (ixtiyoriy)

PDF yaratish uchun LaTeX kerak (pdflatex). Agar LaTeX o'rnatilmagan bo'lsa, fpdf2 kutubxonasi PDF yaratadi.

```bash
# Ubuntu/Debian
sudo apt-get install texlive-latex-base

# macOS
brew install --cask mactex

# Windows
# https://miktex.org/download
```

---

## Xatolar va yechimlar

### "ModuleNotFoundError: No module named 'fpdf'"

```bash
pip install fpdf2
```

### "pdflatex: command not found"

LaTeX o'rnatilmagan. Yuqoridagi "Talablar" bo'limiga qarang. Yoki fpdf2 ishlating - u LaTeX siz ham ishlaydi.

### Bo'sh PDF chiqadi

`output/` papkasida `.log` faylini tekshiring. U yerda LaTeX xatolari bo'ladi.

---

## Ishlatish misollari

### 1. Maktabda

O'qituvchi har hafta yangi qo'lyozma tarqatadi. Har bir o'quvchi o'z qo'lyozmasini oladi va mustaqil ishlaydi.

### 2. Uyda

O'quvchi o'zi misollar yaratib, amaliyot qiladi. Javoblarni keyin tekshiradi.

### 3. Takrorlash

Har bir formula uchun 10-20 ta misol ishlash orqali formula yodga olinadi.

---

## Foydali formulalar ro'yxati

### Kvadrat formulalari

1. $(a+b)^2 = a^2 + 2ab + b^2$
2. $(a-b)^2 = a^2 - 2ab + b^2$
3. $a^2 - b^2 = (a+b)(a-b)$

### Kub formulalari

4. $(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$
5. $(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$
6. $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$
7. $a^3 - b^3 = (a-b)(a^2 + ab + b^2)$

### Kompleks formulalar

8. $(ax+by)^2 = a^2x^2 + 2abxy + b^2y^2$
9. $(ax+by)^3 = a^3x^3 + 3a^2bx^2y + 3ab^2xy^2 + b^3y^3$
10. $(x+a)(x+b) = x^2 + (a+b)x + ab$
11. $(a+b+c)^2 = a^2 + b^2 + c^2 + 2ab + 2ac + 2bc$

---

## GitHub havolasi

https://github.com/SardorCyberSafe/math_worksheets

---

## Muallif

SardorCyberSafe

Bu loyiha o'zbek tilidagi matematik mashqlar generatori. Qisqa ko'paytirish formulalari (kvadrat va kub) bo'yicha amaliyot uchun mo'ljallangan. Har qanday taklif va tuzatishlar uchun GitHub Issues bo'limida yozishingiz mumkin.

---

## License

MIT License - erkin foydalaning va o'zgartiring!
#!/usr/bin/env python3
"""
Qisqa Ko'paytirish Formulalari - Generator
LaTeX orqali PDF yaratish
"""

import random
import os
import subprocess
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")
TEMPLATE_PATH = os.path.join(SCRIPT_DIR, "template.tex")


def g(d, sign=True, zeron=False):
    if d == 1:
        vals = list(range(2, 10))
    elif d == 2:
        vals = list(range(-9, 10))
    elif d == 3:
        vals = list(range(-12, 13))
    else:
        vals = list(range(-15, 16))
    if not zeron:
        vals = [v for v in vals if v != 0]
    if sign:
        return random.choice(vals)
    return random.choice([v for v in vals if v > 0])


def make_problem(fkey, diff):
    a = g(diff, True)
    b = g(diff, True)
    c = g(diff, True) if fkey in ["uch_o_z_1", "yigindi_kv"] else None

    if fkey == "kvadrat_yigindi":
        q = f"({a}x + {b})^2"
        if a == 1:
            q = f"(x + {b})^2"
        if a == -1:
            q = f"(-x + {b})^2"
        if b == 0:
            q = f"({a}x)^2"
        ab2 = 2 * a * b
        ans = f"{a**2}x^2"
        if ab2 != 0:
            ans += f" + {ab2}x" if ab2 > 0 else f" - {abs(ab2)}x"
        ans += f" + {b**2}"
        if b == 0:
            ans = f"{a**2}x^2"
        if a == 1 and b > 0:
            ans = f"x^2 + {2 * b}x + {b**2}"
        if a == 1 and b < 0:
            ans = f"x^2 - {2 * abs(b)}x + {b**2}"

    elif fkey == "kvadrat_ayirma":
        abs_b = abs(b)
        q = f"({a}x - {abs_b})^2"
        if a == 1:
            q = f"(x - {abs_b})^2"
        if a == -1:
            q = f"(-x - {abs_b})^2"
        ab2 = 2 * a * abs_b
        ans = f"{a**2}x^2"
        if ab2 != 0:
            ans += f" - {ab2}x"
        ans += f" + {b**2}"

    elif fkey == "kvadrat_ayirma_f":
        q = f"{a}^2 - {b}^2"
        ans = f"({a}+{b})({a}-{b})"

    elif fkey == "kub_yigindi":
        q = f"({a}x + {b})^3"
        if a == 1:
            q = f"(x + {b})^3"
        if b == 0:
            q = f"({a}x)^3"
        a3, a2b, ab2, b3 = a**3, 3 * a**2 * b, 3 * a * b**2, b**3
        ans = f"{a3}x^3"
        if a2b > 0:
            ans += f" + {a2b}x^2"
        elif a2b < 0:
            ans += f" - {abs(a2b)}x^2"
        if ab2 > 0:
            ans += f" + {ab2}x"
        elif ab2 < 0:
            ans += f" - {abs(ab2)}x"
        if b3 != 0:
            ans += f" + {b3}"
        if b == 0:
            ans = f"{a3}x^3"

    elif fkey == "kub_ayirma":
        abs_b = abs(b)
        q = f"({a}x - {abs_b})^3"
        if a == 1:
            q = f"(x - {abs_b})^3"
        if b == 0:
            q = f"({a}x)^3"
        a3, a2b, ab2, b3 = a**3, 3 * a**2 * abs_b, 3 * a * b**2, b**3
        ans = f"{a3}x^3 - {a2b}x^2"
        if ab2 > 0:
            ans += f" + {ab2}x"
        elif ab2 < 0:
            ans += f" - {abs(ab2)}x"
        if b3 != 0:
            ans += f" - {b3}"
        if b == 0:
            ans = f"{a3}x^3"

    elif fkey == "kub_yigindi_f":
        q = f"{a}^3 + {b}^3"
        ans = f"({a}+{b})({a}^2{a * b}+{b}^2)".replace("+-", "-").replace("+", "+")

    elif fkey == "kub_ayirma_f":
        q = f"{a}^3 - {b}^3"
        ans = f"({a}-{b})({a}^2+{a * b}+{b}^2)"

    elif fkey == "kompleks_kv_yig":
        q = f"({a}x + {b}y)^2"
        if a == 1:
            q = f"(x + {b}y)^2"
        if b == 1:
            q = f"({a}x + y)^2"
        if a == 1 and b == 1:
            ans = "x^2 + 2xy + y^2"
        else:
            ans = f"{a**2}x^2 + {2 * a * b}xy + {b**2}y^2"

    elif fkey == "kompleks_kv_ayr":
        abs_b = abs(b)
        q = f"({a}x - {abs_b}y)^2"
        if a == 1:
            q = f"(x - {abs_b}y)^2"
        if b == 1:
            q = f"({a}x - y)^2"
        if a == 1 and b == 1:
            ans = "x^2 - 2xy + y^2"
        else:
            ans = f"{a**2}x^2 - {2 * a * abs_b}xy + {b**2}y^2"

    elif fkey == "kompleks_fark_f":
        abs_b = abs(b)
        q = f"({a}x)^2 - ({abs_b}y)^2"
        if a == 1:
            q = f"x^2 - ({abs_b}y)^2"
        if b == 1:
            q = f"({a}x)^2 - y^2"
        ans = f"({a}x+{abs_b}y)({a}x-{abs_b}y)"

    elif fkey == "uchinchi_kompl_yig":
        q = f"({a}x + {b}y)^3"
        if a == 1:
            q = f"(x + {b}y)^3"
        if b == 1:
            q = f"({a}x + y)^3"
        a3, a2b, ab2, b3 = a**3, 3 * a**2 * b, 3 * a * b**2, b**3
        ans = f"{a3}x^3"
        if a2b > 0:
            ans += f" + {a2b}x^2y"
        elif a2b < 0:
            ans += f" - {abs(a2b)}x^2y"
        if ab2 > 0:
            ans += f" + {ab2}xy^2"
        elif ab2 < 0:
            ans += f" - {abs(ab2)}xy^2"
        if b3 > 0:
            ans += f" + {b3}y^3"
        elif b3 < 0:
            ans += f" - {abs(b3)}y^3"

    elif fkey == "uchinchi_kompl_ayr":
        abs_b = abs(b)
        q = f"({a}x - {abs_b}y)^3"
        if a == 1:
            q = f"(x - {abs_b}y)^3"
        if b == 1:
            q = f"({a}x - y)^3"
        a3, a2b, ab2, b3 = a**3, 3 * a**2 * abs_b, 3 * a * b**2, b**3
        ans = f"{a3}x^3"
        if a2b > 0:
            ans += f" - {a2b}x^2y"
        elif a2b < 0:
            ans += f" + {abs(a2b)}x^2y"
        if ab2 > 0:
            ans += f" + {ab2}xy^2"
        elif ab2 < 0:
            ans += f" - {abs(ab2)}xy^2"
        if b3 > 0:
            ans += f" - {b3}y^3"
        elif b3 < 0:
            ans += f" + {abs(b3)}y^3"

    elif fkey == "kop_o_z_1":
        q = f"(x + {a})(x + {b})"
        s, p = a + b, a * b
        ans = f"x^2 + {s}x + {p}"

    elif fkey == "kop_o_z_2":
        q = f"(x - {abs(a)})(x - {abs(b)})"
        s, p = abs(a) + abs(b), a * b
        ans = f"x^2 - {s}x + {p}"

    elif fkey == "uch_o_z_1":
        q = f"(x + {a})(x + {b})(x + {c})"
        s1 = a + b + c
        s2 = a * b + a * c + b * c
        sp = a * b * c
        ans = f"x^3 + {s1}x^2 + {s2}x + {sp}"

    elif fkey == "yigindi_kv":
        q = f"({a} + {b} + {c})^2"
        a2, b2, c2, ab, ac, bc = a**2, b**2, c**2, 2 * a * b, 2 * a * c, 2 * b * c
        parts = [str(x) for x in [a2, b2, c2, ab, ac, bc] if x != 0]
        ans = "+".join(parts) if parts else "0"

    elif fkey == "ikki_kv_yig":
        a, b = abs(g(2, False)), abs(g(2, False))
        q = f"({a}+{b})^2+({a}-{b})^2"
        ans = f"2({a}^2+{b}^2) = {2 * a**2}+{2 * b**2}"

    elif fkey == "ikki_kv_ayr":
        a, b = abs(g(2, False)), abs(g(2, False))
        q = f"({a}+{b})^2-({a}-{b})^2"
        ans = f"4*{a}*{b} = {4 * a * b}"

    else:
        q, ans = "?", "?"

    return {"question": q, "answer": ans, "difficulty": diff}


FORMULA_TEMPLATES = [
    ("kvadrat_yigindi", r"(a+b)^2 = a^2+2ab+b^2", 1),
    ("kvadrat_ayirma", r"(a-b)^2 = a^2-2ab+b^2", 1),
    ("kvadrat_ayirma_f", r"a^2-b^2 = (a+b)(a-b)", 1),
    ("kub_yigindi", r"(a+b)^3 = a^3+3a^2b+3ab^2+b^3", 2),
    ("kub_ayirma", r"(a-b)^3 = a^3-3a^2b+3ab^2-b^3", 2),
    ("kub_yigindi_f", r"a^3+b^3 = (a+b)(a^2-ab+b^2)", 2),
    ("kub_ayirma_f", r"a^3-b^3 = (a-b)(a^2+ab+b^2)", 2),
    ("kompleks_kv_yig", r"(ax+by)^2 = a^2x^2+2abxy+b^2y^2", 3),
    ("kompleks_kv_ayr", r"(ax-by)^2 = a^2x^2-2abxy+b^2y^2", 3),
    ("kompleks_fark_f", r"(ax)^2-(by)^2 = (ax+by)(ax-by)", 3),
    ("uchinchi_kompl_yig", r"(ax+by)^3", 4),
    ("uchinchi_kompl_ayr", r"(ax-by)^3", 4),
    ("kop_o_z_1", r"(x+a)(x+b) = x^2+(a+b)x+ab", 2),
    ("kop_o_z_2", r"(x-a)(x-b) = x^2-(a+b)x+ab", 2),
    ("uch_o_z_1", r"(x+a)(x+b)(x+c)", 4),
    ("yigindi_kv", r"(a+b+c)^2", 4),
    ("ikki_kv_yig", r"(a+b)^2+(a-b)^2 = 2(a^2+b^2)", 3),
    ("ikki_kv_ayr", r"(a+b)^2-(a-b)^2 = 4ab", 3),
]

DIFF_NAMES = {1: "Oson", 2: "O'rtacha", 3: "Qiyin", 4: "Juda Qiyin"}


def generate_worksheet(seed_val, per_diff=10):
    random.seed(seed_val)
    problems = []
    for diff in [1, 2, 3, 4]:
        templates = [(k, d) for k, _, d in FORMULA_TEMPLATES if d == diff]
        for _ in range(per_diff):
            k, d = random.choice(templates)
            problems.append(make_problem(k, d))
    random.shuffle(problems)
    return problems


def build_latex(problems, num):
    by_diff = {1: [], 2: [], 3: [], 4: []}
    for p in problems:
        by_diff[p["difficulty"]].append(p)

    questions_tex = ""
    for diff in [1, 2, 3, 4]:
        if not by_diff[diff]:
            continue
        questions_tex += f"\\subsection*{{{DIFF_NAMES[diff]}}}\n"
        questions_tex += "\\begin{{enumerate}}\n"
        for p in by_diff[diff]:
            questions_tex += f"\\item $ {p['question']} $\n"
        questions_tex += "\\end{enumerate}\n"
        questions_tex += "\\vspace{{0.3cm}}\n"

    answers_tex = ""
    for diff in [1, 2, 3, 4]:
        if not by_diff[diff]:
            continue
        answers_tex += f"\\subsection*{{{DIFF_NAMES[diff]}}}\n"
        answers_tex += "\\begin{enumerate}\n"
        for p in by_diff[diff]:
            answers_tex += f"\\item $ {p['question']} = {p['answer']} $\n"
        answers_tex += "\\end{enumerate}\n"
        answers_tex += "\\vspace{0.3cm}\n"

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    latex = template.replace("{{WORKSHEET_NUM}}", str(num))
    latex = latex.replace("{{QUESTIONS}}", questions_tex)
    latex = latex.replace("{{ANSWERS}}", answers_tex)
    latex = latex.replace("{{TOTAL}}", str(len(problems)))

    return latex


def compile_latex(latex_content, worksheet_num):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tex_path = os.path.join(OUTPUT_DIR, f"worksheet_{worksheet_num}.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(latex_content)

    result = subprocess.run(
        [
            "pdflatex",
            "-interaction=nonstopmode",
            f"-output-directory={OUTPUT_DIR}",
            tex_path,
        ],
        capture_output=True,
        text=True,
    )

    for ext in [".aux", ".log"]:
        try:
            os.remove(tex_path.replace(".tex", ext))
        except:
            pass

    pdf_path = os.path.join(OUTPUT_DIR, f"worksheet_{worksheet_num}.pdf")
    return os.path.exists(pdf_path), result.stdout, result.stderr


def merge_pdfs(output_filename="barcha_misollar.pdf"):
    try:
        from PyPDF2 import PdfMerger

        merger = PdfMerger()
        for n in range(1, 11):
            pdf_path = os.path.join(OUTPUT_DIR, f"worksheet_{n}.pdf")
            if os.path.exists(pdf_path):
                merger.append(pdf_path)
        out_path = os.path.join(SCRIPT_DIR, output_filename)
        merger.write(out_path)
        merger.close()
        return out_path
    except ImportError:
        return None


def main():
    print("=" * 50)
    print("Qisqa Ko'paytirish Formulalari - Generator")
    print("=" * 50)

    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    if not os.path.exists(TEMPLATE_PATH):
        print(f"Xatolik: template.tex topilmadi!")
        return

    for n in range(1, 11):
        problems = generate_worksheet(seed_val=n * 777, per_diff=10)
        latex_content = build_latex(problems, n)
        success, stdout, stderr = compile_latex(latex_content, n)
        if success:
            print(f"  OK   Qo'lyozma N{n} ({len(problems)} ta misol)")
        else:
            print(f"  XATO Qo'lyozma N{n}")
            print(f"        {stderr[-200:] if stderr else "Noma'lum xatolik"}")

    print("\nPDFlarni birlashtirish...")
    final_path = merge_pdfs("barcha_misollar.pdf")
    if final_path:
        print(f"Tayyor: {final_path}")
        print(f"Umumiy: 400 ta misol, 10 ta qo'lyozma")
    else:
        print("PyPDF2 o'rnatilmagan - PDFlar output/ papkasida alohida")


if __name__ == "__main__":
    main()

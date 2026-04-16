from fpdf import FPDF
import random


class FormulaPDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 16)
        self.cell(
            0,
            10,
            "Qisqa Ko'paytirish Formulalari - Mashqlar",
            align="C",
            new_x="LMARGIN",
            new_y="NEXT",
        )
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Sahifa {self.page_no()}", align="C")


def generate_problem(formula_type, difficulty):
    if formula_type == "kvadrat_yigindi":
        a = random.randint(1 + difficulty, 5 + difficulty * 3)
        b = random.randint(1 + difficulty, 5 + difficulty * 3)
        problem = f"({a} + {b})\u00b2"
        answer = f"{a}\u00b2 + 2ab + {b}\u00b2 = {a**2 + 2 * a * b + b**2}"
        return problem, answer

    elif formula_type == "kvadrat_ayirma":
        a = random.randint(5 + difficulty, 10 + difficulty * 2)
        b = random.randint(1 + difficulty, 4 + difficulty)
        problem = f"({a} - {b})\u00b2"
        answer = f"{a}\u00b2 - 2ab + {b}\u00b2 = {a**2 - 2 * a * b + b**2}"
        return problem, answer

    elif formula_type == "yigindi_ayirma_kupaytirish":
        a = random.randint(2 + difficulty, 6 + difficulty * 2)
        b = random.randint(1, a - 1)
        problem = f"({a} + {b})({a} - {b})"
        answer = f"{a}\u00b2 - {b}\u00b2 = {a**2 - b**2}"
        return problem, answer

    elif formula_type == "kub_yigindi":
        a = random.randint(1 + difficulty, 3 + difficulty)
        b = random.randint(1, a)
        problem = f"({a} + {b})\u00b3"
        result = (a + b) ** 3
        answer = f"{a}\u00b3 + 3a\u00b2b + 3ab\u00b2 + {b}\u00b3 = {result}"
        return problem, answer

    elif formula_type == "kub_ayirma":
        a = random.randint(3 + difficulty, 6 + difficulty)
        b = random.randint(1, a - 1)
        problem = f"({a} - {b})\u00b3"
        result = (a - b) ** 3
        answer = f"{a}\u00b3 - 3a\u00b2b + 3ab\u00b2 - {b}\u00b3 = {result}"
        return problem, answer

    elif formula_type == "ikki_had_yigindi_kvadrat":
        a = random.randint(1 + difficulty, 4 + difficulty * 2)
        b = random.randint(2, 5 + difficulty)
        problem = f"({a}x + {b})\u00b2"
        answer = f"{a}\u00b2x\u00b2 + {2 * a * b}bx + {b}\u00b2"
        return problem, answer

    elif formula_type == "ikki_had_ayirma_kvadrat":
        a = random.randint(1 + difficulty, 4 + difficulty * 2)
        b = random.randint(2, 5 + difficulty)
        problem = f"({a}x - {b})\u00b2"
        answer = f"{a}\u00b2x\u00b2 - {2 * a * b}bx + {b}\u00b2"
        return problem, answer

    elif formula_type == "kopaytma_yigindi":
        a = random.randint(1 + difficulty, 3 + difficulty)
        b = random.randint(1 + difficulty, 3 + difficulty)
        c = random.randint(1 + difficulty, 3 + difficulty)
        problem = f"x({a}x + {b}) + {c}({a}x + {b})"
        answer = f"({a}x + {b})(x + {c}) = {a}x\u00b2 + {a * c + b}x + {b * c}"
        return problem, answer

    elif formula_type == "uch_had_yigindi_kvadrat":
        a = random.randint(1, 2 + difficulty)
        b = random.randint(1, 3)
        c = random.randint(1, 2)
        result_a = a**2
        result_b = 2 * a * b + 2 * a * c
        result_c = b**2 + 2 * b * c + c**2
        problem = f"({a}x + {b} + {c})\u00b2"
        answer = f"{result_a}x\u00b2 + {result_b}x + {result_c}"
        return problem, answer

    elif formula_type == "mustaqil_hadli":
        a = random.randint(1 + difficulty, 3 + difficulty * 2)
        b = random.randint(1, 3)
        problem = f"({a}x + {b})({a}x - {b})"
        answer = f"{a}\u00b2x\u00b2 - {b}\u00b2"
        return problem, answer


def create_pdf():
    pdf = FormulaPDF(orientation="L", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=10)

    formula_types = [
        "kvadrat_yigindi",
        "kvadrat_ayirma",
        "yigindi_ayirma_kupaytirish",
        "kub_yigindi",
        "kub_ayirma",
        "ikki_had_yigindi_kvadrat",
        "ikki_had_ayirma_kvadrat",
        "kopaytma_yigindi",
        "uch_had_yigindi_kvadrat",
        "mustaqil_hadli",
    ]

    formula_names = {
        "kvadrat_yigindi": "(a+b)\u00b2 = a\u00b2 + 2ab + b\u00b2",
        "kvadrat_ayirma": "(a-b)\u00b2 = a\u00b2 - 2ab + b\u00b2",
        "yigindi_ayirma_kupaytirish": "(a+b)(a-b) = a\u00b2 - b\u00b2",
        "kub_yigindi": "(a+b)\u00b3 = a\u00b3 + 3a\u00b2b + 3ab\u00b2 + b\u00b3",
        "kub_ayirma": "(a-b)\u00b3 = a\u00b3 - 3a\u00b2b + 3ab\u00b2 - b\u00b3",
        "ikki_had_yigindi_kvadrat": "(ax+b)\u00b2 = a\u00b2x\u00b2 + 2abx + b\u00b2",
        "ikki_had_ayirma_kvadrat": "(ax-b)\u00b2 = a\u00b2x\u00b2 - 2abx + b\u00b2",
        "kopaytma_yigindi": "(a+b)(x+c)",
        "uch_had_yigindi_kvadrat": "(ax+b+c)\u00b2",
        "mustaqil_hadli": "(ax+b)(ax-b)",
    }

    random.seed(42)

    for level in range(1, 11):
        pdf.add_page()

        difficulty_stars = "*" * level
        pdf.set_font("helvetica", "B", 14)
        pdf.cell(
            0,
            8,
            f"{level}-daraja (Qiyinchilik: {difficulty_stars})",
            align="C",
            new_x="LMARGIN",
            new_y="NEXT",
        )
        pdf.ln(3)

        pdf.set_font("helvetica", "I", 9)
        pdf.cell(
            0,
            5,
            formula_names[formula_types[level - 1]],
            align="C",
            new_x="LMARGIN",
            new_y="NEXT",
        )
        pdf.ln(5)

        problems = []
        for i in range(10):
            problem, answer = generate_problem(formula_types[level - 1], level)
            problems.append((problem, answer))

        col_width = 85

        pdf.set_font("helvetica", "", 11)

        for row in range(5):
            y_start = pdf.get_y()

            problem1, answer1 = problems[row * 2]
            problem2, answer2 = problems[row * 2 + 1]

            pdf.set_xy(10, y_start)
            pdf.set_font("helvetica", "B", 11)
            pdf.cell(col_width, 6, f"{row * 2 + 1}. {problem1}", align="L")
            pdf.ln(5)
            pdf.set_font("helvetica", "", 9)
            pdf.cell(col_width, 5, f"Javob: {answer1}", align="L")

            pdf.set_xy(10 + col_width + 10, y_start)
            pdf.set_font("helvetica", "B", 11)
            pdf.cell(col_width, 6, f"{row * 2 + 2}. {problem2}", align="L")
            pdf.ln(5)
            pdf.set_font("helvetica", "", 9)
            pdf.cell(col_width, 5, f"Javob: {answer2}", align="L")

            pdf.ln(8)

        pdf.ln(5)
        pdf.set_font("helvetica", "I", 8)
        pdf.cell(0, 5, "Formulalarni eslab qoling va ishlashni davom eting!", align="C")

    pdf.output("/content/Qisqa_kopaytirish_mashqlar.pdf")
    print("PDF yaratildi: /content/Qisqa_kopaytirish_mashqlar.pdf")


if __name__ == "__main__":
    create_pdf()

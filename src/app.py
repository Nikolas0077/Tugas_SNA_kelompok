"""
Core Calculation Engine — DevOps Calculator
Menyediakan operasi aritmatika dasar via Flask web interface.
"""

import math
from flask import Flask, render_template_string, request

app = Flask(__name__)

# ---------------------------------------------------------------------------
# HTML template (inline agar tidak perlu folder templates)
# ---------------------------------------------------------------------------
PAGE = """
<!doctype html>
<title>Core Calculation Engine</title>
<h1>Core Calculation Engine</h1>
<form method="post">
  <input name="a" type="number" step="any" placeholder="a" required>
  <select name="op">
    <option value="add">+</option>
    <option value="sub">−</option>
    <option value="mul">×</option>
    <option value="div">÷</option>
    <option value="sqrt">√a</option>
    <option value="ln">ln a</option>
  </select>
  <input name="b" type="number" step="any" placeholder="b (diabaikan untuk √, ln)">
  <button type="submit">Compute</button>
</form>
{% if result is not none %}
  <h2>Result: {{ result }}</h2>
{% endif %}
"""

# ---------------------------------------------------------------------------
# Fungsi-fungsi kalkulasi murni (mudah diuji dengan pytest)
# ---------------------------------------------------------------------------

def add(a: float, b: float) -> float:
    """Penjumlahan dua bilangan."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Pengurangan dua bilangan."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Perkalian dua bilangan."""
    return a * b


def divide(a: float, b: float) -> float:
    """Pembagian dua bilangan; raises ZeroDivisionError jika b == 0."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def square_root(a: float) -> float:
    """Akar kuadrat; raises ValueError jika a < 0."""
    if a < 0:
        raise ValueError("sqrt domain error")
    return math.sqrt(a)


def natural_log(a: float) -> float:
    """Logaritma natural; raises ValueError jika a <= 0."""
    if a <= 0:
        raise ValueError("ln domain error")
    return math.log(a)


# ---------------------------------------------------------------------------
# Route Flask
# ---------------------------------------------------------------------------

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        op = request.form.get("op", "add")
        try:
            a = float(request.form.get("a", "0"))
            if op == "sqrt":
                result = square_root(a)
            elif op == "ln":
                result = natural_log(a)
            else:
                b = float(request.form.get("b", "0"))
                if op == "add":
                    result = add(a, b)
                elif op == "sub":
                    result = subtract(a, b)
                elif op == "mul":
                    result = multiply(a, b)
                elif op == "div":
                    result = divide(a, b)
        except (ValueError, ZeroDivisionError) as exc:
            result = f"Error: {exc}"
    return render_template_string(PAGE, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

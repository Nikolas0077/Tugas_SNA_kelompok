"""
Core Calculation Engine — DevOps Calculator
Menyediakan operasi aritmatika dasar via Flask web interface.
"""

import math
from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template_string, request
import math
app = Flask(__name__)

# very small HTML so you can see it working immediately
PAGE = """
<!doctype html>
<title>DevOps Calculator</title>
<h1>DevOps Calculator</h1>
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
  <input name="b" type="number" step="any" placeholder="b (ignored for √,ln)" />
  <button type="submit">Compute</button>
</form>
{% if result is not none %}
  <h2>Result: {{ result }}</h2>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        op = request.form.get("op", "add")
        try:
            a = float(request.form.get("a", "0"))
            if op == "sqrt":
                if a < 0:
                    raise ValueError("sqrt domain error")
                result = a ** 0.5
            elif op == "ln" :
                if a<=0:
                    raise ValueError("ln domain error")
                result = math.log(a)
            else:
                b = float(request.form.get("b", "0"))
                if op == "add":
                    result = a + b
                elif op == "sub":
                    result = a - b
                elif op == "mul":
                    result = a * b
                elif op == "div":
                    if b == 0:
                        raise ZeroDivisionError("division by zero")
                    result = a / b

        except Exception as e:
            result = f"Error: {e}"
    return render_template_string(PAGE, result=result)
 

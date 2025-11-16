import sys
import math
import numpy as np
from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QTabWidget, QGridLayout, 
    QLineEdit, QPushButton, QVBoxLayout, QLabel, QComboBox
)
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtCore import Qt

import matplotlib.pyplot as plt


# --------------------------
# Standard Calculator Tab
# --------------------------
class StandardCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

        grid = QGridLayout()
        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
            ("C", 4, 0), ("(", 4, 1), (")", 4, 2)
        ]

        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(self.handleButton)
            grid.addWidget(btn, row, col)

        layout.addLayout(grid)
        self.setLayout(layout)

    def handleButton(self):
        text = self.sender().text()

        if text == "C":
            self.display.clear()
        elif text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)


# --------------------------
# Trigonometry Calculator Tab
# --------------------------
class TrigonometryCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.inputField = QLineEdit()
        self.inputField.setValidator(QDoubleValidator())
        layout.addWidget(QLabel("Enter angle (degrees):"))
        layout.addWidget(self.inputField)

        self.functionSelector = QComboBox()
        self.functionSelector.addItems(["sin", "cos", "tan", "cot", "sec", "csc"])
        layout.addWidget(self.functionSelector)

        self.calculateBtn = QPushButton("Calculate")
        self.calculateBtn.clicked.connect(self.calculate)
        layout.addWidget(self.calculateBtn)

        self.resultLabel = QLabel("Result: ")
        layout.addWidget(self.resultLabel)

        self.setLayout(layout)

    def calculate(self):
        try:
            angle_deg = float(self.inputField.text())
            angle_rad = math.radians(angle_deg)
            func = self.functionSelector.currentText()

            functions = {
                "sin": math.sin(angle_rad),
                "cos": math.cos(angle_rad),
                "tan": math.tan(angle_rad),
                "cot": 1 / math.tan(angle_rad),
                "sec": 1 / math.cos(angle_rad),
                "csc": 1 / math.sin(angle_rad),
            }

            self.resultLabel.setText(f"Result: {functions[func]}")
        except Exception:
            self.resultLabel.setText("Error: Invalid Input")


# --------------------------
# Calculus Calculator Tab
# --------------------------
class CalculusCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Enter function (in variable x):"))
        self.functionInput = QLineEdit()
        layout.addWidget(self.functionInput)

        self.operationSelector = QComboBox()
        self.operationSelector.addItems(["Derivative", "Integral"])
        layout.addWidget(self.operationSelector)

        self.calculateBtn = QPushButton("Compute")
        self.calculateBtn.clicked.connect(self.calculate)
        layout.addWidget(self.calculateBtn)

        self.resultLabel = QLabel("Result:")
        layout.addWidget(self.resultLabel)

        self.setLayout(layout)

    def calculate(self):
        expr = self.functionInput.text()
        operation = self.operationSelector.currentText()

        try:
            import sympy as sp
            x = sp.symbols("x")
            f = sp.sympify(expr)

            if operation == "Derivative":
                result = sp.diff(f, x)
            else:
                result = sp.integrate(f, x)

            self.resultLabel.setText(f"Result: {sp.simplify(result)}")

        except Exception:
            self.resultLabel.setText("Error: Invalid function")


# --------------------------
# Discrete Mathematics Calculator Tab
# --------------------------
class DiscreteCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Discrete Operations:"))
        self.selector = QComboBox()
        self.selector.addItems([
            "Factorial",
            "Permutation nPr",
            "Combination nCr"
        ])
        layout.addWidget(self.selector)

        self.nInput = QLineEdit()
        self.nInput.setValidator(QDoubleValidator())
        layout.addWidget(QLabel("n:"))
        layout.addWidget(self.nInput)

        self.rInput = QLineEdit()
        self.rInput.setValidator(QDoubleValidator())
        layout.addWidget(QLabel("r (if applicable):"))
        layout.addWidget(self.rInput)

        self.calculateBtn = QPushButton("Compute")
        self.calculateBtn.clicked.connect(self.compute)
        layout.addWidget(self.calculateBtn)

        self.resultLabel = QLabel("Result:")
        layout.addWidget(self.resultLabel)

        self.setLayout(layout)

    def compute(self):
        try:
            n = int(self.nInput.text())
            operation = self.selector.currentText()

            if operation == "Factorial":
                result = math.factorial(n)

            else:
                r = int(self.rInput.text())
                if operation == "Permutation nPr":
                    result = math.perm(n, r)
                else:
                    result = math.comb(n, r)

            self.resultLabel.setText(f"Result: {result}")

        except Exception:
            self.resultLabel.setText("Error: Invalid Input")


# --------------------------
# Graphing Calculator Tab
# --------------------------
class GraphingCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Enter function(s):"))
        self.functionInput = QLineEdit()
        self.functionInput.setPlaceholderText("Examples: sin(x), x**2, sin(x)+cos(y)")
        layout.addWidget(self.functionInput)

        # Choose graph type
        layout.addWidget(QLabel("Graph Type:"))
        self.modeBox = QComboBox()
        self.modeBox.addItems(["2D Plot (x only)", "3D Surface Plot (x, y)"])
        layout.addWidget(self.modeBox)

        self.plotBtn = QPushButton("Plot")
        self.plotBtn.clicked.connect(self.plotGraph)
        layout.addWidget(self.plotBtn)

        self.setLayout(layout)

    def plotGraph(self):
        expr_raw = self.functionInput.text().replace(" ", "")
        mode = self.modeBox.currentText()

        try:
            import sympy as sp
            x, y = sp.symbols("x y")

            # Multiple functions separated by commas
            expressions = [sp.sympify(e) for e in expr_raw.split(",")]

            if mode == "2D Plot (x only)":
                self.plot2D(expressions)
            else:
                self.plot3D(expressions[0])  # only first function used for 3D

        except Exception as e:
            print("Error:", e)

    # ------------------ 2D Plotting ------------------
    def plot2D(self, expressions):
        import numpy as np
        import matplotlib.pyplot as plt
        import sympy as sp

        x_vals = np.linspace(-10, 10, 500)

        plt.figure()

        for expr in expressions:
            f = sp.lambdify(sp.symbols("x"), expr, "numpy")
            y_vals = f(x_vals)
            plt.plot(x_vals, y_vals, label=str(expr))

        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.title("2D Function Plot")
        plt.legend()
        plt.grid(True)
        plt.show()

    # ------------------ 3D Plotting ------------------
    def plot3D(self, expr):
        import numpy as np
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
        import sympy as sp

        x_vals = np.linspace(-5, 5, 200)
        y_vals = np.linspace(-5, 5, 200)
        X, Y = np.meshgrid(x_vals, y_vals)

        f = sp.lambdify((sp.symbols("x"), sp.symbols("y")), expr, "numpy")
        Z = f(X, Y)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.plot_surface(X, Y, Z, cmap="viridis")
        ax.set_title(f"3D Surface Plot of {expr}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

        plt.show()

# --------------------------
# Main Window
# --------------------------
class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Multi-Tab Calculator")

        tabs = QTabWidget()
        tabs.addTab(StandardCalculator(), "Standard")
        tabs.addTab(TrigonometryCalculator(), "Trigonometry")
        tabs.addTab(CalculusCalculator(), "Calculus")
        tabs.addTab(DiscreteCalculator(), "Discrete Math")
        tabs.addTab(GraphingCalculator(), "Graphing")

        self.setCentralWidget(tabs)


# --------------------------
# Run Application
# --------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.resize(500, 400)
    window.show()
    sys.exit(app.exec())

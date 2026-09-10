import tkinter as tk
from tkinter import messagebox
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbol
x = sp.Symbol('x')

# Function to differentiate
def differentiate():
    try:
        func = entry.get()
        expression = sp.sympify(func)
        derivative = sp.diff(expression, x)

        result_label.config(
            text=f"Derivative:\n{sp.pretty(derivative)}"
        )

    except Exception as e:
        messagebox.showerror("Error", "Invalid function input")

# Function to integrate
def integrate():
    try:
        func = entry.get()
        expression = sp.sympify(func)
        integral = sp.integrate(expression, x)

        result_label.config(
            text=f"Integral:\n{sp.pretty(integral)} + C"
        )

    except Exception as e:
        messagebox.showerror("Error", "Invalid function input")

# Function to plot
def plot_function():
    try:
        func = entry.get()
        expression = sp.sympify(func)

        f = sp.lambdify(x, expression, 'numpy')

        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)

        plt.figure()
        plt.axhline(0)
        plt.axvline(0)
        plt.title(f"Graph of {func}")
        plt.plot(x_vals, y_vals)
        plt.grid()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", "Cannot plot this function")

# Function to plot derivative
def plot_derivative():
    try:
        func = entry.get()
        expression = sp.sympify(func)
        derivative = sp.diff(expression, x)

        f = sp.lambdify(x, expression, 'numpy')
        df = sp.lambdify(x, derivative, 'numpy')

        x_vals = np.linspace(-10, 10, 400)

        plt.figure()
        plt.plot(x_vals, f(x_vals), label="f(x)")
        plt.plot(x_vals, df(x_vals), label="f'(x)")
        plt.title("Function and its Derivative")
        plt.legend()
        plt.grid()
        plt.show()

    except Exception:
        messagebox.showerror("Error", "Cannot compute derivative plot")

# GUI Setup
root = tk.Tk()
root.title("IB Calculus Solver")
root.geometry("500x400")

title = tk.Label(root, text="IB Calculus Visualizer", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

diff_button = tk.Button(root, text="Differentiate", command=differentiate)
diff_button.pack(pady=5)

int_button = tk.Button(root, text="Integrate", command=integrate)
int_button.pack(pady=5)

plot_button = tk.Button(root, text="Plot Function", command=plot_function)
plot_button.pack(pady=5)

plot_deriv_button = tk.Button(root, text="Plot Derivative", command=plot_derivative)
plot_deriv_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Courier", 12))
result_label.pack(pady=20)

root.mainloop()

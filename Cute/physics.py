import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("IB Physics HL Toolkit")
root.geometry("700x600")

title = tk.Label(root, text="IB Physics Calculator & Visualizer",
                 font=("Arial", 18))
title.pack(pady=10)

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# ----------- MECHANICS TAB -----------
mech_tab = ttk.Frame(notebook)
notebook.add(mech_tab, text="Mechanics")

tk.Label(mech_tab, text="SUVAT Solver", font=("Arial", 14)).pack()

tk.Label(mech_tab, text="Initial Velocity (u)").pack()
u_entry = tk.Entry(mech_tab)
u_entry.pack()

tk.Label(mech_tab, text="Acceleration (a)").pack()
a_entry = tk.Entry(mech_tab)
a_entry.pack()

tk.Label(mech_tab, text="Time (t)").pack()
t_entry = tk.Entry(mech_tab)
t_entry.pack()

def suvat():
    try:
        u = float(u_entry.get())
        a = float(a_entry.get())
        t = float(t_entry.get())

        v = u + a*t
        s = u*t + 0.5*a*t**2

        result = f"Final velocity v = {v} m/s\nDisplacement s = {s} m"
        messagebox.showinfo("Result", result)

    except:
        messagebox.showerror("Error", "Enter valid numbers")

tk.Button(mech_tab, text="Calculate SUVAT", command=suvat).pack(pady=10)


# -------- Projectile Motion Visualiser --------

tk.Label(mech_tab, text="Projectile Motion", font=("Arial", 14)).pack(pady=10)

angle = tk.Entry(mech_tab)
speed = tk.Entry(mech_tab)

tk.Label(mech_tab, text="Angle (degrees)").pack()
angle.pack()

tk.Label(mech_tab, text="Speed (m/s)").pack()
speed.pack()

def projectile():
    try:
        theta = float(angle.get())
        v = float(speed.get())

        g = 9.81
        t = np.linspace(0, 2*v*np.sin(np.radians(theta))/g, 100)

        x = v*np.cos(np.radians(theta))*t
        y = v*np.sin(np.radians(theta))*t - 0.5*g*t**2

        plt.figure()
        plt.plot(x, y)
        plt.title("Projectile Path")
        plt.xlabel("Distance (m)")
        plt.ylabel("Height (m)")
        plt.grid()
        plt.show()

    except:
        messagebox.showerror("Error", "Invalid input")

tk.Button(mech_tab, text="Visualize Projectile",
          command=projectile).pack(pady=10)


# -------- ELECTRICITY TAB --------
elec_tab = ttk.Frame(notebook)
notebook.add(elec_tab, text="Electricity")

tk.Label(elec_tab, text="Ohm's Law Calculator",
         font=("Arial", 14)).pack()

v_entry = tk.Entry(elec_tab)
i_entry = tk.Entry(elec_tab)

tk.Label(elec_tab, text="Voltage (V)").pack()
v_entry.pack()

tk.Label(elec_tab, text="Current (I)").pack()
i_entry.pack()

def ohms():
    try:
        V = float(v_entry.get())
        I = float(i_entry.get())

        R = V/I
        messagebox.showinfo("Resistance", f"R = {R} ohms")

    except:
        messagebox.showerror("Error", "Invalid input")

tk.Button(elec_tab, text="Calculate Resistance",
          command=ohms).pack(pady=10)


# -------- WAVES TAB --------
waves_tab = ttk.Frame(notebook)
notebook.add(waves_tab, text="Waves")

tk.Label(waves_tab, text="Wave Visualiser",
         font=("Arial", 14)).pack()

freq = tk.Entry(waves_tab)
amp = tk.Entry(waves_tab)

tk.Label(waves_tab, text="Frequency (Hz)").pack()
freq.pack()

tk.Label(waves_tab, text="Amplitude").pack()
amp.pack()

def wave():
    try:
        f = float(freq.get())
        A = float(amp.get())

        x = np.linspace(0, 2*np.pi, 500)
        y = A*np.sin(f*x)

        plt.figure()
        plt.plot(x, y)
        plt.title("Wave Form")
        plt.grid()
        plt.show()

    except:
        messagebox.showerror("Error", "Invalid input")

tk.Button(waves_tab, text="Show Wave",
          command=wave).pack(pady=10)


# -------- THERMAL PHYSICS TAB --------
thermal_tab = ttk.Frame(notebook)
notebook.add(thermal_tab, text="Thermal")

tk.Label(thermal_tab, text="Ideal Gas Law",
         font=("Arial", 14)).pack()

n_entry = tk.Entry(thermal_tab)
T_entry = tk.Entry(thermal_tab)
V_entry = tk.Entry(thermal_tab)

tk.Label(thermal_tab, text="Moles (n)").pack()
n_entry.pack()

tk.Label(thermal_tab, text="Temperature (K)").pack()
T_entry.pack()

tk.Label(thermal_tab, text="Volume (m^3)").pack()
V_entry.pack()

def gas():
    try:
        n = float(n_entry.get())
        T = float(T_entry.get())
        V = float(V_entry.get())

        R = 8.31
        P = n*R*T/V

        messagebox.showinfo("Pressure", f"P = {P} Pa")

    except:
        messagebox.showerror("Error", "Invalid input")

tk.Button(thermal_tab, text="Calculate Pressure",
          command=gas).pack(pady=10)


# -------- RUN APP --------
root.mainloop()

import sys
import math
import random
from dataclasses import dataclass

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QFormLayout,
    QPushButton, QLabel, QComboBox,
    QTextEdit, QLineEdit, QStackedWidget
)
from PySide6.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# =======================
# DATA MODELS
# =======================
@dataclass
class KinematicsResult:
    displacement: float
    time: float
    velocity: float


# =======================
# CALCULATORS
# =======================
class KinematicsCalculator:
    @staticmethod
    def uniform_motion(v, t):
        return KinematicsResult(v * t, t, v)


class ProjectileCalculator:
    g = 9.81

    @staticmethod
    def no_air(v, angle_deg):
        angle = math.radians(angle_deg)
        t = 2 * v * math.sin(angle) / ProjectileCalculator.g
        r = v**2 * math.sin(2 * angle) / ProjectileCalculator.g
        return t, r


class UncertaintyCalculator:
    @staticmethod
    def percent(delta, value):
        return abs(delta / value) * 100

    @staticmethod
    def absolute(percent, value):
        return percent / 100 * value


# =======================
# PLOTS
# =======================
class SimplePlot(FigureCanvas):
    def __init__(self):
        self.fig = Figure(figsize=(5, 4))
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)


# =======================
# PAGES
# =======================
class KinematicsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)

        notes = QTextEdit()
        notes.setReadOnly(True)
        notes.setText(
            "KINEMATICS (IB HL)\n\n"
            "s = vt\n"
            "v = u + at\n"
            "s = ut + 1/2 at^2\n\n"
            "Exam tip: Always state assumptions."
        )
        layout.addWidget(notes, 2)

        right = QVBoxLayout()
        layout.addLayout(right, 3)

        form = QFormLayout()
        self.v = QLineEdit()
        self.t = QLineEdit()
        form.addRow("Velocity (m/s)", self.v)
        form.addRow("Time (s)", self.t)
        right.addLayout(form)

        btn = QPushButton("Calculate")
        right.addWidget(btn)

        self.result = QLabel("Displacement = ")
        right.addWidget(self.result)

        self.plot = SimplePlot()
        right.addWidget(self.plot)

        btn.clicked.connect(self.solve)

    def solve(self):
        try:
            v = float(self.v.text())
            t = float(self.t.text())
            r = KinematicsCalculator.uniform_motion(v, t)
            self.result.setText(f"Displacement = {r.displacement:.2f} m")

            self.plot.ax.clear()
            time = [i * t / 100 for i in range(101)]
            s = [v * ti for ti in time]
            self.plot.ax.plot(time, s)
            self.plot.ax.set_xlabel("Time (s)")
            self.plot.ax.set_ylabel("Displacement (m)")
            self.plot.draw()
        except:
            self.result.setText("Invalid input")


class ProjectilePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        form = QFormLayout()
        self.v = QLineEdit()
        self.a = QLineEdit()
        form.addRow("Speed (m/s)", self.v)
        form.addRow("Angle (deg)", self.a)
        layout.addLayout(form)

        btn = QPushButton("Solve")
        layout.addWidget(btn)

        self.result = QLabel("")
        layout.addWidget(self.result)

        self.plot = SimplePlot()
        layout.addWidget(self.plot)

        btn.clicked.connect(self.solve)

    def solve(self):
        try:
            v = float(self.v.text())
            a = float(self.a.text())
            t, r = ProjectileCalculator.no_air(v, a)

            self.result.setText(
                f"Time of flight = {t:.2f} s\n"
                f"Range = {r:.2f} m\n\n"
                "Working:\n"
                "t = 2u sinθ / g\n"
                "R = u² sin2θ / g"
            )

            self.plot.ax.clear()
            angle = math.radians(a)
            time = [i * 0.02 for i in range(200)]
            x = [v * math.cos(angle) * ti for ti in time]
            y = [v * math.sin(angle) * ti - 0.5 * 9.81 * ti**2 for ti in time]
            self.plot.ax.plot(x, y)
            self.plot.ax.set_xlabel("x (m)")
            self.plot.ax.set_ylabel("y (m)")
            self.plot.draw()
        except:
            self.result.setText("Invalid input")


class UncertaintyPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout(self)

        self.value = QLineEdit()
        self.delta = QLineEdit()
        self.percent = QLineEdit()

        layout.addRow("Value", self.value)
        layout.addRow("Absolute uncertainty", self.delta)
        layout.addRow("Percent uncertainty", self.percent)

        btn = QPushButton("Calculate")
        self.out = QLabel("")
        layout.addRow(btn, self.out)

        btn.clicked.connect(self.solve)

    def solve(self):
        try:
            v = float(self.value.text())
            if self.delta.text():
                d = float(self.delta.text())
                p = UncertaintyCalculator.percent(d, v)
                self.out.setText(f"% uncertainty = {p:.2f}%")
            elif self.percent.text():
                p = float(self.percent.text())
                d = UncertaintyCalculator.absolute(p, v)
                self.out.setText(f"Absolute uncertainty = ±{d:.3g}")
        except:
            self.out.setText("Invalid input")


class SHMPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        form = QFormLayout()
        self.A = QLineEdit()
        self.w = QLineEdit()
        form.addRow("Amplitude (m)", self.A)
        form.addRow("Angular frequency", self.w)
        layout.addLayout(form)

        btn = QPushButton("Plot SHM")
        layout.addWidget(btn)

        self.plot = SimplePlot()
        layout.addWidget(self.plot)

        btn.clicked.connect(self.solve)

    def solve(self):
        try:
            A = float(self.A.text())
            w = float(self.w.text())
            t = [i * 0.02 for i in range(300)]
            x = [A * math.cos(w * ti) for ti in t]

            self.plot.ax.clear()
            self.plot.ax.plot(t, x)
            self.plot.ax.set_xlabel("Time (s)")
            self.plot.ax.set_ylabel("Displacement (m)")
            self.plot.draw()
        except:
            pass


class ExamPage(QWidget):
    QUESTIONS = [
        "Derive v² = u² + 2as.",
        "Explain energy conservation in SHM.",
        "Describe electric field lines.",
        "A projectile is launched horizontally. Find time to ground."
    ]

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel("Click to generate IB-style question")
        layout.addWidget(self.label)

        btn = QPushButton("Generate")
        layout.addWidget(btn)
        btn.clicked.connect(self.gen)

    def gen(self):
        self.label.setText(random.choice(self.QUESTIONS))


# =======================
# MAIN APP
# =======================
class PhysicsHLApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IB Physics HL Ultimate Helper")
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)

        sidebar = QVBoxLayout()
        layout.addLayout(sidebar, 1)

        self.menu = QComboBox()
        self.menu.addItems([
            "Kinematics",
            "Projectile Motion",
            "Uncertainty",
            "SHM",
            "Exam Practice"
        ])
        sidebar.addWidget(self.menu)
        sidebar.addStretch()

        self.pages = QStackedWidget()
        layout.addWidget(self.pages, 4)

        self.pages.addWidget(KinematicsPage())
        self.pages.addWidget(ProjectilePage())
        self.pages.addWidget(UncertaintyPage())
        self.pages.addWidget(SHMPage())
        self.pages.addWidget(ExamPage())

        self.menu.currentIndexChanged.connect(self.pages.setCurrentIndex)


# =======================
# RUN
# =======================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhysicsHLApp()
    window.show()
    sys.exit(app.exec())

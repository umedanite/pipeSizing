# pipeSizing

A small pipe friction / pressure-drop calculator based on the Haaland equation, with both a desktop
(PySide6) and a web (Streamlit) interface.

This project started as a way to learn Git and GitHub — it's intentionally small, so the workflow
(commits, history, branching) stays easy to follow while still being a real, useful calculator.

## What it calculates

Given a flow rate, pipe diameter, fluid viscosity, and pipe roughness, it computes:

- **Flow velocity** (m/s)
- **Reynolds number** (dimensionless)
- **Darcy friction factor**, via the Haaland approximation (a closed-form estimate of the Colebrook
  equation, avoiding the need to solve it iteratively)
- **Pressure drop per meter of pipe** (m/m and Pa/m)

## Running it

No `requirements.txt` or `pyproject.toml` exists yet — dependencies are only installed in the local
`.venv` (PySide6 6.11, Streamlit 1.58, Python 3.13).

Desktop GUI:
```
python main.py
```

Web GUI:
```
streamlit run streamlit_app.py
```

## Code structure

- **`Calculation.py`** — the single source of truth for the physics. Everything else is UI wrapping
  around this file.
  - `velocity(V, d)` — flow velocity from volumetric flow rate and diameter.
  - `reynold(u, d, v)` — Reynolds number from velocity, diameter, and kinematic viscosity.
  - `haaland(V, d, v, k)` — the main entry point. Takes flow rate `V` (l/s), diameter `d` (mm),
    kinematic viscosity `v` (m²/s), and pipe roughness `k` (mm); converts units internally
    (l/s → m³/s, mm → m) and returns `(u, re, f, pd)`: velocity (m/s), Reynolds number, Darcy friction
    factor, and pressure drop per meter (m/m).

- **`theGUI.py`** — `MainWindow(QMainWindow)`, the PySide6 desktop UI. Reads four `QLineEdit` inputs,
  calls `haaland`, and renders results into a `QTextEdit`.

- **`main.py`** — the desktop app's entry point: builds the `QApplication` and shows `MainWindow`
  from `theGUI.py`.

- **`streamlit_app.py`** — the web UI. Independent of `theGUI.py` / `main.py`; calls `haaland` directly
  from Streamlit input widgets.

Both UIs are thin, stateless wrappers with no shared UI abstraction — if `haaland`'s signature or
return tuple changes, both call sites need updating.

## Domain notes

- `k` = pipe roughness; the GUIs default to ~0.045–0.046 mm (heavy-grade steel pipe).
- Kinematic viscosity defaults differ slightly between the two UIs (water at different reference
  temperatures).

## Status

There are no automated tests, lint configs, or build steps in this repo yet.

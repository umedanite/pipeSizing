import streamlit as st

from Calculation import haaland

st.title("Pipe Friction Calculation")

V = st.number_input("Volume flow (l/s)", value=50.0)
d = st.number_input("Pipe diameter (mm)", value=150.0)
v = st.number_input("Kinematic viscosity (m2/s)", value=0.00000114, format="%.10f")
k = st.number_input("Pipe roughness (mm)", value=0.046)

if st.button("Calculate"):
    u, re, f, pd = haaland(V, d, v, k)

    st.write(f"Flow velocity: {u} m/s")
    st.write(f"Reynolds number: {re:.0f}")
    st.write(f"Friction factor: {f}")
    st.write(f"Pressure drop per meter: {pd} m/m")
    st.write(f"Pressure drop per meter: {1000 * 9.81 * pd:.2f} Pa/m")
    st.write(f"Pressure drop over 300 m: {300 * pd:.2f} m")
import streamlit as st

from Calculation import haaland

st.title("Pipe Friction Calculation ")

V = st.number_input("Volume flow (l/s)", value=50.0)
d = st.number_input("Pipe diameter (mm)", value=150.0)
v = st.number_input("Kinematic viscosity (m2/s) water at 25 ℃", value=0.000000895, format="%.10f")
k = st.number_input("Pipe roughness (mm), heavy grade steel pipe", value=0.046,  format="%.3f")

if st.button("Calculate"):
    u, re, f, pd = haaland(V, d, v, k)

    st.write(f"Flow velocity: {u} m/s")
    st.write(f"Reynolds number: {re:.0f}")
    st.write(f"Friction factor: {f}")
    st.write(f"Pressure drop per meter: {pd} m/m")
    st.write(f"Pressure drop per meter: {1000 * 9.81 * pd:.2f} Pa/m\n")
    st.write(f"Freddy is taking a nap......ZZZZZ")
  #  st.write(f"Pressure drop over 100 m: {100 * pd:.2f} m")
    

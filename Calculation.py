import math

def velocity(V,d):
    #diameter
    u = round(V/(0.25*math.pi*(d)**2),2)
    print(f"flow velocity u: {u} m/s")
    return u

def reynold(u, d, v):
    Re = u * (d) / v
    #print(f"Reynold's number Re: {round(Re,0)}")
    return Re

def haaland(V,d,v,k):
    V=V/1000
    d=d/1000
    k=k/1000
    u = velocity(V,d)
    re = round(reynold(u,d,v),0)
    f = round((1/(-3.6*math.log10(6.9/re+(k/d/3.7)**1.11)))**2,5)
    pd = round(4*f*u**2/d/2/9.81,5) # unit = m/m
    #print(f"relative roughless k/d: {k/d}")
    #print(f"friction factor f: {f}")
    #print(f"pressure drop per meter pd:{pd} m/m")
    #print(f"pressure drop per meter pd:{1000*9.81*pd} Pa/m")
    #print(f"pressure drop pd:{300*pd} m")
    return u, re, f, pd

#pd = haaland(50,150, 0.00000114, 0.00015)
#print(pd)
# k: average roughless; heavy grade steel = 0.046
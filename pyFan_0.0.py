# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:51:04 2024

@author: thompsonj

Simple tool to adjust fan curves 
Obtain duty points based on changes to system resistance
fan speed or air desnity
"""


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button

class FanCurve:
    def __init__(self,vol,pre,rpm,diameter,rho,area_F,k):
        self.vol = vol
        self.pre = pre
        self.rpm = rpm
        self.diameter = diameter
        self.rho = rho
        self.area_F = area_F
        self.k = k
        self.n = 1000
        
    def setBaseCurves(self):
        
        npx = np.linspace(self.vol[0],self.vol[3],self.n)
        npy = np.zeros((self.n))
        npz = np.zeros((self.n))
        
        for i,x in enumerate(npx):
            f1 = self.f(x,self.vol,0)
            f2 = self.f(x,self.vol,1)
            f3 = self.f(x,self.vol,2)
            f4 = self.f(x,self.vol,3)
            npy[i] = f1*self.pre[0] + f2*self.pre[1] + f3*self.pre[2] + f4*self.pre[3]
            npz[i] = self.k*0.5*self.rho*(x/self.area_F)**2
            
        self.pltVol = npx
        self.pltPre = npy
        self.pltRes = npz
        
    def f(self,x,vol,opt):
        if opt == 0:
            arr = [0,1,2,3]
        elif opt == 1:
            arr = [1,0,2,3]
        elif opt == 2:
            arr = [2,0,1,3]
        elif opt == 3:
            arr = [3,0,1,2]
        x1 = vol[arr[0]]
        x2 = vol[arr[1]]
        x3 = vol[arr[2]]
        x4 = vol[arr[3]]
        
        return ((x-x2)*(x-x3)*(x-x4))/((x1-x2)*(x1-x3)*(x1-x4))
            
    def setOptCurves(self,rpm,diameter,rho,k):
        # Set new Curves
        ratRpm = rpm/self.rpm
        ratRho = rho/self.rho
        ratDia = diameter/self.diameter
        ratK = k/self.k
        
        self.OptVol = self.vol * ratRpm * ratDia**3
        self.OptPre = self.pre * ratRpm**2 * ratDia**2 * ratRho
        
        npx = np.linspace(self.OptVol[0],self.OptVol[3],self.n)
        npy = np.zeros((self.n))
        npz = np.zeros((self.n))
        
        for i,x in enumerate(npx):
            f1 = self.f(x,self.OptVol,0)
            f2 = self.f(x,self.OptVol,1)
            f3 = self.f(x,self.OptVol,2)
            f4 = self.f(x,self.OptVol,3)
            npy[i] = f1*self.OptPre[0] + f2*self.OptPre[1] + f3*self.OptPre[2] + f4*self.OptPre[3]
            npz[i] = ratK*self.k*0.5*self.rho*(x/self.area_F)**2
            
        self.pltOptVol = npx
        self.pltOptPre = npy
        self.pltOptRes = npz        
        
        idx = np.argwhere(np.diff(np.sign(npy - npz))).flatten()
        self.optDV = np.rint(npx[idx])[0]
        self.optDP = np.rint(ratK*self.k*0.5*self.rho*(self.optDV/self.area_F)**2)
        

def main():
    """ Interactive Fan Curve generator """
    # Define the fan curve to initially draw
    vol = np.array([0,81,180,271.8])
    pre = np.array([2700,2400,1500,0])
    rpm = 1485
    diameter = 2
    rho = 1.204
    duty_V = 180
    duty_P = 1500
    area_F = np.pi*diameter**2/4
    k = duty_P/(0.5*rho*(duty_V/area_F)**2)
    
    f = FanCurve(vol,pre,rpm,diameter,rho,area_F,k)
    f.setBaseCurves()
    f.setOptCurves(rpm,diameter,rho,k)
	
	# Create Interactive figure
    fig = plt.figure(figsize=(8,6), dpi=150)
    plt.subplots_adjust(bottom=0.35)
    
    ax1 = fig.add_subplot(111)
    plt.title('Interactive Fan Curve')
    bFan, = plt.plot(f.pltVol, f.pltPre,color='blue',label='Base Fan Curve')
    bRes, = plt.plot(f.pltVol, f.pltRes,'--',color='blue',label='Base Resistance')
    sFan, = plt.plot(f.pltOptVol, f.pltOptPre,color='red',label='Option Fan Curve')
    sRes, = plt.plot(f.pltOptVol, f.pltOptRes,'--',color='red',label='Option Resistance')
    ax1.text(20, 2000, 'Pressure - {} Pa\nVol Flow - {} m³/s'.format(duty_P,duty_V), 
             color='blue', bbox=dict(facecolor='none', edgecolor='blue'))
    
    sTxt = ax1.text(20, 1500, 'Pressure - {} Pa\nVol Flow - {} m³/s'.format(int(f.optDP),int(f.optDV)), 
             color='red', bbox=dict(facecolor='none', edgecolor='red'))
    
    #ax1.annotate('Pressure - %s Pa\nVol Flow - %s m³/s' % [duty_P,duty_V], xy=[duty_P,duty_V])
    ax1.set_xlim(0,250)
    ax1.set_ylim(0,3000)
    ax1.set_xlabel('Volume Flow rate (m³/s)')
    ax1.set_ylabel('Total Pressure (Pa)')
    ax1.legend(loc='upper right')
    
    # Create axes for sliders
    ax_rpm   = plt.axes([0.1, 0.20, 0.8, 0.03])
    ax_rho   = plt.axes([0.1, 0.15, 0.8, 0.03])
    ax_dia   = plt.axes([0.1, 0.10, 0.8, 0.03])
    ax_K     = plt.axes([0.1, 0.05, 0.8, 0.03])
	
	# Create sliders
    sl_rpm   = Slider(ax_rpm, 'Fan RPM', 0.0, 1500.0, valinit=rpm)
    sl_rho   = Slider(ax_rho, 'Density', 0.125, 2.0, valinit=rho)
    sl_dia   = Slider(ax_dia, 'Diameter', 0.5, 2.5, valinit=diameter)
    sl_K     = Slider(ax_K, 'K', 0.01, 2.0, valinit=k)

    # update plot function
    def update(val):
		# Update the chart based on the sliders position
        rpm = sl_rpm.val
        rho = sl_rho.val
        diameter = sl_dia.val
        k = sl_K.val
          		
        f.setOptCurves(rpm,diameter,rho,k)
          		
        sFan.set_xdata(f.pltOptVol)
        sFan.set_ydata(f.pltOptPre)
        sRes.set_xdata(f.pltOptVol)
        sRes.set_ydata(f.pltOptRes)
        sTxt.set_text('Pressure - {} Pa\nVol Flow - {} m³/s'.format(int(f.optDP),int(f.optDV)))
        
	# Call update function when a slider is changed
    sl_rpm.on_changed(update)
    sl_rho.on_changed(update)
    sl_dia.on_changed(update)
    sl_K.on_changed(update)
	
    plt.show()

if __name__== "__main__":
	main()

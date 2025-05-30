import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main(tunWid,tunHei,blkAra,ambTmp):
    # This function produces a set of graphics for different critical velocity settings
    MWs = [1,2,3,4,5,7.5,10,30,50,70,100,150,200,300]
    MWs = np.asarray(MWs)
    grs = [-6,-4,-2,-1,-0.5,0,0.5,1,2,4,6]
    grs = np.asarray(grs)

    # The six charts to be made are three grads for all MWs and three FHRR for all grs
    grad1 = 0
    grad2 = -1
    grad3 = -3
    crt1 = list()
    crt2 = list()
    crt3 = list()
    for MW in MWs:
        crtVel,TFlame = critVel(tunWid,tunHei,blkAra,ambTmp,MW,grad1)
        crt1.append(crtVel)
        crtVel,TFlame = critVel(tunWid,tunHei,blkAra,ambTmp,MW,grad2)
        crt2.append(crtVel)
        crtVel,TFlame = critVel(tunWid,tunHei,blkAra,ambTmp,MW,grad3)
        crt3.append(crtVel)

    crt1 = np.array(crt1)
    crt2 = np.array(crt2)
    crt3 = np.array(crt3)
    crt7 = crt1*(tunWid*tunHei -blkAra)
    crt8 = crt2*(tunWid*tunHei -blkAra)
    crt9 = crt3*(tunWid*tunHei -blkAra)

    MW1 = 5
    MW2 = 30
    MW3 = 100
    crt4 = list()
    crt5 = list()
    crt6 = list()
    for gr in grs:
        crtVel,TFlame = critVel(tunWid,tunHei,blkAra,ambTmp,MW1,gr)
        crt4.append(crtVel)
        crtVel,TFlame = critVel(tunWid,tunHei,blkAra,ambTmp,MW2,gr)
        crt5.append(crtVel)
        crtVel,TFlame = critVel(tunWid,tunHei,blkAra,ambTmp,MW3,gr)
        crt6.append(crtVel)

    crt4 = np.array(crt4)
    crt5 = np.array(crt5)
    crt6 = np.array(crt6)

    # Now develop the charts
    fig1, (axGr1, axGr2, axGr3) = plt.subplots(3, 1, sharex=True)
    axGr1.plot(MWs,crt1)
    axGr1.set_title('Gradient => Top - 0% : Mid - 1% : Bot - 3%')
    axGr1.set_ylim([0,5])
    axGr1.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1))
    axGr1.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    #axGr1.set_ylabel('Critical Velocity (m/s)')
    axGr2.plot(MWs,crt2)
    #axGr2.set_title('Gradient = 1%')
    axGr2.set_ylim([0,5])
    axGr2.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1))
    axGr2.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axGr2.set_ylabel('Critical Velocity (m/s)')
    axGr3.plot(MWs,crt3)
    #axGr3.set_title('Gradient = 3%')
    axGr3.set_ylim([0,5])
    axGr3.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1))
    axGr3.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    #axGr3.set_ylabel('Critical Velocity (m/s)')
    axGr3.set_xlabel('Fire heat release rate (MW)')

    fig1.savefig('/static/images/CV-MW.png')
    #fig1.show()

    # Now develop the charts
    fig2, (axFhr1, axFh2, axFh3) = plt.subplots(3, 1, sharex=True)
    axFhr1.plot(grs,crt4)
    axFhr1.set_title('Fire Heat Release Rate => Top - 5MW : Mid - 30MW : Bot - 100MW')
    axFhr1.set_ylim([0,5])
    axFhr1.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1))
    axFhr1.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    #axGr1.set_ylabel('Critical Velocity (m/s)')
    axFh2.plot(grs,crt5)
    #axFh2.set_title('Fire Heat Release Rate = 30MW')
    axFh2.set_ylim([0,5])
    axFh2.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1))
    axFh2.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axFh2.set_ylabel('Critical Velocity (m/s)')
    axFh3.plot(grs,crt6)
    #axFh3.set_title('Fire Heat Release Rate = 100MW')
    axFh3.set_ylim([0,5])
    axFh3.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1))
    axFh3.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    #axGr3.set_ylabel('Critical Velocity (m/s)')
    axFh3.set_xlabel('Tunnel Gradient (%)')

    fig2.savefig('/static/images/CV-Grad.png')
    #fig2.show()

    # Now develop the charts
    fig3, (axGr4, axGr5, axGr6) = plt.subplots(3, 1, sharex=True)
    axGr4.plot(MWs,crt7)
    axGr4.set_title('Gradient => Top - 0% : Mid - 1% : Bot - 3%')
    #axGr4.set_ylim([0,5])
    #xGr4.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1))Q
    axGr4.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    #axGr4.set_ylabel('Critical Velocity (m/s)')
    axGr5.plot(MWs,crt8)
    #axGr5.set_title('Gradient = 1%')
    #axGr5.set_ylim([0,5])
    #xGr5.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1))
    axGr5.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axGr5.set_ylabel('Critical Air Flow (m^3/s)')
    axGr6.plot(MWs,crt9)
    #axGr6.set_title('Gradient = 3%')
    #axGr6.set_ylim([0,5])
    #xGr6.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1))
    axGr6.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    #axGr6.set_ylabel('Critical Velocity (m/s)')
    axGr6.set_xlabel('Fire heat release rate (MW)')

    fig3.savefig('/static/images/CV-Flow.png')
    #fig3.show()
def critVel(tunWid,tunHei,blkAra,ambTmp,FHRR,grad):
    # This fucntion calculates critical velocity and flame temperature
    tunAra = tunWid*tunHei - blkAra
    airDen = 1.2*(293/(273.15+ambTmp))
    grvity = 9.81

    # Now solution is iterative with flame temperature
    # Guess starting flame temperature as ambient conditions
    Tflame = ambTmp
    TflameOld = ambTmp
    k1Coef = k1(FHRR)
    kgCoef = kg(grad)
    VelCrit = k1Coef*kgCoef*((grvity*tunHei*FHRR*1000000)/(airDen*1007*tunAra*(Tflame+273.15)))**(1/3)
    Tflame=FHRR*1000000/(airDen*1007*tunAra*VelCrit)+ambTmp

    # Now cycle through the iterations until convergence
    while True:
        if abs(Tflame-TflameOld) <= 0.0005:
            break
        TflameOld = Tflame
        VelCrit = k1Coef*kgCoef*((grvity*tunHei*FHRR*1000000)/(airDen*1007*tunAra*(Tflame+273.15)))**(1/3)
        Tflame=FHRR*1000000/(airDen*1007*tunAra*VelCrit)+ambTmp

    return VelCrit,Tflame

def k1(MW):
    # Determine the K1 factor using NFPA 502 2017 data
    if MW>=100:
        return 0.606
    elif MW>=90:
        return 0.62
    elif MW>=70:
        return 0.64
    elif MW>=50:
        return 0.68
    elif MW>=30:
        return 0.74
    else:
        return 0.87

def kg(grad):
    # Determine the kg factor using NFPA 502 2017 data
    if grad>=0:
        return 1
    else:
        return 1+0.0374*(abs(grad))**0.8

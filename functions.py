#!/usr/bin/python3
#NOTE: The initial version of mVNC will NOT support creating its own virtual outputs ; an existing physical or virtual output must be hijacked.
import os
from subprocess import check_output

def aggregateOutputDevices()->list:
    xOutput = check_output('xrandr')
    xOutput = xOutput.decode('utf-8')   #Get rid of byte-encoding, ew.
    xList  = xOutput.split('\n')

    viableOutputHostNames = ["DP","VGA","DisplayPort","HDMI","VIRTUAL","DVI"]   #Add port types here if your system supports other display technology, such as S-Video or Apple Display Connector.
    
    portLines = []
    for line in xList:
        for portType in viableOutputHostNames:
            if portType in line:
                portLines.append(line)
    
    cPorts = []
    dPorts = []  #Create empty lists for connected and disconnected ports.

    #Sort the ports into connected and disconnected.
    for line in portLines:
        if "disconnected" in line:
            dPorts.append(line)
        elif "connected" in line:
            cPorts.append(line)
    
    for x in range(len(cPorts)):
        cPorts[x]=cPorts[x].split(" ")[0]
    
    for x in range(len(dPorts)):
        dPorts[x]=dPorts[x].split(" ")[0]

    return [cPorts,dPorts]

def realX():    #Dead simple python wrapper to call xrandr to reorient itself with only real displays.
    os.system('xrandr --auto')

def addmodeX(display:str='VIRTUAL1',width='768',height='768',rRate='60'):
    os.system('xrandr --addmode '+display+' '+width+'x'+height+'_'+rRate)

def createVMM(width:str='768',height:str='768',rRate:str='60'):    #Create a virtual monitor mode, and set the properties of the virtual display.

    #modeInfo = check_output(['gtf', '600', '975' ,'60'])   #Sanity test run.

    modeInfo = check_output(['gtf',width,height,rRate])  #A bit of junk gets added. :(
    findModeline = modeInfo.find(b'Modeline')   #Find Modeline subsection. The b before Modeline translates the string into a format that the find method can understand, a side-effect of Python 3.5.

    #print("Found beginning of Modeline at: ",findModeline)     Debug.
    #print(modeInfo[findModeline+9:])                           Debug.
    #print(modeInfo[findModeline+9:].decode('utf-8'))           Debug.

    modeline  = modeInfo[findModeline+9:].decode('utf-8')   #Have to truncate modeInfo to get the string we want to pass to xrandr, along with re-formatting the byte-encoded string acquired from earlier.
    os.system("xrandr --newmode "+modeline)

def outputVirtualDisplay(hostPort:str,width,height,rRate,position:str='--left-of',relativeMonitor:str='DisplayPort-1'):
    os.system('xrandr --output '+hostPort+' --mode '+width+'x'+height+'_'+rRate+' '+position+' '+relativeMonitor)

def pressMe(hostPort,width,height,rRate,position,relativeMonitor):
    createVMM(width,height,rRate)
    addmodeX(hostPort,width,height,rRate)
    outputVirtualDisplay(hostPort,width,height,rRate,position,relativeMonitor)
    
import os, sys, traceback
logFile='/tmp/RaedQuickSignal.log'

def trace_error():
    try:
        traceback.print_exc(file=sys.stdout)
        traceback.print_exc(file=open(logFile, 'a'))
    except:
        pass

def logdata(label_name = '', data = None,mode='a'):
    try:
        data=str(data)
        if mode=='w':
           fp = open(logFile, 'w')
        else:   
           fp = open(logFile, 'a')
        fp.write( str(label_name) + ': ' + data+"\n")
        fp.close()
    except:
        trace_error()    
        pass

def dellog():
    try:
        if os_path.exists(logFile):
                os_remove(logFile)
    except:
        pass

def DreamOS():
    if os_path.exists('/var/lib/dpkg/status'):
        return True
    else:
        return False

    

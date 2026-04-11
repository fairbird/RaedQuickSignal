import os, sys, traceback
logFile='/tmp/RaedQuickSignal.log'

def trace_error():
    try:
        traceback.print_exc(file=sys.stdout)
        with open(logFile, 'a') as _lf:
            traceback.print_exc(file=_lf)
    except Exception:
        pass

def logdata(label_name = '', data = None, mode='a'):
    try:
        data = str(data)
        with open(logFile, mode) as fp:
            fp.write(str(label_name) + ': ' + data + "\n")
    except Exception:
        trace_error()

def dellog():
    try:
        if os.path.exists(logFile):
            os.remove(logFile)
    except Exception:
        pass

def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return True
    else:
        return False

    

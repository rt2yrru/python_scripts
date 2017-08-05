from subprocess import Popen, PIPE

def getstatusoutput(command):
    process = Popen(command, stdout=PIPE)
    out = process.communicate()
    return (out)

_cmd='ifconfig'
code= getstatusoutput(_cmd) # we are sending command -->  ifconfig
print (code[0])

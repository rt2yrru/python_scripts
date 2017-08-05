from subprocess import Popen, PIPE

def getstatusoutput(command):
    process = Popen(command, stdout=PIPE)
    out = process.communicate()
    return (out)

code= getstatusoutput('ifconfig') # we are sending command -->  ifconfig
print (code[0])

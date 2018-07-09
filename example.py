from yeast import *

pYeast = yeastManager() 
print "Current time: %d" % pYeast.currentTime()
print "Yeast encode: %s" % pYeast.getCurrentEncode()
print "Yeast decode: %d" % pYeast.decode(pYeast.getCurrentEncode())
print "It returned 1481712065055? %d | %s" % (pYeast.decode("LZywzeV"), "Yes" if pYeast.decode("LZywzeV") == 1481712065055 else "No")
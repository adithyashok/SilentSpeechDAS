import sys
import numpy

fname = sys.argv[1]

x=loadtxt(fname)

#figure(figsize=(8,3))
plot((x[18000:23000,-1]/(2**10)-0.5)*3.3/1009*1000,'k')
ylim([-1.63,1.63])
ylabel('mV')
xlabel('t (ms)')
savefig('SampleEMG.png',dpi=300) #,bbox_inches='tight')
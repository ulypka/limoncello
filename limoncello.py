#sasha  -s 1000 -g 38 -f 20
import argparse, sys
parser = argparse.ArgumentParser()
parser.add_argument('-g', help="Final gradus of lemonchelo 35 is default", default=35,type=int)
parser.add_argument('-k', help="Gradus of spirt 95 is default", default=95,type=int)
parser.add_argument('-s', help="V of spirt", type=int)
parser.add_argument('-f', help="procent os sugar in final 15 is default", default=15,type=int)

args = parser.parse_args()
if (args.s is None):
    parser.print_usage()
    print ('%s Error: need V of spirt'%(sys.argv[0]))
    quit()
g=args.g #final gradus
k=args.k #spirt gradus
s=args.s #V spirta
f=args.f #prosent of sugar
c=s*f*k/(100*g) #sugar in gram
print c,'sugar gram'
v=(s*k-g*c*60/100-g*s)/g
print v,'water'

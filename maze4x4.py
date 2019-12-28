from __future__ import print_function
import copy
import time
import sys

start=time.time()

def new_list_remove(src, a):
    new_list = copy.deepcopy(src) # src.copy() - in case of list of list 
    new_list.remove(a)
    return new_list

alist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#alist = [1,2,3,4,5,6,7,8,9,10,10,11,13,14,14,15]

lineSum =0
for a in range(16):
    lineSum += alist[a]
lineSum//=4

count = 0
match = 0

for a in alist:
    count+=1
    blist = new_list_remove(alist,a)
    for b in blist:
        clist = new_list_remove(blist,b)
        count+=1
        for c in clist:       
            dlist = new_list_remove(clist,c)
            count+=1
            for d in dlist:
                elist = new_list_remove(dlist,d)
                count+=1
                if (a+b+c+d != lineSum):
                    count+=1
                    continue
                for e in elist:               
                    flist = new_list_remove(elist,e)
                    count+=1
                    for f in flist:                  
                        glist = new_list_remove(flist,f)
                        count+=1
                        if (a+b+e+f != lineSum):
                            count+=1
                            continue
                        for g in glist:                       
                            hlist = new_list_remove(glist,g)
                            count+=1
                            for h in hlist:   
                                ilist = new_list_remove(hlist,h)
                                count+=1
                                if (c+d+g+h != lineSum):
                                    count+=1
                                    continue
                                if (e+f+g+h != lineSum):
                                    count+=1
                                    continue
                                for i in ilist:
                                    jlist = new_list_remove(ilist,i)
                                    count +=1
                                    for j in jlist:
                                        klist = new_list_remove(jlist,j)
                                        count +=1
                                        for k in klist:
                                            llist = new_list_remove(klist,k)
                                            count +=1
                                            if( f+g+j+k != lineSum):
                                                count+=1
                                                continue
                                            for l in llist:
                                                mlist = new_list_remove(llist,l)
                                                count +=1
                                                if (i+j+k+l != lineSum):
                                                    count+=1
                                                    continue
                                                for m in mlist:
                                                    nlist = new_list_remove(mlist,m)
                                                    count +=1
                                                    if (d+g+j+m != lineSum):
                                                        count+=1
                                                        continue
                                                    if (a+e+i+m != lineSum):
                                                        count+=1
                                                        continue
                                                    for n in nlist:
                                                        olist = new_list_remove(nlist,n)
                                                        count +=1
                                                        if (b+f+j+n != lineSum):
                                                            count+=1
                                                            continue
                                                        if (i+j+m+n != lineSum):
                                                            count+=1
                                                            continue
                                                        for o in olist:
                                                            plist = new_list_remove(olist,o)
                                                            count +=1
                                                            if (c+g+k+o != lineSum):
                                                                count+=1
                                                                continue
                                                            for p in plist:
                                                                count +=1 
                                                                if (m+n+o+p != lineSum):
                                                                    count+=1
                                                                    continue
                                                                if (d+h+l+p != lineSum):
                                                                    count+=1
                                                                    continue
                                                                if (a+f+k+p != lineSum):
                                                                    count+=1
                                                                    continue
                                                                if (k+l+o+p != lineSum):
                                                                    count+=1
                                                                    continue
                                                                match+=1
                                                                print("%3d"%a,"%3d"%b,"%3d"%c,"%3d"%d)
                                                                print("%3d"%e,"%3d"%f,"%3d"%g,"%3d"%h)
                                                                print("%3d"%i,"%3d"%j,"%3d"%k,"%3d"%l)
                                                                print("%3d"%m,"%3d"%n,"%3d"%o,"%3d"%p)
                                                                print(" ")
                                    
                                   


print("Total Count/Match = ", count, "/", match)
print("Execution Time =", time.time() - start)



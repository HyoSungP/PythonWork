from __future__ import print_function
import copy
import time
import sys

start=time.time()

def new_list_remove(src, a):
    new_list = copy.deepcopy(src) # src.copy() - in case of list of list 
    new_list.remove(a)
    return new_list

lineSum = 15  # Sum of 1~9 is 45 therfore all line sum should be 15
alist = [1,2,3,4,5,6,7,8,9]
#blist = clist = dlist = elist = flist = glist = hlist = ilist = alist
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
                for e in elist:     
                    flist = new_list_remove(elist,e)
                    count+=1
                    for f in flist:                  
                        glist = new_list_remove(flist,f)
                        count+=1
                        for g in glist:                       
                            hlist = new_list_remove(glist,g)
                            count+=1
                            for h in hlist:                            
                                ilist = new_list_remove(hlist,h)
                                count+=1
                                for i in ilist:
                                    count+=1
                                    if (a+b+c != lineSum):
                                        count+=1
                                        continue
                                    if (d+e+f != lineSum):
                                        count+=1
                                        continue
                                    if (g+h+i != lineSum):
                                        count+=1
                                        continue
                                    if (a+d+g != lineSum):
                                        count+=1
                                        continue
                                    if (b+e+h != lineSum):
                                        count+=1
                                        continue
                                    if (c+f+i != lineSum):
                                        count+=1
                                        continue
                                    if (a+e+i != lineSum):
                                        count+=1
                                        continue
                                    if (c+e+g != lineSum):
                                        count+=1
                                        continue
                                    match+=1
                                    print("%d"%a,"%d"%b,"%d"%c,'\n',"%d"%d, "%d"%e,"%d"%f,'\n',"%d"%g,"%d"%h,"%d"%i)
                                    print("--------------")


print("Total Count/Match = ", count, "/", match, file= sys.stderr)
print("Execution Time =", time.time() - start, file= sys.stderr)



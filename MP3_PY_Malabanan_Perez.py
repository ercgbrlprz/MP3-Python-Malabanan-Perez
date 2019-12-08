#MachineProblem3
#Malabanan,Angelo-Perez,Eric
#2-ece-a
import numpy as np

def MP3_ML_Malabanan_Perez(x):
    
    l = len(x)
       
    for w in range(l):
        
        f = np.polyfit(x[:,0], x[:,1], w)
        
        p1 = x[:,1]
        p2 = np.polyval(f, x[:,0])
        
        P = np.linalg.norm(p1-p2)
        
        x2 = [w,P]
        
        if w == 0: 
            
            y = x2        
                    
        elif y[1] >= x2[1]: 
            
            z = x2[0]         

    P = f.argmin()
    f = np.polyfit(x[:,0], x[:,1], z)
    
    print (f)
print('please input array with example,np.array([(1,2),(2,3),(3,4),(4,6)])\n')
print('then enter def MP3_ML_Malabanan_Perez(x)\n')
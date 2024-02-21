
def Disks(k , main, target, helper):
    if k==1:
        print ("Move disk 1 from source",main,"to destination",target)
        return

    else:
        Disks(k-1, main, helper, target)
    
        print ("Move disk",k,"from source",main,"to destination",target)
        Disks(k-1, helper, target, main)
         

k = 4
Disks(k,'A','B','C')
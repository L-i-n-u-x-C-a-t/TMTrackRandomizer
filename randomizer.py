from donadigo.savegbx import * #import code made by donadigo (tho i cleaned up unneeded functions)
import random 
   
    
def randomize(name,loop,start, template):
    output = name + ".Challenge.Gbx"
    trackdata = []
    cplist = [13,20,45,46,72,73,114,115,116,117,118,119,120,200,208] #used for CP counter.
    cpcount = 0
    for i in range(loop):
        flags = 0
        block = random.randint(1, 292)
        x = random.randint(0,31)
        y = random.randint(0,31)
        z = random.randint(0,31)
        if y == 0:
            flags |= 0x1000
        if block == 210: #workaround due to a bug in pygbx
            block = 214
        if block != 14: #avoid putting accidental start points
            if block != 16:
                trackdata.append((block, x, y, z, random.randint(0,3), flags))
        if block in cplist:cpcount+=1

    if start == 1:
        trackdata.append((16,random.randint(0,31), random.randint(0,31), random.randint(0,31), random.randint(0,3)))
    else:
        trackdata.append((14,random.randint(0,31), random.randint(0,31), random.randint(0,31), random.randint(0,3)))

    options = {"track_data":trackdata, "map_name":name}
    save_gbx(options, template, output)
    return cpcount




if __name__ == "__main__":
    name = str(input("Name of the map : "))
    loop = int(input("Number of blocks : "))
    start = int(input("Type of start (Normal = 0, multilap = 1) : "))
    print("Done!\nNumber of checkpoints : "+randomize(name,loop,start))

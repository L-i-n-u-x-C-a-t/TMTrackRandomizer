from donadigo.savegbx import * #import code made by donadigo (tho i cleaned up unneeded functions)

name = str(input("Name of the map : "))
loop = int(input("Number of blocks : "))
start = int(input("Type of start (Normal = 0, multilap = 1) : "))
output = name + ".Challenge.Gbx"
template = "Template.Challenge.Gbx"
trackdata = []
for i in range(loop):
    block = random.randint(1, 292)
    if block == 210: #workaround due to a bug in pygbx
        block = 214
    if block != 14: #avoid putting accidental start points
        if block != 16:
            trackdata.append((block,random.randint(0,31), random.randint(0,31), random.randint(0,31), random.randint(0,3)))
#track data format : [(block, x,y,z,rotation),(...)]
if start == 1:
    trackdata.append((16,random.randint(0,31), random.randint(0,31), random.randint(0,31), random.randint(0,3)))
else:
    trackdata.append((14,random.randint(0,31), random.randint(0,31), random.randint(0,31), random.randint(0,3)))

options = {"track_data":trackdata, "map_name":name}
save_gbx(options, template, output)
print("Done!")

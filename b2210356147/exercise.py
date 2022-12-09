import os,sys
current_dir_path=os.getcwd()
txtinput=[]
info={}
namelist=[]
def fread():
    reading_file_name = "Students.txt"
    reading_file_path = os.path.join(current_dir_path, reading_file_name)
    with open(reading_file_path, "r") as i:
        count = 0
        while True:
            count += 1
            line = i.readline()
            if not line:
                break
            txtinput.append(line)
        i.close()
def scan():
    i=0
    while i<len(txtinput):
        strscan=txtinput[i]
        strscan=strscan.strip("\n")
        data=strscan.split(":")
        namelist.append(data[0])
        info.update({data[0]:data[1]})
        i+=1
def fwrite():
        if len(sys.argv)==2:
            command=sys.argv[1]
        else:
            command=input()
        name=command.split(",")
        for i in range(len(name)):
            sysinfo=info.get(name[i])
            if name[i] in namelist:
                print("Name: {}, University: {} ".format(name[i],sysinfo))
            else:
                raise NameError("No record of '{}' was found!".format(name[i]))
fread()
scan()
fwrite()
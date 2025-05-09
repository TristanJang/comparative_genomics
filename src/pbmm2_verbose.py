import subprocess

# takes contents of isolate txt file and creates a dicitonary of lists with patient ID (key) and list of pre and post isolates (values)
with open('isolates.txt', 'r') as f:
    lines = f.readlines()
    data = {}
    c = 0
    v = []
    for line in lines:
        line = line.strip()
        c +=1
        if c%2==1:
            key = str(line)[0:3]
            v.append(line)
        elif c%2==0:
            v.append(line)
            if str(v[0])[0:3] == str(v[1])[0:3]:
                value = v
                data[key] = value
            v =[]
            key = None
            value = None
print(data)
f = open("patientIDs.txt","w")
for d in data:
    f.write(d + "\n")
for patient in data:
    pre = patient
    path1 = "../../../../grp/valafar/data/depot/assembly/south_africa/genomes_renamed/"
    post = data[patient][1]
    path2 = "../../../../grp/valafar/data/depot/assembly/south_africa/" + data[patient][1] + "/"
    output = patient + "_pre_post_aligned.bam"
    command = "pbmm2 align " + path1 + pre + "_pre.fasta " + path2 + post + ".fastq " + output + " --sort --rg '@RG\tID:myid\tSM:mysample' --preset CCS --sample " + patient
    subprocess.call(command, shell=True)
    print("Alignment file for Patient " + patient + " was generated.")

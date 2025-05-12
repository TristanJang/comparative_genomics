import subprocess
with open('/grp/valafar/data/depot/assembly/south_africa/isolates_new_bsl.txt', 'r') as f:
    lines = f.readlines()
    data = {}
    for line in lines:
        line = line.strip()
        key = str(line)[0:3]
        data[key] = line
        #key = None
        #value = None

for d in data:
    command = "mv " + d +"_clair3_selected.vcf " + data[d] + "_clair3_selected_ref_bsl.vcf"
    print(command)
    #subprocess.call(command,shell=True)

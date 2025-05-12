import vcf
import matplotlib.pyplot as plt

input_file = "/grp/valafar/data/depot/assembly/south_africa/variants/het_clair3_ref_H37Rv/A04_B124_FV_New_clair3.vcf"
vcf_reader = vcf.Reader(open(input_file, 'r'))
x = []
y = []
z = []
a = []
for record in vcf_reader:
    if record.FILTER == ['LowQual']:
        y.append(record.samples[0]['AD'][1])
        x.append(record.samples[0]['DP'])
    else:
        z.append(record.samples[0]['DP'])
        a.append(record.samples[0]['AD'][1])
plt.scatter(x, y, color='purple')
plt.scatter(z, a, color='yellow')
plt.xlabel("Depth")
plt.ylabel("VSR")
plt.savefig('plot.png')

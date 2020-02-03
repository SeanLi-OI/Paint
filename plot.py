import xlrd 
import numpy as np
import matplotlib.pylab as pylab
import matplotlib
from matplotlib import pyplot as plt 
from matplotlib.ticker import FuncFormatter
import pylab
params = {
            'axes.labelsize': '16',
            'xtick.labelsize': '16',
            'ytick.labelsize': '12',
            'lines.linewidth': '3',
            'legend.fontsize': '12',
            'figure.figsize': '25, 5'  # set figure size
        }
pylab.rcParams.update(params)

col = [4,10,15]
labels = ['baseline']
titles = ["MC average idle rate(a)","MC average idle rate(b)","Average Bandwidth(a)","Average Bandwidth(b)","Power Reduction"]
markers = ['.','v','^','1','s','p','*','+','x','D',matplotlib.markers.CARETDOWNBASE,'P',',','h']
for i in range(15):
    labels.append(pf_labels[int(i/5)] + '_' + rp_labels[int(i%5)])
###################################
# a=np.array(table.col_values(15)[1:]).reshape(12,22)
# b = a[:,1]

# for i in range(12):
#     a[i]=a[i] - b[i]


###################################


def to_percent(temp, position):
    return '%.0f'%(100*temp) + '%'
  
j=0
fig, axs = plt.subplots(nrows=1, ncols=4)
#for row in axs:
#    for ax in row:
for ax in axs:
        DMCidle = np.array(table.col_values(col[j//2])[1:]).reshape(12,22)
        DMCidle = np.concatenate(( DMCidle[:,0:7], DMCidle[:,12:22]), axis=1) 
        baseline = DMCidle[:,1]
      #  print(DMCidle)
        for i in range(12):
            if(i!=0 and i!=2 ):
                if (j==0 and DMCidle[i,1]>0.5) or (j==1 and DMCidle[i,1]<0.5) or (j==2 and DMCidle[i,1]>3) or (j==3 and DMCidle[i,1]<3):
                    ax.plot(labels, DMCidle[i,1:], label= ds_labels[i],marker = markers[i])   
        ax.set_title(titles[j],fontsize=16)
        if(j>1):
            ax.set_ylabel("GB/s")
            ax.set_xticks(np.arange(len(labels)))
            ax.set_xticklabels(labels)
            #plt.xticks(rotation=90) 
            for xtick in ax.get_xticklabels():
                xtick.set_rotation(65)
        else:
            ax.set_xticks(np.arange(len(labels)))
            ax.set_xticklabels(labels)
            #plt.xticks(rotation=90) 
            for xtick in ax.get_xticklabels():
                xtick.set_rotation(65)
            ax.yaxis.set_major_formatter(FuncFormatter(to_percent))
        if j==1:
           fig.legend(bbox_to_anchor=(0.26,1.13),loc=2,prop={'size':15}, ncol=5) #  
        j=j+1
fig.tight_layout()
plt.savefig(FIG_DIR+"idle_bw_lx.pdf", bbox_inches="tight")
plt.show()
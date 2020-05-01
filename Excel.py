from matplotlib import pyplot as plt
import math
import numpy as np
import pandas as pd

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

def main():
    LT = pd.read_excel('LTSpiceData.xlsx')
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    fig = plt.figure()
    host = fig.add_subplot(111)
    fig.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()

    host.set_xlabel(r'\textbf{Widerstand in $\Omega$}', fontsize=11)
    host.set_ylabel("Power in W")
    par1.set_ylabel("Voltage in V")
    par2.set_ylabel("Current in A")

    par2.spines['right'].set_position(('outward', 60))
    make_patch_spines_invisible(par2)
    par2.spines['right'].set_visible(True)

    LT.head(30).plot(x='Resistance', y='Power', color='g', ax=host, label = '_Power', legend = None)
    LT.head(30).plot(x='Resistance', y='Voltage', color='r', ax=par1, label = '_Voltage', legend = None)
    LT.head(30).plot(x='Resistance', y='Current', color='b', ax=par2, label = '_Current', legend = None)
    host.yaxis.label.set_color('g')
    par1.yaxis.label.set_color('r')
    par2.yaxis.label.set_color('b')

    plt.title(r'\textbf{Die Leistung und Spannung der Last}', fontsize=11)

    plt.savefig('pw_volt_rsv2.png')
    plt.show()

if __name__ == "__main__":
    main()
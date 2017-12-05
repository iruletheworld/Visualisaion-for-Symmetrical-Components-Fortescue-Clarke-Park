'''
'''

import matplotlib as mpl
import matplotlib.pyplot as plt


CONST_WITH = 1280
CONST_HEIGHT = 800
CONST_DPI = 100

CONST_BBOX_LEFT = 0.5
CONST_BBOX_HEIGT1 = 1.25
CONST_BBOX_HEIGT2 = 1.23
CONST_BBOX_HEIGT3 = 1.26

CONST_TITLE_FONTSIZE = 14

# matplotlib font settings
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times New Roman'
mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['mathtext.fontset'] = 'cm'


def pltTimeDom(time, 
               xlim_min, xlim_max,
               ylim_min, ylim_max,
               a, b, c, 
               a_pos, b_pos, c_pos, 
               a_neg, b_neg, c_neg, 
               zero, 
               alpha, beta, 
               alpha_pos, beta_pos, 
               alpha_neg, beta_neg, 
               d, q, 
               d_pos, q_pos, 
               d_neg, q_neg):

    fig_main = plt.figure(figsize=(CONST_WITH/CONST_DPI, CONST_HEIGHT/CONST_DPI), 
                          dpi=CONST_DPI, num='Time domain plots')
    
    # 3-phase inputs and symmetrical components
    ax1 = plt.subplot(4, 3, 1)
    ax1_a, = ax1.plot(time, a, label=r'Phase-A Input', color='r', lw=2)
    ax1_b, = ax1.plot(time, b, label=r'Phase-B Input', color='g', lw=2)
    ax1_c, = ax1.plot(time, c, label=r'Phase-C Input', color='b', lw=2)

    ax1.set_title('Three-Phase Inputs', y=1.2, 
                  family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    ax1_legend = plt.legend(handles=[ax1_a, ax1_b, ax1_c], fontsize=9,
                            ncol=3,                            
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT1])
    
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax2 = plt.subplot(4, 3, 4)
    ax2_a, = ax2.plot(time, a_pos, label=r'Phase-A +', color='r', lw=2)
    ax2_b, = ax2.plot(time, b_pos, label=r'Phase-B +', color='g', lw=2)
    ax2_c, = ax2.plot(time, c_pos, label=r'Phase-C +', color='b', lw=2)
    ax2_legend = plt.legend(handles=[ax2_a, ax2_b, ax2_c], fontsize=9,
                            ncol=3,                            
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT2])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax3 = plt.subplot(4, 3, 7)
    ax3_a, = ax3.plot(time, a_neg, label=r'Phase-A -', color='r', lw=2)
    ax3_b, = ax3.plot(time, b_neg, label=r'Phase-B -', color='g', lw=2)
    ax3_c, = ax3.plot(time, c_neg, label=r'Phase-C -', color='b', lw=2)
    ax3_legend = plt.legend(handles=[ax3_a, ax3_b, ax3_c], fontsize=9,
                            ncol=3,
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT2])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax4 = plt.subplot(4, 3, 10)
    ax4_zero, = ax4.plot(time, zero, label=r'Zero Sequence', color='slateblue', lw=2)
    ax4_legend = plt.legend(handles=[ax4_zero], fontsize=9,
                            ncol=3,
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT2])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    plt.xlabel('Time (s)')


    # Clarke Transfroms
    ax5 = plt.subplot(4, 3, 2)
    ax5_alpha, = ax5.plot(time, alpha, label=r'$\alpha$', color='r', lw=2)
    ax5_beta, = ax5.plot(time, beta, label=r'$\beta$', color='g', lw=2)

    ax5.set_title('Clarke Transforms', y=1.2, 
                  family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    ax5_legend = plt.legend(handles=[ax5_alpha, ax5_beta], fontsize=9,
                            ncol=3,
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT1])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax6 = plt.subplot(4, 3, 5)
    ax6_alpha_pos, = ax6.plot(time, alpha_pos, label=r'$\alpha_+$  (DSOGI)', color='r', lw=2)
    ax6_beta_pos, = ax6.plot(time, beta_pos, label=r'$\beta_+$ (DSOGI)', color='g', lw=2)
    ax6_legend = plt.legend(handles=[ax6_alpha_pos, ax6_beta_pos], fontsize=9,
                            ncol=3,                            
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT3])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax7 = plt.subplot(4, 3, 8)
    ax7_alpha_neg, = ax7.plot(time, alpha_neg, label=r'$\alpha_-$ (DSOGI)', color='r', lw=2)
    ax7_beta_neg, = ax7.plot(time, beta_neg, label=r'$\beta_-$ (DSOGI)', color='g', lw=2)
    ax7_legend = plt.legend(handles=[ax7_alpha_neg, ax7_beta_neg], fontsize=9,
                            ncol=3,                            
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT3])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax8 = plt.subplot(4, 3, 11)
    ax8_zero, = ax8.plot(time, zero, label=r'Zero Sequence', color='slateblue', lw=2)
    ax8_legend = plt.legend(handles=[ax8_zero], fontsize=9,
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT2])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    plt.xlabel('Time (s)')

    # Parke Transforms
    ax9 = plt.subplot(4, 3, 3)
    ax9_d, = ax9.plot(time, d, label=r'$d$', color='r', lw=2)
    ax9_q, = ax9.plot(time, q, label=r'$q$', color='g', lw=2)

    ax9.set_title('Park Transforms', y=1.2, 
                  family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    ax9_legend = plt.legend(handles=[ax9_d, ax9_q], fontsize=9,
                            ncol=2,
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT1])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax10 = plt.subplot(4, 3, 6)
    ax10_d_pos, = ax10.plot(time, d_pos, label=r'$d_+$', color='r', lw=2)
    ax10_q_pos, = ax10.plot(time, q_pos, label=r'$q_+$', color='g', lw=2)
    ax10_legend = plt.legend(handles=[ax10_d_pos, ax10_q_pos], fontsize=9,
                             ncol=2,
                             loc='upper center',
                             bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT3])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax11 = plt.subplot(4, 3, 9)
    ax11_d_neg, = ax11.plot(time, d_neg, label=r'$d_-$', color='r', lw=2)
    ax11_q_neg, = ax11.plot(time, q_neg, label=r'$q_-$', color='g', lw=2)
    ax11_legend = plt.legend(handles=[ax11_d_neg, ax11_q_neg], fontsize=9,
                             ncol=2,
                             loc='upper center',
                             bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT3])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax12 = plt.subplot(4, 3, 12)
    ax12_zero, = ax12.plot(time, zero, label=r'Zero Sequence', color='slateblue', lw=2)
    ax12_legend = plt.legend(handles=[ax12_zero], fontsize=9,
                             ncol=2,
                             loc='upper center',
                             bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT2])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    plt.xlabel('Time (s)')

    plt.tight_layout(h_pad=1.7, rect=[0, -0.01, 1, 1])
    plt.show()

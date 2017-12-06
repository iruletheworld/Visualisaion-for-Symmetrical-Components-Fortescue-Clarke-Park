'''
'''

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


CONST_WITH = 1280
CONST_HEIGHT = 800
CONST_DPI = 100

CONST_BBOX_LEFT = 0.5
CONST_BBOX_HEIGT1 = 1.25
CONST_BBOX_HEIGT2 = 1.23
CONST_BBOX_HEIGT3 = 1.26

CONST_TITLE_FONTSIZE = 14

CONST_COLOR_CMB_A = 'red'
CONST_COLOR_CMB_B = 'green'
CONST_COLOR_CMB_C = 'blue'

CONST_COLOR_POS_A = 'red'
CONST_COLOR_POS_B = 'green'
CONST_COLOR_POS_C = 'blue'

CONST_COLOR_NEG_A = 'salmon'
CONST_COLOR_NEG_B = 'mediumseagreen'
CONST_COLOR_NEG_C = 'skyblue'

CONST_COLOR_ZERO  = 'black'

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
                          dpi=CONST_DPI, 
                          num='Time Domain Plots')
    
    # 3-phase inputs and symmetrical components
    ax1 = plt.subplot(4, 3, 1)
    ax1_a, = ax1.plot(time, a, label=r'Phase-A Input', color=CONST_COLOR_CMB_A, lw=2)
    ax1_b, = ax1.plot(time, b, label=r'Phase-B Input', color=CONST_COLOR_CMB_B, lw=2)
    ax1_c, = ax1.plot(time, c, label=r'Phase-C Input', color=CONST_COLOR_CMB_C, lw=2)

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
    ax2_a, = ax2.plot(time, a_pos, label=r'Phase-A +', color=CONST_COLOR_POS_A, lw=2)
    ax2_b, = ax2.plot(time, b_pos, label=r'Phase-B +', color=CONST_COLOR_POS_B, lw=2)
    ax2_c, = ax2.plot(time, c_pos, label=r'Phase-C +', color=CONST_COLOR_POS_C, lw=2)

    ax2_legend = plt.legend(handles=[ax2_a, ax2_b, ax2_c], fontsize=9,
                            ncol=3,                            
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT2])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax3 = plt.subplot(4, 3, 7)
    ax3_a, = ax3.plot(time, a_neg, label=r'Phase-A -', color=CONST_COLOR_NEG_A, lw=2)
    ax3_b, = ax3.plot(time, b_neg, label=r'Phase-B -', color=CONST_COLOR_NEG_B, lw=2)
    ax3_c, = ax3.plot(time, c_neg, label=r'Phase-C -', color=CONST_COLOR_NEG_C, lw=2)
    ax3_legend = plt.legend(handles=[ax3_a, ax3_b, ax3_c], fontsize=9,
                            ncol=3,
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT2])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax4 = plt.subplot(4, 3, 10)
    ax4_zero, = ax4.plot(time, zero, label=r'Zero Sequence', color=CONST_COLOR_ZERO, lw=2)

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
    ax5_alpha, = ax5.plot(time, alpha, label=r'$\alpha$', color=CONST_COLOR_CMB_A, lw=2)
    ax5_beta, = ax5.plot(time, beta, label=r'$\beta$', color=CONST_COLOR_CMB_B, lw=2)

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
    ax6_alpha_pos, = ax6.plot(time, alpha_pos, label=r'$\alpha_+$  (DSOGI)', color=CONST_COLOR_POS_A, lw=2)
    ax6_beta_pos, = ax6.plot(time, beta_pos, label=r'$\beta_+$ (DSOGI)', color=CONST_COLOR_POS_B, lw=2)

    ax6_legend = plt.legend(handles=[ax6_alpha_pos, ax6_beta_pos], fontsize=9,
                            ncol=3,                            
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT3])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax7 = plt.subplot(4, 3, 8)
    ax7_alpha_neg, = ax7.plot(time, alpha_neg, label=r'$\alpha_-$ (DSOGI)', color=CONST_COLOR_NEG_A, lw=2)
    ax7_beta_neg, = ax7.plot(time, beta_neg, label=r'$\beta_-$ (DSOGI)', color=CONST_COLOR_NEG_B, lw=2)

    ax7_legend = plt.legend(handles=[ax7_alpha_neg, ax7_beta_neg], fontsize=9,
                            ncol=3,                            
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT3])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax8 = plt.subplot(4, 3, 11)
    ax8_zero, = ax8.plot(time, zero, label=r'Zero Sequence', color=CONST_COLOR_ZERO, lw=2)

    ax8_legend = plt.legend(handles=[ax8_zero], fontsize=9,
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT2])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    plt.xlabel('Time (s)')

    # Parke Transforms
    ax9 = plt.subplot(4, 3, 3)
    ax9_d, = ax9.plot(time, d, label=r'$d$', color=CONST_COLOR_CMB_A, lw=2)
    ax9_q, = ax9.plot(time, q, label=r'$q$', color=CONST_COLOR_CMB_B, lw=2)

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
    ax10_d_pos, = ax10.plot(time, d_pos, label=r'$d_+$', color=CONST_COLOR_POS_A, lw=2)
    ax10_q_pos, = ax10.plot(time, q_pos, label=r'$q_+$', color=CONST_COLOR_POS_B, lw=2)

    ax10_legend = plt.legend(handles=[ax10_d_pos, ax10_q_pos], fontsize=9,
                             ncol=2,
                             loc='upper center',
                             bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT3])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax11 = plt.subplot(4, 3, 9)
    ax11_d_neg, = ax11.plot(time, d_neg, label=r'$d_-$', color=CONST_COLOR_NEG_A, lw=2)
    ax11_q_neg, = ax11.plot(time, q_neg, label=r'$q_-$', color=CONST_COLOR_NEG_B, lw=2)

    ax11_legend = plt.legend(handles=[ax11_d_neg, ax11_q_neg], fontsize=9,
                             ncol=2,
                             loc='upper center',
                             bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT3])

    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    plt.grid(True)

    ax12 = plt.subplot(4, 3, 12)
    ax12_zero, = ax12.plot(time, zero, label=r'Zero Sequence', color=CONST_COLOR_ZERO, lw=2)
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


def pltPolar(r_max,
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

    fig_polar = plt.figure(figsize=(CONST_WITH/CONST_DPI, CONST_HEIGHT/CONST_DPI), 
                           dpi=CONST_DPI, 
                           num='Polar Domain Plots')

    # plt.subplots_adjust(hspace=0.33)

    if len(a) > 20:

        Nth_marker = 20

    else:

        Nth_marker = int(len(a) / 2)

        if Nth_marker == 0:

            Nth_marker = 1


    # plot 1
    ax_polar1       = plt.subplot(231, projection='polar')

    polar1_input_a  = ax_polar1.plot(np.angle(a), abs(a), label=r'Phase-A Input',
                                     color=CONST_COLOR_CMB_A, lw=2,
                                     marker='.', markersize=10, 
                                     markevery=Nth_marker)

    polar1_input_b  = ax_polar1.plot(np.angle(b), abs(b), label=r'Phase-B Input',
                                     color=CONST_COLOR_CMB_B, lw=2,
                                     marker='.', markersize=10, 
                                     markevery=Nth_marker)

    polar1_input_c  = ax_polar1.plot(np.angle(c), abs(c), label=r'Phase-C Input',
                                     color=CONST_COLOR_CMB_C, lw=2,
                                     marker='.', markersize=10, 
                                     markevery=Nth_marker)
    
    # rotate the radius labels by -93 degrees
    ax_polar1.set_rlabel_position(-93)

    ax_polar1.set_title('Three-Phase Inputs', y=1.1,
                        family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    polar1_legned   = ax_polar1.legend(loc='upper left', bbox_to_anchor=[-0.5, 1.1])

    ax_polar1.set_rmax(r_max)

    # plot 2
    ax_polar2           = plt.subplot(234, projection='polar')

    polar2_input_a_pos  = ax_polar2.plot(np.angle(a_pos), abs(a_pos), label=r'Phase-A +',
                                         color=CONST_COLOR_POS_A, lw=2,
                                         marker='.', markersize=10, 
                                         markevery=Nth_marker)

    polar2_input_b_pos  = ax_polar2.plot(np.angle(b_pos), abs(b_pos), label=r'Phase-B +',
                                         color=CONST_COLOR_POS_B, lw=2,
                                         marker='.', markersize=10, 
                                         markevery=Nth_marker)

    polar2_input_c_pos  = ax_polar2.plot(np.angle(c_pos), abs(c_pos), label=r'Phase-C +',
                                         color=CONST_COLOR_POS_C, lw=2,
                                         marker='.', markersize=10, 
                                         markevery=Nth_marker)

    polar2_input_a_neg  = ax_polar2.plot(np.angle(a_neg), abs(a_neg), label=r'Phase-A -',
                                         color=CONST_COLOR_NEG_A, lw=2,
                                         marker='^', markersize=6, 
                                         markevery=Nth_marker)

    polar2_input_b_neg  = ax_polar2.plot(np.angle(b_neg), abs(b_neg), label=r'Phase-B -',
                                         color=CONST_COLOR_NEG_B, lw=2,
                                         marker='^', markersize=6, 
                                         markevery=Nth_marker)

    polar2_input_c_neg  = ax_polar2.plot(np.angle(c_neg), abs(c_neg), label=r'Phase-C -',
                                         color=CONST_COLOR_NEG_C, lw=2,
                                         marker='^', markersize=6, 
                                         markevery=Nth_marker)

    polar2_zero         = ax_polar2.plot(np.angle(zero), abs(zero), label=r'Zero',
                                         color=CONST_COLOR_ZERO, lw=2,
                                         marker='X', markersize=7,
                                         markevery=Nth_marker)

    # rotate the radius labels by -93 degrees
    ax_polar2.set_rlabel_position(-93)

    ax_polar2.set_title('Fortescue Components', y=1.1,
                        family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    polar2_legned       = ax_polar2.legend(loc='lower left', bbox_to_anchor=[-0.5, -0.2])

    ax_polar2.set_rmax(r_max)

    # plot 3
    ax_polar3       = plt.subplot(232, projection='polar')

    polar3_alpha    = ax_polar3.plot(np.angle(alpha), abs(alpha), label=r'$\alpha$',
                                     color=CONST_COLOR_CMB_A, lw=2,
                                     marker='.', markersize=10, 
                                     markevery=Nth_marker)
    
    polar3_beta     = ax_polar3.plot(np.angle(beta), abs(beta), label=r'$\beta$',
                                     color=CONST_COLOR_CMB_B, lw=2,
                                     marker='.', markersize=10, 
                                     markevery=Nth_marker)
    
    # rotate the radius labels by -93 degrees
    ax_polar3.set_rlabel_position(-93)

    ax_polar3.set_title('Clarke Transform', y=1.1,
                        family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    polar3_legned   = ax_polar3.legend(loc='upper right', bbox_to_anchor=[1.2, 1.1])
    
    ax_polar3.set_rmax(r_max)

    # plot 4
    ax_polar4           = plt.subplot(235, projection='polar')

    polar4_alpha_pos    = ax_polar4.plot(np.angle(alpha_pos), abs(alpha_pos), label=r'$\alpha_+$',
                                         color=CONST_COLOR_POS_A, lw=2,
                                         marker='.', markersize=10, 
                                         markevery=Nth_marker)
    
    polar4_beta_pos     = ax_polar4.plot(np.angle(beta_pos), abs(beta_pos), label=r'$\beta_+$',
                                         color=CONST_COLOR_POS_B, lw=2,
                                         marker='.', markersize=10, 
                                         markevery=Nth_marker)

    polar4_alpha_neg    = ax_polar4.plot(np.angle(alpha_neg), abs(alpha_neg), label=r'$\alpha_-$',
                                         color=CONST_COLOR_NEG_A, lw=2,
                                         marker='^', markersize=6, 
                                         markevery=Nth_marker)
    
    polar4_beta_neg     = ax_polar4.plot(np.angle(beta_neg), abs(beta_neg), label=r'$\beta_-$',
                                         color=CONST_COLOR_NEG_B, lw=2,
                                         marker='^', markersize=6, 
                                         markevery=Nth_marker)

    polar4_zero         = ax_polar4.plot(np.angle(zero), abs(zero), label=r'Zero',
                                         color=CONST_COLOR_ZERO, lw=2,
                                         marker='X', markersize=7,
                                         markevery=Nth_marker)

    # rotate the radius labels by -93 degrees
    ax_polar4.set_rlabel_position(-93)

    ax_polar4.set_title('Clarke Components (DSOGI)', y=1.1,
                        family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    polar4_legned       = ax_polar4.legend(loc='lower right', bbox_to_anchor=[1.3, -0.2])

    ax_polar4.set_rmax(r_max)

    # plot 5
    ax_polar5       = plt.subplot(233, projection='polar')

    polar5_d        = ax_polar5.plot(np.angle(d), abs(d), label=r'$d$',
                                     color=CONST_COLOR_CMB_A, lw=2,
                                     marker='.', markersize=10, 
                                     markevery=Nth_marker)

    # print(round(len(d)/4))
    
    polar5_q        = ax_polar5.plot(np.angle(q), abs(q), label=r'$q$',
                                     color=CONST_COLOR_CMB_B, lw=2, 
                                     marker='.', markersize=10, 
                                     markevery=Nth_marker)

    # rotate the radius labels by -93 degrees
    ax_polar5.set_rlabel_position(-93)
    
    ax_polar5.set_title('Park Transform', y=1.1,
                        family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')
    
    polar5_legned = ax_polar5.legend(loc='upper right', bbox_to_anchor=[1.2, 1.1])
    
    ax_polar5.set_rmax(r_max)

    # plot 6
    ax_polar6       = plt.subplot(236, projection='polar')

    polar6_d_pos    = ax_polar6.plot(np.angle(d_pos), abs(d_pos), label=r'$d_+$',
                                     color=CONST_COLOR_POS_A, lw=2,
                                     marker='.', markersize=10, 
                                     markevery=Nth_marker)

    polar6_q_pos    = ax_polar6.plot(np.angle(q_pos), abs(q_pos), label=r'$q_+$',
                                     color=CONST_COLOR_POS_B, lw=2,
                                     marker='.', markersize=10, 
                                     markevery=Nth_marker)

    polar6_d_neg    = ax_polar6.plot(np.angle(d_neg), abs(d_neg), label=r'$d_-$',
                                     color=CONST_COLOR_NEG_A, lw=2,
                                     marker='^', markersize=6, 
                                     markevery=Nth_marker)

    polar6_q_neg    = ax_polar6.plot(np.angle(q_neg), abs(q_neg), label=r'$q_-$',
                                     color=CONST_COLOR_NEG_B, lw=2,
                                     marker='^', markersize=6, 
                                     markevery=Nth_marker)

    polar6_zero     = ax_polar6.plot(np.angle(zero), abs(zero), label=r'Zero',
                                     color=CONST_COLOR_ZERO, lw=2,
                                     marker='X', markersize=7,
                                     markevery=Nth_marker)

    # rotate the radius labels by -93 degrees
    ax_polar6.set_rlabel_position(-93)

    ax_polar6.set_title('Park Components', y=1.1,
                        family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    polar6_legned = ax_polar6.legend(loc='lower right', bbox_to_anchor=[1.3, -0.2])

    ax_polar6.set_rmax(r_max)

    # plt.tight_layout(h_pad=0.5, rect=[0.06, 0.05, 0.98, 0.995])
    plt.tight_layout(rect=[0.06, 0.05, 0.98, 0.995])

    plt.show()

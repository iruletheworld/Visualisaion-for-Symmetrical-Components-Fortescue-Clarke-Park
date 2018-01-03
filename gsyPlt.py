"""
Custom module for plottings that I need. This module uses "matplotlib" heavily.

*Note that matplotlib would automatically disgard the imaginary part of a 
complex number when plotting it in the time domain.*

Module Name : gsyPlt

Author : 高斯羽 博士 (Dr. GAO, Siyu)

Version : 0.1.0

Last Modified : 2017-12-21

Change Log
----------------------
* **Notable changes:**

    + Version : 0.1.0
        - Added "pltPolarDom"
        - Added "pltTimeDom"

List of functions
----------------------

* pltPolarDom_
* pltTimeDom_

Function definitions
----------------------

"""

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

# =============================================================================
# <Function: plotting time domain data for symmetrical components>
# =============================================================================
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

    """
    .. _pltTimeDom :

    Plots the time domain data in a 4 by 3 grid of subplots.

    Parameters
    ----------
    time : float or a list of float
        Time data.

    xlim_min : float
        Minimum of x axis. This is also the minimum of time.

    xlim_max : float
        Maximum of x axis. This is also the maximum of time.

    ylim_min : float
        Minimum of y axis.

    ylim_max : float
        Maximum of y axis.

    a : float or a list of float
        Phase-A input.

    b : float or a list of float
        Phase-B input.

    c : float or a list of float
        Phase-C input.

    a_pos : float or a list of float
        Positive sequence of Phase-A input.

    b_pos : float or a list of float
        Positive sequence of Phase-B input.

    c_pos : float or a list of float
        Positive sequence of Phase-C input.

    a_neg : float or a list of float
        Negative sequence of Phase-A input.

    b_neg : float or a list of float
        Negative sequence of Phase-B input.

    c_neg : float or a list of float
        Negative sequence of Phase-C input.

    zero : float or a list of float
        The Zero sequence

    alpha : float or a list of float
        The :math:`\\alpha` component of the Clarke Transform.

    beta : float or a list of float
        The :math:`\\beta` component of the Clarke Transform.

    alpha_pos : float or a list of float
        The :math:`\\alpha_+` component of the Clarke Transform (DSOGI).

    beta_pos : float or a list of float
        The :math:`\\beta_+` component of the Clarke Transform (DSOGI).

    alpha_neg : float or a list of float
        The :math:`\\alpha_-` component of the Clarke Transform (DSOGI).

    beta_neg : float or a list of float
        The :math:`\\beta_-` component of the Clarke Transform (DSOGI).

    d : float or a list of float
        The :math:`d` component of the Park Transform.

    q : float or a list of float
        The :math:`q` component of the Park Transform.

    d_pos : float or a list of float
        The :math:`d_+` component of the Park Transform (by applying the 
        Park Transform on the DSOGI Clarke Transform components).

    q_pos : float or a list of float
        The :math:`q_+` component of the Park Transform (by applying the 
        Park Transform on the DSOGI Clarke Transform components).

    d_neg : float or a list of float
        The :math:`d_-` component of the Park Transform (by applying the 
        Park Transform on the DSOGI Clarke Transform components).

    q_neg : float or a list of float
        The :math:`q_-` component of the Park Transform (by applying the 
        Park Transform on the DSOGI Clarke Transform components).

    Returns
    -------
    fig_main : matplotlib figure object
        The figure object for time domain plots.
    
    Examples
    --------
    
    .. code :: python

        fig_time_dom = gsyPlt.pltTimeDom(time,
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
                                         d_neg, q_neg)
    """

    # make the figure
    fig_main = plt.figure(figsize=(CONST_WITH/CONST_DPI, CONST_HEIGHT/CONST_DPI), 
                          dpi=CONST_DPI, 
                          num='Time Domain Plots')
    
    # subplot 1---------------------------------------------------------------------#
    # 3-phase inputs
    ax1     = plt.subplot(4, 3, 1)
    ax1_a,  = ax1.plot(time, a, label=r'Phase-A Input', color=CONST_COLOR_CMB_A, lw=2)
    ax1_b,  = ax1.plot(time, b, label=r'Phase-B Input', color=CONST_COLOR_CMB_B, lw=2)
    ax1_c,  = ax1.plot(time, c, label=r'Phase-C Input', color=CONST_COLOR_CMB_C, lw=2)

    # set the axes title
    ax1.set_title('Three-Phase Inputs', y=1.2, 
                  family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    # set the axes legend
    ax1_legend = plt.legend(handles=[ax1_a, ax1_b, ax1_c], fontsize=9,
                            ncol=3,                            
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT1])
    
    # set axes limits
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    # grid on
    plt.grid(True)

    # subplot 2---------------------------------------------------------------------#
    # 3-phase positive sequence
    ax2     = plt.subplot(4, 3, 4)
    ax2_a,  = ax2.plot(time, a_pos, label=r'Phase-A +', color=CONST_COLOR_POS_A, lw=2)
    ax2_b,  = ax2.plot(time, b_pos, label=r'Phase-B +', color=CONST_COLOR_POS_B, lw=2)
    ax2_c,  = ax2.plot(time, c_pos, label=r'Phase-C +', color=CONST_COLOR_POS_C, lw=2)

    # set axes legend
    ax2_legend = plt.legend(handles=[ax2_a, ax2_b, ax2_c], fontsize=9,
                            ncol=3,                            
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT2])

    # set axes limits
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    # grid on
    plt.grid(True)

    # subplot 3---------------------------------------------------------------------#
    # 3-phase negative sequence
    ax3     = plt.subplot(4, 3, 7)
    ax3_a,  = ax3.plot(time, a_neg, label=r'Phase-A -', color=CONST_COLOR_NEG_A, lw=2)
    ax3_b,  = ax3.plot(time, b_neg, label=r'Phase-B -', color=CONST_COLOR_NEG_B, lw=2)
    ax3_c,  = ax3.plot(time, c_neg, label=r'Phase-C -', color=CONST_COLOR_NEG_C, lw=2)
    
    # set axes legend
    ax3_legend = plt.legend(handles=[ax3_a, ax3_b, ax3_c], fontsize=9,
                            ncol=3,
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT2])

    # set axes limits
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    # grid on
    plt.grid(True)

    # subplot 4---------------------------------------------------------------------#
    # zero sequence
    ax4         = plt.subplot(4, 3, 10)
    ax4_zero,   = ax4.plot(time, zero, label=r'Zero Sequence', color=CONST_COLOR_ZERO, lw=2)

    # set axes legend
    ax4_legend = plt.legend(handles=[ax4_zero], fontsize=9,
                            ncol=3,
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT2])

    # set axes legend
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    # grid on
    plt.grid(True)

    # set x axis label (used by all the subplots in the column)
    plt.xlabel('Time (s)')

    # subplot 5---------------------------------------------------------------------#
    # Clarke Transfrom
    ax5         = plt.subplot(4, 3, 2)
    ax5_alpha,  = ax5.plot(time, alpha, label=r'$\alpha$', color=CONST_COLOR_CMB_A, lw=2)
    ax5_beta,   = ax5.plot(time, beta, label=r'$\beta$', color=CONST_COLOR_CMB_B, lw=2)

    # set axes title
    ax5.set_title('Clarke Transforms', y=1.2, 
                  family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    # set axes title
    ax5_legend = plt.legend(handles=[ax5_alpha, ax5_beta], fontsize=9,
                            ncol=3,
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT1])

    # set axes limits
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    # grid on
    plt.grid(True)

    # subplot 6---------------------------------------------------------------------#
    # Clarke Transfrom positive sequence (DSOGI)
    ax6             = plt.subplot(4, 3, 5)
    ax6_alpha_pos,  = ax6.plot(time, alpha_pos, label=r'$\alpha_+$  (DSOGI)', color=CONST_COLOR_POS_A, lw=2)
    ax6_beta_pos,   = ax6.plot(time, beta_pos, label=r'$\beta_+$ (DSOGI)', color=CONST_COLOR_POS_B, lw=2)

    # set axes legend
    ax6_legend = plt.legend(handles=[ax6_alpha_pos, ax6_beta_pos], fontsize=9,
                            ncol=3,                            
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT3])

    # set axes limits
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    # grid on
    plt.grid(True)

    # subplot 7---------------------------------------------------------------------#
    # Clarke Transfrom negative sequence (DSOGI)
    ax7             = plt.subplot(4, 3, 8)
    ax7_alpha_neg,  = ax7.plot(time, alpha_neg, label=r'$\alpha_-$ (DSOGI)', color=CONST_COLOR_NEG_A, lw=2)
    ax7_beta_neg,   = ax7.plot(time, beta_neg, label=r'$\beta_-$ (DSOGI)', color=CONST_COLOR_NEG_B, lw=2)

    # set axes legend
    ax7_legend = plt.legend(handles=[ax7_alpha_neg, ax7_beta_neg], fontsize=9,
                            ncol=3,                            
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT3])

    # set axes limits
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    # grid on
    plt.grid(True)

    # subplot 8---------------------------------------------------------------------#
    # zero sequence
    ax8         = plt.subplot(4, 3, 11)
    ax8_zero,   = ax8.plot(time, zero, label=r'Zero Sequence', color=CONST_COLOR_ZERO, lw=2)

    # set axes legend
    ax8_legend = plt.legend(handles=[ax8_zero], fontsize=9,
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT2])

    # set axes limits
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    # grid on
    plt.grid(True)

    # set x axis label (used by all the subplots in the column)
    plt.xlabel('Time (s)')

    # subplot 9---------------------------------------------------------------------#
    # Parke Transform
    ax9     = plt.subplot(4, 3, 3)
    ax9_d,  = ax9.plot(time, d, label=r'$d$', color=CONST_COLOR_CMB_A, lw=2)
    ax9_q,  = ax9.plot(time, q, label=r'$q$', color=CONST_COLOR_CMB_B, lw=2)

    # set axes title
    ax9.set_title('Park Transforms', y=1.2, 
                  family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    # set axes legend
    ax9_legend = plt.legend(handles=[ax9_d, ax9_q], fontsize=9,
                            ncol=2,
                            loc='upper center',
                            bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT1])

    # set axes limits
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    # grid on
    plt.grid(True)

    # subplot 10---------------------------------------------------------------------#
    # Park Transform, positive sequence (by applying the normal Park Transform on the
    # DSOGI Clarke Transform's positive sequence)
    ax10        = plt.subplot(4, 3, 6)
    ax10_d_pos, = ax10.plot(time, d_pos, label=r'$d_+$', color=CONST_COLOR_POS_A, lw=2)
    ax10_q_pos, = ax10.plot(time, q_pos, label=r'$q_+$', color=CONST_COLOR_POS_B, lw=2)

    # set axes legend
    ax10_legend = plt.legend(handles=[ax10_d_pos, ax10_q_pos], fontsize=9,
                             ncol=2,
                             loc='upper center',
                             bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT3])

    # set axes limits
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    # grid on
    plt.grid(True)

    # subplot 11---------------------------------------------------------------------#
    # Park Transform, negative sequence (by applying the normal Park Transform on the
    # DSOGI Clarke Transform's negative sequence)
    ax11        = plt.subplot(4, 3, 9)
    ax11_d_neg, = ax11.plot(time, d_neg, label=r'$d_-$', color=CONST_COLOR_NEG_A, lw=2)
    ax11_q_neg, = ax11.plot(time, q_neg, label=r'$q_-$', color=CONST_COLOR_NEG_B, lw=2)

    # set axes legend
    ax11_legend = plt.legend(handles=[ax11_d_neg, ax11_q_neg], fontsize=9,
                             ncol=2,
                             loc='upper center',
                             bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT3])

    # set axes limits
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    # grid on
    plt.grid(True)

    # subplot 12---------------------------------------------------------------------#
    # zero sequence
    ax12        = plt.subplot(4, 3, 12)
    ax12_zero,  = ax12.plot(time, zero, label=r'Zero Sequence', color=CONST_COLOR_ZERO, lw=2)

    # set axes legend
    ax12_legend = plt.legend(handles=[ax12_zero], fontsize=9,
                             ncol=2,
                             loc='upper center',
                             bbox_to_anchor=[CONST_BBOX_LEFT, CONST_BBOX_HEIGT2])

    # set axes limits
    plt.xlim([xlim_min, xlim_max])
    plt.ylim([ylim_min, ylim_max])

    # grid on
    plt.grid(True)

    # set x axis label (used by all the subplots in the column)
    plt.xlabel('Time (s)')

    # reduce white space of the figure
    plt.tight_layout(h_pad=1.7, rect=[0, -0.01, 1, 1])

    # show the figure
    plt.show()

    return fig_main
# =============================================================================
# </Function: plotting time domain data for symmetrical components>
# =============================================================================


# =============================================================================
# <Function: plotting polar domain data for symmetrical components>
# =============================================================================
def pltPolarDom(r_max,
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

    """
    .. _pltPolarDom :

    Plots the polar domain data in a 3 by 3 grid of subplots.

    Parameters
    ----------
    r_max : float 
        Radius limit.

    a : complex or a list of complex
        Phase-A input.

    b : complex or a list of complex
        Phase-B input.

    c : complex or a list of complex
        Phase-C input.

    a_pos : complex or a list of complex
        Positive sequence of Phase-A input.

    b_pos : complex or a list of complex
        Positive sequence of Phase-B input.

    c_pos : complex or a list of complex
        Positive sequence of Phase-C input.

    a_neg : complex or a list of complex
        Negative sequence of Phase-A input.

    b_neg : complex or a list of complex
        Negative sequence of Phase-B input.

    c_neg : complex or a list of complex
        Negative sequence of Phase-C input.

    zero : complex or a list of complex
        The Zero sequence

    alpha : complex or a list of complex
        The :math:`\\alpha` component of the Clarke Transform.

    beta : complex or a list of complex
        The :math:`\\beta` component of the Clarke Transform.

    alpha_pos : complex or a list of complex
        The :math:`\\alpha_+` component of the Clarke Transform (DSOGI).

    beta_pos : complex or a list of complex
        The :math:`\\beta_+` component of the Clarke Transform (DSOGI).

    alpha_neg : complex or a list of complex
        The :math:`\\alpha_-` component of the Clarke Transform (DSOGI).

    beta_neg : complex or a list of complex
        The :math:`\\beta_-` component of the Clarke Transform (DSOGI).

    d : complex or a list of complex
        The :math:`d` component of the Park Transform.

    q : complex or a list of complex
        The :math:`q` component of the Park Transform.

    d_pos : complex or a list of complex
        The :math:`d_+` component of the Park Transform (by applying the 
        Park Transform on the DSOGI Clarke Transform components).

    q_pos : complex or a list of complex
        The :math:`q_+` component of the Park Transform (by applying the 
        Park Transform on the DSOGI Clarke Transform components).

    d_neg : complex or a list of complex
        The :math:`d_-` component of the Park Transform (by applying the 
        Park Transform on the DSOGI Clarke Transform components).

    q_neg : complex or a list of complex
        The :math:`q_-` component of the Park Transform (by applying the 
        Park Transform on the DSOGI Clarke Transform components).

    Returns
    -------
    fig_polar : matplotlib figure object
        The figure object for polar domain plots.
    
    Examples
    --------
    
    .. code :: python

        fig_polar_dom = gsyPlt.pltPolarDom(r_max,
                                           a, b, c,
                                           a_pos, b_pos, c_pos,
                                           a_neg, b_neg, c_neg,
                                           zero,
                                           alpha, beta,
                                           alpha_pos, beta_pos,
                                           alpha_neg, beta_neg,
                                           d, q,
                                           d_pos, q_pos,
                                           d_neg, q_neg)
    """
    # make the figure
    fig_polar = plt.figure(figsize=(CONST_WITH/CONST_DPI, CONST_HEIGHT/CONST_DPI), 
                           dpi=CONST_DPI, 
                           num='Polar Domain Plots')

    # plt.subplots_adjust(hspace=0.33)

    # set marker distance for lines. The numbers were achieved via experiments.
    if len(a) > 20:

        Nth_marker = 20

    else:

        Nth_marker = int(len(a) / 2)

        if Nth_marker == 0:

            Nth_marker = 1


    # subplot 1---------------------------------------------------------------------#
    # 3-phase inputs
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
    
    # rotate the radius labels by -93 degrees (clockwise)
    ax_polar1.set_rlabel_position(-93)

    # set axes title
    ax_polar1.set_title('Three-Phase Inputs', y=1.1,
                        family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    # set axes legend. Note that for polar, no handles in "legend"
    polar1_legned   = ax_polar1.legend(loc='upper left', bbox_to_anchor=[-0.5, 1.1])

    # set radius limit
    ax_polar1.set_rmax(r_max)

    # subplot 2---------------------------------------------------------------------#
    # 3-phase symmetrical components (all)
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

    # set axes title
    ax_polar2.set_title('Fortescue Components', y=1.1,
                        family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    # set axes legend
    polar2_legned       = ax_polar2.legend(loc='lower left', bbox_to_anchor=[-0.5, -0.2])

    # set radius limit
    ax_polar2.set_rmax(r_max)

    # subplot 3---------------------------------------------------------------------#
    # Clarke Transform
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

    # set axes title
    ax_polar3.set_title('Clarke Transform', y=1.1,
                        family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    # set axes legend
    polar3_legned   = ax_polar3.legend(loc='upper right', bbox_to_anchor=[1.2, 1.1])
    
    # set radius limit
    ax_polar3.set_rmax(r_max)

    # subplot 4---------------------------------------------------------------------#
    # Clarke Transforms' symmetrical components (all, according to dDSOGI)
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

    # set axes title
    ax_polar4.set_title('Clarke Components (DSOGI)', y=1.1,
                        family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    # set axes legend
    polar4_legned       = ax_polar4.legend(loc='lower right', bbox_to_anchor=[1.3, -0.2])

    # set radius limit
    ax_polar4.set_rmax(r_max)

    # subplot 5---------------------------------------------------------------------#
    # Park Transform
    ax_polar5       = plt.subplot(233, projection='polar')

    polar5_d        = ax_polar5.plot(np.angle(d), abs(d), label=r'$d$',
                                     color=CONST_COLOR_CMB_A, lw=2,
                                     marker='.', markersize=10, 
                                     markevery=Nth_marker)
    
    polar5_q        = ax_polar5.plot(np.angle(q), abs(q), label=r'$q$',
                                     color=CONST_COLOR_CMB_B, lw=2, 
                                     marker='.', markersize=10, 
                                     markevery=Nth_marker)

    # rotate the radius labels by -93 degrees
    ax_polar5.set_rlabel_position(-93)
    
    # set axes title
    ax_polar5.set_title('Park Transform', y=1.1,
                        family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')
    
    # set axes legend
    polar5_legned = ax_polar5.legend(loc='upper right', bbox_to_anchor=[1.2, 1.1])
    
    # set radius limit
    ax_polar5.set_rmax(r_max)

    # subplot 6---------------------------------------------------------------------#
    # Park Transforms' symmetrical components (by applying the normal Park Transform
    # on the symmetrical components of DSOGI Clarke Transform)
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

    # set axes title
    ax_polar6.set_title('Park Components', y=1.1,
                        family='Arial', fontsize=CONST_TITLE_FONTSIZE, fontweight='bold')

    # set axes legend
    polar6_legned = ax_polar6.legend(loc='lower right', bbox_to_anchor=[1.3, -0.2])

    # set radius limit
    ax_polar6.set_rmax(r_max)

    # reduce white space of the figure (make the plots larger)
    plt.tight_layout(rect=[0.06, 0.05, 0.98, 0.995])

    # show the figure
    plt.show()

    return fig_polar
# =============================================================================
# </Function: plotting polar domain data for symmetrical components>
# =============================================================================
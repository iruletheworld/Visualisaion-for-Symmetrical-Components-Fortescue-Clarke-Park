import gsyTransforms as trf
import numpy as np
import matplotlib.pyplot as plt

from numpy import sqrt, sin, cos
    
CONST_WITH = 1280
CONST_HEIGHT = 800
CONST_DPI = 100

dbl_base_freq = 50

dbl_base_period = 1 / dbl_base_freq
    
time_end = 0.04

n = 1

phi_a = 0
phi_b = -2/3 * np.pi - 1/12 * np.pi
phi_c = 2/3 * np.pi + 1/4 * np.pi

mag_a = 1
mag_b = 1
mag_c = 1


# time vector
time = np.linspace( 0, time_end, (10 ** 5) )

# angular freq
omega = 2 * np.pi * dbl_base_freq



# base phases of the 3-phase inputs, note, base phases only
phase_a = omega * time + phi_a
phase_b = omega * time + phi_b
phase_c = omega * time + phi_c

# 3-phase inputs
input_a = mag_a * (cos(n * phase_a) + 1j * sin(n * phase_a))
input_b = mag_b * (cos(n * phase_b) + 1j * sin(n * phase_b))
input_c = mag_c * (cos(n * phase_c) + 1j * sin(n * phase_c))

# Fortescue
a_pos, b_pos, c_pos, a_neg, b_neg, c_neg, zero = trf.cal_symm(input_a, input_b, input_c)

# amplitude invariant Clarke Transform
alpha, beta, zero = trf.cal_clarke(input_a, input_b, input_c)

# DSOGI Clarke
alpha_pos_dsogi, beta_pos_dsogi, alpha_neg_dsogi, beta_neg_dsogi, _ = trf.cal_clarke_dsogi(input_a, input_b, input_c)

# normal Park Transform
d, q, _ = trf.cal_park(omega*time, alpha, beta,)

# postive Park (DSOGI)
d_pos_dsogi, q_pos_dsogi, _ = trf.cal_park(omega*time, alpha_pos_dsogi, beta_pos_dsogi)

# negative Park (DSOGI)
d_neg_dsogi, q_neg_dsogi, _ = trf.cal_park(omega*time, alpha_neg_dsogi, beta_neg_dsogi)

ylim_max = 1.1
ylim_min = -1 * ylim_max

fig_main = plt.figure(figsize=(CONST_WITH/CONST_DPI, CONST_HEIGHT/CONST_DPI), dpi=CONST_DPI)

# 3-phase inputs and symmetrical components
ax1 = plt.subplot(4, 3, 1)
ax1_a, = ax1.plot(time, input_a, label=r'Phase-A Input', color='r', lw=2)
ax1_b, = ax1.plot(time, input_b, label=r'Phase-B Input', color='g', lw=2)
ax1_c, = ax1.plot(time, input_c, label=r'Phase-C Input', color='b', lw=2)
ax1_legend = plt.legend(handles=[ax1_a, ax1_b, ax1_c], title=r'3-phase inputs', loc='upper right')

plt.ylim([ylim_min, ylim_max])

ax2 = plt.subplot(4, 3, 4)
ax2_a, = ax2.plot(time, a_pos, label=r'Phase-A +', color='r', lw=2)
ax2_b, = ax2.plot(time, b_pos, label=r'Phase-B +', color='g', lw=2)
ax2_c, = ax2.plot(time, c_pos, label=r'Phase-C +', color='b', lw=2)
ax2_legend = plt.legend(handles=[ax2_a, ax2_b, ax2_c], title=r'Positive Seq.', loc='upper right')

plt.ylim([ylim_min, ylim_max])

ax3 = plt.subplot(4, 3, 7)
ax3_a, = ax3.plot(time, a_neg, label=r'Phase-A -', color='r', lw=2)
ax3_b, = ax3.plot(time, b_neg, label=r'Phase-B -', color='g', lw=2)
ax3_c, = ax3.plot(time, c_neg, label=r'Phase-C -', color='b', lw=2)
ax3_legend = plt.legend(handles=[ax3_a, ax3_b, ax3_c], title=r'Negative Seq.', loc='upper right')

plt.ylim([ylim_min, ylim_max])

ax4 = plt.subplot(4, 3, 10)
ax4_zero, = ax4.plot(time, zero, label=r'Zero Seq', color='slateblue', lw=2)
ax4_legend = plt.legend(handles=[ax4_zero], loc='upper right')

plt.ylim([ylim_min, ylim_max])


# Clarke Transfroms
ax5 = plt.subplot(4, 3, 2)
ax5_alpha, = ax5.plot(time, alpha, label=r'$\alpha$', color='r', lw=2)
ax5_beta, = ax5.plot(time, beta, label=r'$\beta$', color='g', lw=2)
ax5_legend = plt.legend(handles=[ax5_alpha, ax5_beta], title=r'Clarke Transform', loc='upper right')

plt.ylim([ylim_min, ylim_max])

ax6 = plt.subplot(4, 3, 5)
ax6_alpha_pos, = ax6.plot(time, alpha_pos_dsogi, label=r'$\alpha_+$', color='r', lw=2)
ax6_beta_pos, = ax6.plot(time, beta_pos_dsogi, label=r'$\beta_+$', color='g', lw=2)
ax6_legend = plt.legend(handles=[ax6_alpha_pos, ax6_beta_pos], title=r'Clarke DSOGI +', loc='upper right')

plt.ylim([ylim_min, ylim_max])

ax7 = plt.subplot(4, 3, 8)
ax7_alpha_neg, = ax7.plot(time, alpha_neg_dsogi, label=r'$\alpha_-$', color='r', lw=2)
ax7_beta_neg, = ax7.plot(time, beta_neg_dsogi, label=r'$\beta_-$', color='g', lw=2)
ax7_legend = plt.legend(handles=[ax7_alpha_neg, ax7_beta_neg], title=r'Clarke DSOGI -', loc='upper right')

plt.ylim([ylim_min, ylim_max])

ax8 = plt.subplot(4, 3, 11)
ax8_zero, = ax8.plot(time, zero, label=r'Zero Seq', color='slateblue', lw=2)
ax8_legend = plt.legend(handles=[ax8_zero], loc='upper right')

plt.ylim([ylim_min, ylim_max])

# Parke Transforms
ax9 = plt.subplot(4, 3, 3)
ax9_d, = ax9.plot(time, d, label=r'$d$', color='r', lw=2)
ax9_q, = ax9.plot(time, q, label=r'$q$', color='g', lw=2)
ax9_legend = plt.legend(handles=[ax9_d, ax9_q], title=r'Park Transform', loc='upper right')

plt.ylim([ylim_min, ylim_max])

ax10 = plt.subplot(4, 3, 6)
ax10_d_pos, = ax10.plot(time, d_pos_dsogi, label=r'$d_+$', color='r', lw=2)
ax10_q_pos, = ax10.plot(time, q_pos_dsogi, label=r'$q_+$', color='g', lw=2)
ax10_legend = plt.legend(handles=[ax10_d_pos, ax10_q_pos], title=r'Park DSOGI +', loc='upper right')

plt.ylim([ylim_min, ylim_max])

ax11 = plt.subplot(4, 3, 9)
ax11_d_neg, = ax11.plot(time, d_neg_dsogi, label=r'$d_-$', color='r', lw=2)
ax11_q_neg, = ax11.plot(time, q_neg_dsogi, label=r'$q_-$', color='g', lw=2)
ax11_legend = plt.legend(handles=[ax11_d_neg, ax11_q_neg], title=r'Park DSOGI -', loc='upper right')

plt.ylim([ylim_min, ylim_max])

ax12 = plt.subplot(4, 3, 12)
ax12_zero, = ax12.plot(time, zero, label=r'Zero Seq', color='slateblue', lw=2)
ax12_legend = plt.legend(handles=[ax12_zero], loc='upper right')

plt.ylim([ylim_min, ylim_max])

plt.tight_layout()
plt.show()

fig_polar = plt.figure(figsize=(CONST_WITH/CONST_DPI, CONST_HEIGHT/CONST_DPI), dpi=CONST_DPI)

ax_polar1 = plt.subplot(231, projection='polar')
polar1_input_a = ax_polar1.plot(omega * time, abs(input_a), label=r'Phase-A Input', color='r', lw=2)
polar1_input_b = ax_polar1.plot(omega * time, abs(input_b), label=r'Phase-B Input', color='g', lw=2)
polar1_input_c = ax_polar1.plot(omega * time, abs(input_c), label=r'Phase-C Input', color='b', lw=2)
polar1_legned = ax_polar1.legend(loc='upper left', bbox_to_anchor=(-0.55, 1))
ax_polar1.set_rmax(1.2)

ax_polar2 = plt.subplot(234, projection='polar')
polar2_input_a_pos = ax_polar2.plot(omega * time, abs(a_pos), label=r'Phase-A +', color='r', lw=5)
polar2_input_b_pos = ax_polar2.plot(omega * time, abs(b_pos), label=r'Phase-B +', color='g', lw=3)
polar2_input_c_pos = ax_polar2.plot(omega * time, abs(c_pos), label=r'Phase-C +', color='b', lw=1)

polar2_input_a_neg = ax_polar2.plot(omega * time, abs(a_neg), label=r'Phase-A -', color='pink', lw=5)
polar2_input_b_neg = ax_polar2.plot(omega * time, abs(b_neg), label=r'Phase-B -', color='limegreen', lw=3)
polar2_input_c_neg = ax_polar2.plot(omega * time, abs(c_neg), label=r'Phase-C -', color='skyblue', lw=1)

polar2_zero = ax_polar2.plot(omega * time, abs(zero), label=r'Zero', color='k', lw=1)
polar2_legned = ax_polar2.legend(loc='lower left', bbox_to_anchor=(-0.55, -0.2))
ax_polar2.set_rmax(1.2)

ax_polar3 = plt.subplot(232, projection='polar')
polar3_alpha = ax_polar3.plot(omega * time, abs(alpha), label=r'$\alpha$', color='r', lw=2)
polar3_beta = ax_polar3.plot(omega * time, abs(beta), label=r'$\beta$', color='g', lw=2)
polar3_legned = ax_polar3.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
ax_polar3.set_rmax(1.2)

ax_polar4 = plt.subplot(235, projection='polar')
polar4_alpha_pos = ax_polar4.plot(omega * time, abs(alpha_pos_dsogi), label=r'$\alpha_+$', color='r', lw=2)
polar4_beta_pos = ax_polar4.plot(omega * time, abs(beta_pos_dsogi), label=r'$\beta_+$', color='g', lw=2)

polar4_alpha_neg = ax_polar4.plot(omega * time, abs(alpha_neg_dsogi), label=r'$\alpha_-$', color='pink', lw=2)
polar4_beta_neg = ax_polar4.plot(omega * time, abs(beta_neg_dsogi), label=r'$\beta_-$', color='limegreen', lw=2)

polar4_zero = ax_polar4.plot(omega * time, abs(zero), label=r'Zero', color='k', lw=1)

polar4_legned = ax_polar4.legend(loc='lower right', bbox_to_anchor=(1.3, -0.2))
ax_polar4.set_rmax(1.2)

ax_polar5 = plt.subplot(233, projection='polar')
polar5_d = ax_polar5.plot(omega * time, abs(d), label=r'$d$', color='r', lw=2)
polar5_q = ax_polar5.plot(omega * time, abs(q), label=r'$q$', color='g', lw=2)
polar5_legned = ax_polar5.legend(loc='upper right', bbox_to_anchor=(1.4, 1))
ax_polar5.set_rmax(1.2)

ax_polar6 = plt.subplot(236, projection='polar')
polar6_d_pos = ax_polar6.plot(omega * time, abs(d_pos_dsogi), label=r'$d_+$', color='r', lw=2)
polar6_q_pos = ax_polar6.plot(omega * time, abs(q_pos_dsogi), label=r'$q_+$', color='g', lw=2)

polar6_d_neg = ax_polar6.plot(omega * time, abs(d_neg_dsogi), label=r'$d_-$', color='pink', lw=2)
polar6_q_neg = ax_polar6.plot(omega * time, abs(q_neg_dsogi), label=r'$q_-$', color='limegreen', lw=2)

polar6_zero = ax_polar6.plot(omega * time, abs(zero), label=r'Zero', color='k', lw=1)

polar6_legned = ax_polar6.legend(loc='lower right', bbox_to_anchor=(1.4, -0.2))
ax_polar6.set_rmax(1.2)

#plt.tight_layout()
plt.show()






# =============================================================================
# plt.subplot(3, 1, 1)
# plt.plot(time, input_a, time, input_b, time, input_c)
# 
# plt.subplot(3, 1, 2)
# plt.plot(time, alpha, time, beta, time, zero)
# 
# plt.subplot(3, 1, 3)
# plt.plot(time, d_ddsrf_pos, time, q_ddsrf_pos, time, d_ddsrf_neg, time, q_ddsrf_neg)
# =============================================================================



# =============================================================================
# def draw_clarke(dbl_har_order, dbl_base_freq=50, dbl_cycle=4, 
#                 mag_a=1, mag_b=1, mag_c=1,
#                 bool_savefig=False, int_dpi=600, str_fig_path=''):
#     
#     # import modules
#     import matplotlib as mpl
#     import matplotlib.pyplot as plt
#     import numpy as np
#     import os
#     
#     from numpy import pi, cos
#     from gsyDqLib import date_time_now
#     
#     # matplotlib setup
#     mpl.rcParams['font.family'] = 'serif'
#     mpl.rcParams['text.usetex'] = True
#     mpl.rcParams['text.latex.preview'] = True
#     mpl.rcParams['text.latex.preamble'] = [r'\boldmath']
#     mpl.rcParams['font.weight'] = 'bold'
#     
# 
#     # =============================================================================
#     # <Process input arguments>    
#     # =============================================================================
#     # process input harmonic order
#     try:
#         
#         dbl_har_order = float(dbl_har_order)    
#         
#         if dbl_har_order != 0:
#             
#             dbl_har_order = abs(dbl_har_order)
#             
#         else:
#             
#             dbl_har_order = 1
#             
#             print(date_time_now() + ' Invalid harmoinc order. Harmonic order set to 1')
#             
#     except:
#         
#         dbl_har_order = 1
#         
#         print(date_time_now() + ' Invalid harmoinc order. Harmonic order set to 1')
#         
#         pass
#     
#     # process base frequency
#     try:
#         
#         dbl_base_freq = float(dbl_base_freq)
#         
#         if dbl_base_freq != 0:
#             
#             dbl_base_freq = abs(dbl_base_freq)
#             
#         else:
#             
#             dbl_base_freq = 50.0
#             
#             print(date_time_now() + ' Invalid base frequency. Base frequency set to 50')        
#     
#     except:
#         
#         dbl_base_freq = 50.0
#             
#         print(date_time_now() + ' Invalid base frequency. Base frequency set to 50') 
#         
#         pass
#     
#     # process how many cycles to display
#     try:
#         
#         dbl_cycle = float(dbl_cycle)
#         
#         if dbl_cycle != 0:
#             
#             dbl_cycle = abs(dbl_cycle)
#             
#         else:
#             
#             dbl_cycle = 4
#             
#             print(date_time_now() + ' Invalid display cycles. Set display cycles to 4')        
#         
#     except:
#         
#         dbl_cycle = 4
#             
#         print(date_time_now() + ' Invalid display cycles. Set display cycles to 4')        
#         
#         pass
#     
#     # process whether to save the figure
#     try:
#         
#         bool_savefig = bool(bool_savefig)
#         
#     except:
#         
#         bool_savefig = False
#             
#         pass
#     
#     # process dpi
#     try:
#         
#         int_dpi = int(int_dpi)
#         
#         if int_dpi != 0:
#             
#             int_dpi = int_dpi
#             
#         else:
#             
#             int_dpi = 600
#             
#             print(date_time_now() + ' Invalid dpi. Set dpi to 600') 
#         
#     except:
#         
#         int_dpi = 600
#             
#         print(date_time_now() + ' Invalid dpi. Set dpi to 600') 
#         
#         pass
#     
#     # process figure path
#     try:
#     
#         str_fig_path = str(str_fig_path)
#         
#         if bool_savefig == True:
#             
#             if len(str_fig_path) == 0:
#                 
#                 str_fig_path = 'Figure_' + str( int(np.random.rand() * 1e6) ) + '.png'
#                 
#                 str_fig_path = os.path.join(os.getcwd(), str_fig_path)
#                 
#             else:
#                 
#                 pass
#                 
#         else:
#             
#             pass
#         
#     except:
#         
#         str_fig_path = 'Figure_' + str( int(np.random.rand() * 1e6) ) + '.png'
#                 
#         str_fig_path = os.path.join(os.getcwd(), str_fig_path)
#         
#         print(date_time_now() + ' Invalid figure path. Set figure path to "' + str_fig_path + '"') 
#         
#         pass
#     # =============================================================================
#     # </Process input arguments>
#     # =============================================================================
#     
#     
#     # =============================================================================
#     # <Make data, titles, legends>    
#     # =============================================================================
#     int_remainder = np.mod(dbl_har_order, 3)
#     
#     dbl_base_period = 1 / dbl_base_freq
#         
#     time_end = dbl_base_period / dbl_har_order * dbl_cycle
#     
#     # time vector
#     time = np.linspace( 0, time_end, (10 ** 5) )
#     
#     # angular freq
#     omega = 2 * np.pi * dbl_base_freq
#     
#     # base phases of the 3-phase inputs, note, base phases only
#     phase_a = omega * time
#     phase_b = omega * time - (2 / 3 * pi)
#     phase_c = omega * time + (2 / 3 * pi)
#     
#     # 3-phase inputs
#     input_a = mag_a * cos(dbl_har_order * phase_a)
#     input_b = mag_b * cos(dbl_har_order * phase_b)
#     input_c = mag_c * cos(dbl_har_order * phase_c)
#     
#     # amplitude invariant Clarke transform
#     alpha, beta, zero = cal_clarke(input_a, input_b, input_c)
#     
#     # legend labels for the 3-phase inputs
#     str_a_lbl = r'$a = cos(' + str(dbl_har_order) + r'\cdot \omega t)$'
#     str_b_lbl = r'$b = cos[' + str(dbl_har_order) + r'\cdot (\omega t - \frac{2}{3}\pi)]$'
#     str_c_lbl = r'$c = cos[' + str(dbl_har_order) + r'\cdot (\omega t + \frac{2}{3}\pi)]$'
#     
#     # legend labels for the Clarke transform
#     str_alpha_lbl = r'$\alpha = \frac{2}{3} (a - \frac{1}{2} b - \frac{1}{2} c)$'                 
#     
#     str_beta_lbl = r'$\beta = \frac{2}{3} ( 0 + \frac{\sqrt{3}}{2} b - \frac{\sqrt{3}}{2} c)$' 
#                         
#     str_zero_lbl = r'$Zero = \frac{2}{3} (\frac{1}{2} a + \frac{1}{2} b + \frac{1}{2} c)$' 
#     
#     # condition, coordinate 1 title
#     if all( x == mag_a for x in (mag_a, mag_b, mag_c) ):
#      
#         if int_remainder == 1:
#         
#             str_ax1_title = ( r'$\textbf{Three-Phase Inputs, } \omega =2 \pi \times' 
#                              + str(dbl_har_order) + r'\times' + str(dbl_base_freq) 
#                              + r'\textbf{ (positive sequence)}$' )
#             
#         elif int_remainder == 2:
#             
#             str_ax1_title = ( r'$\textbf{Three-Phase Inputs, } \omega =2 \pi \times' 
#                              + str(dbl_har_order) + r'\times' + str(dbl_base_freq) 
#                              + r'\textbf{ (negative sequence)}$' )
#             
#         elif int_remainder == 0:
#             
#             str_ax1_title = ( r'$\textbf{Three-Phase Inputs, } \omega =2 \pi \times' 
#                              + str(dbl_har_order) + r'\times' + str(dbl_base_freq) 
#                              + r'\textbf{ (zero sequence)}$' )
#             
#         else:
#                 
#             str_ax1_title = ( r'$\textbf{Three-Phase Inputs, } \omega =2 \pi \times' 
#                              + str(dbl_har_order) + r'\times' + str(dbl_base_freq) 
#                              + r'$' )    
#             
#     else:
#         
#         str_ax1_title = ( r'$\textbf{Three-Phase Inputs, } \omega =2 \pi \times' 
#                              + str(dbl_har_order) + r'\times' + str(dbl_base_freq) 
#                              + r'$' )  
#         
#     # coordinate 2 title
#     str_ax2_title = r'$\textbf{Outputs of the General Amplitude Invariant Clarke Transform}$'        
#     # =============================================================================
#     # </Make data, titles, legends>    
#     # =============================================================================
#     
#     
#     # =============================================================================
#     # <Main figure setup>
#     # =============================================================================
#     # make main figure
#     fig = plt.figure(figsize=(900.0/100.0, 600.0/100.0), dpi = 100.0)
#     
#     # adjust spacing between subplots
#     fig.subplots_adjust(hspace=0.5)
#     
#     # <coordnate 1> =============================================================================
#     # make coordinate 1
#     ax1 = plt.subplot(2, 1, 1)
#     
#     # set coordinate 1 title
#     ax1.set_title(str_ax1_title, fontsize=14, fontweight='bold', y=1.2)
#     
#     # set coordinate 1 horizontal line
#     ax1.axhline(y=0, color='k', lw=3)
#     
#     # plot 3-phase inputs
#     ax1_input_a, = plt.plot(time, input_a, color='r', lw=2, label=str_a_lbl)
#     ax1_input_b, = plt.plot(time, input_b, color='g', lw=2, label=str_b_lbl)
#     ax1_input_c, = plt.plot(time, input_c, color='b', lw=2, label=str_c_lbl)
#     
#     # get automatic y limits
#     y_min, y_max = ax1.get_ylim()
#     
#     # set limits and grid lines
#     plt.xlim([0, time_end])
#     plt.ylim([y_min, y_max])
#     plt.grid(True)
#     
#     # range arguments for ploting period helping lines
#     rng_start = dbl_base_period / dbl_har_order
#     rng_stop = time_end + rng_start
#     rng_step = rng_start
#     
#     # plot period helping lines
#     for item in np.arange(rng_start, rng_stop, rng_step):
#         
#         plt.plot([item, item], [y_min, y_max], 
#                  linestyle='--', linewidth=2, color='k')
#     
#     # set legend
#     ax1_lgd = plt.legend(handles=[ax1_input_a, ax1_input_b, ax1_input_c], 
#                          loc='upper center', fontsize=11, bbox_to_anchor=(0.5, 1.25), 
#                          shadow=False, fancybox=True, ncol=3)
#     
#     # set legend transparence
#     ax1_lgd.get_frame().set_alpha(1.0)
#     
#     # set y label
#     ax1.set_ylabel(r'\textbf{Amplitude}', fontweight='bold', fontsize=12)    
#     # </coordnate 1> =============================================================================
#     
#     # <coordnate 2> =============================================================================
#     # make coordinate 2
#     ax2 = plt.subplot(2, 1, 2)
#     
#     # set coordinate 2 title
#     ax2.set_title(str_ax2_title, fontsize=14, fontweight='bold', y=1.23)
#     
#     # plot coordinate 2 horizontal line
#     ax2.axhline(y=0, color='k', lw=3)
#     
#     # plot Clarke transform components
#     ax2_alpha, = plt.plot(time, alpha, color='r', lw=2, label=str_alpha_lbl)
#     ax2_beta, = plt.plot(time, beta, color='g', lw=2, label=str_beta_lbl)
#     ax2_zero, = plt.plot(time, zero, color='b', lw=2, label=str_zero_lbl)
#     
#     # get automatic y limits
# #    y_min, y_max = ax2.get_ylim()
#     
#     # set coordinate 2 limits
#     plt.xlim([0, time_end])
#     plt.ylim([y_min, y_max])
#     plt.grid(True)
#     
#     # plot period helping lines
#     for item in np.arange(rng_start, rng_stop, rng_step):
#         
#         plt.plot([item, item], [y_min, y_max], linestyle='--', linewidth=2, color='k')
#     
#     # set coordinate 2 legend
#     ax2_lgd = plt.legend(handles=[ax2_alpha, ax2_beta, ax2_zero], loc='upper center', 
#                          fontsize=11, bbox_to_anchor=(0.5, 1.27), 
#                          shadow=False, fancybox=True, ncol=3)
#     
#     # set legend transparence
#     ax2_lgd.get_frame().set_alpha(1.0)
#     
#     # set labels
#     ax2.set_xlabel(r'\textbf{Time (s)}', fontweight='bold', fontsize=12)
#     ax2.set_ylabel(r'\textbf{Amplitude}', fontweight='bold', fontsize=12)
#     # </coordnate 2> =============================================================================
#     
#     plt.show()
#     # =============================================================================
#     # </Main figure setup>
#     # =============================================================================
#     
#     
#     # =============================================================================
#     # <Condition, save figure>    
#     # =============================================================================
#     if bool_savefig == True:
#         
#         plt.tight_layout()
#         
#         fig.savefig(str_fig_path, dpi=int_dpi)
#         
#         plt.tight_layout()
#         
#         print( date_time_now() + 'Figure saved as:"' + str_fig_path + '"' ) 
#         
#         plt.close()
#         
#         
#     else:
#                 
#         pass    
#     # =============================================================================
#     # </Condition, save figure>    
#     # =============================================================================
#         
# draw_clarke(1, mag_a=0.7, mag_b=1.2, mag_c=0.6)
# =============================================================================
    
# =============================================================================
# 
# import numpy as np
# import os
# 
# for item in (1.7, 2.4, 5.6):
#     
#     path = r'J:\_Clarke & Park\Figures\Clarke_unbalanced'
#     
#     path = os.path.join(path, str(item) + '.png')
#     
#     draw_clarke(item, bool_savefig=True, str_fig_path=path)
# =============================================================================
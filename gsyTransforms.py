# -*- coding: utf-8 -*-
"""
Calculations for the following transforms:
Fortescue (3-phase symmetrical components), Clarke (DSOGI), Park (normal & DDSRF).abs

Module Name : gsyTransforms

Author : Dr. GAO, Siyu

Version : 0.1.2

Last Modified : 2017-12-12

Change Log
----------------------
* **Notable changes:**

    + Version : 0.1.2
        - Added "cal_clarke"
        - Added "cal_clarke_dsogi"
        - Added "cal_park"
        - Added "cal_park_ddsrf"
        - Added "cal_symm"
        - Added "to_complex"



List of functions
----------------------
* cal_clarke_
* cal_clarke_dsogi_
* cal_park_
* cal_park_ddsrf_
* cal_symm_
* to_complex_

Function definitions
----------------------
"""

import numpy as np

from numpy import sqrt, sin, cos

# =============================================================================
# <Function: calculate the symmetrical components (Fortescue)>
# =============================================================================
def cal_symm(a, b, c):

    """
    .. _cal_symm :

    Calculates the 3-phase symmetrical components (Fortescue). 

    Accepts complex forms of three-phase inputs. Returns the Positive sequence,
    the Negative sequence and the Zero sequence.

    .. math ::

        A = e^{j \\frac{2}{3} \pi} = \\angle 120^{\circ}
    
    Commonly, the lowercase of :math:`A`, :math:`\\alpha`, is used. 
    To avoid confusion with :math:`a` (/eɪ/), the uppercase, :math:`A`, is used here instead.

    .. math ::

        \left[\\begin{matrix} 
        a_{+} \\\\ b_{+} \\\\ c_{+}
        \end{matrix}\\right] 
        &= \\frac{1}{3} 
        \left[\\begin{matrix} 
        1 & A & A^2 
        \\\\ A^2 & 1 & A
        \\\\ A & A^2 & 1 
        \end{matrix}\\right] 
        \left[\\begin{matrix} 
        a \\\\ b \\\\ c 
        \end{matrix}\\right]

        \\\\

        \left[\\begin{matrix} 
        a_{-} \\\\ b_{-} \\\\ c_{-}
        \end{matrix}\\right] 
        &= \\frac{1}{3} 
        \left[\\begin{matrix} 
        1 & A^2 & A
        \\\\ A & 1 & A^2
        \\\\ A^2 & A & 1 
        \end{matrix}\\right] 
        \left[\\begin{matrix} 
        a \\\\ b \\\\ c 
        \end{matrix}\\right]        
        
        \\\\

        \left[\\begin{matrix} 
        a_{Zero} \\\\ b_{Zero} \\\\ c_{Zero}
        \end{matrix}\\right] 
        = \\frac{1}{3} 
        \left[\\begin{matrix} 
        1 & 1 & 1
        \\\\ 1 & 1 & 1
        \\\\ 1 & 1 & 1 
        \end{matrix}\\right] 
        \left[\\begin{matrix} 
        a \\\\ b \\\\ c 
        \end{matrix}\\right]

    Parameters
    ----------
    a : complex or a list of complex
        Phase-A inputs

    b : complex or a list of complex
        Phase-B inputs

    c : complex or a list of complex
        Phase-C inputs

    Returns
    -------
    a_pos : complex
        Phase-A Positive sequence.

    b_pos : complex
        Phase-B Positive sequence.

    c_pos : complex
        Phase-C Positive sequence.

    a_neg : complex
        Phase-A Negative sequence.

    b_neg : complex
        Phase-B Negative sequence.

    c_neg : complex
        Phase-C Negative sequence.

    Zero : complex
        Ther Zero sequence.
    
    
    Examples
    --------
    
    .. code :: python

        import gsyTransforms as trf

        (phaseA_pos, phaseB_pos,
         phaseC_pos, phaseA_neg, 
         phaseB_neg, phaseC_neg, 
         phaseZero)              = trf.cal_symm(phaseAdata,
                                                phaseBdata,
                                                phaseCdata)


    """

    # 120 degree rotator
    ALPHA = np.exp(1j * 2/3 * np.pi)
        
    # Positive sequence
    a_pos = 1/3 * ( a + b * ALPHA + c * (ALPHA ** 2) )
    
    b_pos = 1/3 * ( a * (ALPHA ** 2) + b + c * ALPHA )
    
    c_pos = 1/3 * ( a * ALPHA + b * (ALPHA ** 2) + c )
    
    # Negative sequence
    a_neg = 1/3 * ( a + b * (ALPHA ** 2) + c * ALPHA )
    
    b_neg = 1/3 * ( a * ALPHA + b + c * (ALPHA ** 2) )
    
    c_neg = 1/3 * ( a * (ALPHA ** 2) + b * ALPHA + c )
    
    # zero sequence
    zero = 1/3 * (a + b + c)
    
    return a_pos, b_pos, c_pos, a_neg, b_neg, c_neg, zero
# =============================================================================
# </Function: calculate the symmetrical components (Fortescue)>
# =============================================================================


# =============================================================================
# <Function: calculate the amplitude invariant Clarke Transform>
# =============================================================================
def cal_clarke(a, b, c):

    """
    .. _cal_clarke :

    Calculates the amplitude invariant Clarke Transform. 

    Accepts complex forms of three-phase inputs. Returns the :math:`\\alpha` component,
    :math:`\\beta` component and the :math:`Zero` component.

    .. math ::

        \left[\\begin{matrix} \\alpha \\\\ \\beta \\\\ Zero \end{matrix}\\right] 
        = \\frac{2}{3} 
        \left[\\begin{matrix} 
        1 & -\\frac{1}{2} & -\\frac{1}{2} 
        \\\\ 0 & \\frac{\sqrt{3}}{2} & -\\frac{\sqrt{3}}{2} 
        \\\\ \\frac{1}{2} & \\frac{1}{2} & \\frac{1}{2} 
        \end{matrix}\\right] 
        \left[\\begin{matrix} 
        a \\\\ b \\\\ c 
        \end{matrix}\\right] 
    
    Parameters
    ----------
    a : complex or a list of complex
        Phase-A inputs

    b : complex or a list of complex
        Phase-B inputs

    c : complex or a list of complex
        Phase-C inputs

    Returns
    -------
    alpha : complex
        The alpha component.

    beta : complex
        The beta component.

    zero : complex
        The Zero sequence.
    
    Examples
    --------
    
    .. code :: python

        import gsyTransforms as trf

        alpha, beta, zero = trf.cal_clarke(phaseAdata,
                                           phaseBdata,
                                           phaseCdata)

    """
    
    alpha = 2/3 * ( a - 1/2 * (b + c) )
    
    beta = 2/3 * ( sqrt(3)/2 * (b - c) )
    
    zero = 1/3 * (a + b + c)
    
    return alpha, beta, zero
# =============================================================================
# </Function: calculate the amplitude invariant Clarke Transform>
# =============================================================================


# =============================================================================
# <Function: calculate the DSOGI symmetrical components for the amplitude invariant Clarke Transform>
# =============================================================================
def cal_clarke_dsogi(a, b, c):

    """
    .. _cal_clarke_dsogi :

    Calculates the Positive sequence and Negative sequence of the Clarke Transform based
    on the method of the Double Second-Order Generalised Integrator. 

    Accepts complex forms of three-phase inputs. Returns the :math:`\\alpha_+`,
    :math:`\\beta_+`, :math:`\\alpha_-`, :math:`\\beta_-` and the :math:`Zero` component.

    .. math ::

        quad = e^{-j \\frac{1}{2} \pi} = \\angle -90^{\circ}
        
        \\\\

        \left[\\begin{matrix}\\alpha_+ \\\\ \\beta_+ \end{matrix}\\right]
        = \\frac{1}{2} 
        \left[
        \\begin{matrix} 
        1 & -quad 
        \\\\ 
        quad & 1
        \end{matrix}
        \\right] 
        \left[
        \\begin{matrix} 
        \\alpha 
        \\\\
        \\beta
        \end{matrix}
        \\right]

        \\\\

        \left[\\begin{matrix} \\alpha_- \\\\ \\beta_- \end{matrix}\\right]
        = \\frac{1}{2} 
        \left[
        \\begin{matrix} 
        1 & quad 
        \\\\ 
        -quad & 1
        \end{matrix}
        \\right] 
        \left[
        \\begin{matrix} 
        \\alpha \\\\ \\beta
        \end{matrix}
        \\right]

    Parameters
    ----------
    a : complex or a list of complex
        Phase-A inputs

    b : complex or a list of complex
        Phase-B inputs

    c : complex or a list of complex
        Phase-C inputs

    Returns
    -------
    alpha : complex
        The alpha component.

    beta : complex
        The beta component.

    zero : complex
        The Zero sequence.
    
    Examples
    --------
    
    .. code :: python

        import gsyTransforms as trf

        alpha, beta, zero = trf.cal_clarke(phaseAdata,
                                           phaseBdata,
                                           phaseCdata)

    """
    
    # based on the DSOGI     
    QUAD = np.exp(-1j * np.pi/2)
    
    # calculate the Clarke components
    alpha, beta, zero = cal_clarke(a, b, c)
    
    # Positive alpha and beta
    alpha_pos_dsogi = 1/2 * ( alpha - beta * QUAD )
    
    beta_pos_dsogi = 1/2 * ( alpha * QUAD + beta )
    
    # Negative alpha and beta
    alpha_neg_dsogi = 1/2 * ( alpha + beta * QUAD )
    
    beta_neg_dsogi = 1/2 * ( -1 * alpha * QUAD + beta )

    # Zero sequence
    zero = 1/3 * ( a + b + c )

    return alpha_pos_dsogi, beta_pos_dsogi, alpha_neg_dsogi, beta_neg_dsogi, zero
# =============================================================================
# </Function: calculate the DSOGI symmetrical components for the amplitude invariant Clarke Transform>
# =============================================================================


# =============================================================================
# <Function: calculate the Park Transform (normal)>
# =============================================================================
def cal_park(theta, alpha, beta, zero=0):
    
    # Park transform (normal)
    
    length_theta = len(theta)
    
    length_alpha = len(alpha)
    
    length_beta = len(beta)
    
    if all( x == length_theta for x in (length_theta, length_alpha, length_beta) ):
        
        pass
    
    else:
        
        raise ValueError('Element length mismatch.'
                         + 'The length of theta, alpha and beta must be all the same')
    
    d = cos(theta) * alpha + sin(theta) * beta
    
    q = -1 * sin(theta) * alpha + cos(theta) * beta
    
    zero = zero
    
    return d, q, zero
# =============================================================================
# </Function: calculate the Park Transform (normal)>
# =============================================================================


# =============================================================================
# <Function: calculate the Park Transform (DDSRF)>
# =============================================================================
def cal_park_ddsrf(theta, alpha, beta, zero=0):

    # Park transform (DDSRF)
    
    length_theta = len(theta)
    
    length_alpha = len(alpha)
    
    length_beta = len(beta)
    
    if all( x == length_theta for x in (length_theta, length_alpha, length_beta) ):
        
        pass
    
    else:
        
        raise ValueError('Element length mismatch.'
                         + 'The length of theta, alpha and beta must be all the same')

    d_ddsrf_pos = cos(theta) * alpha + sin(theta) * beta

    q_ddsrf_pos = -1 * sin(theta) * alpha + cos(theta) * beta

    d_ddsrf_neg = cos(theta) * alpha + (-sin(theta)) * beta

    q_ddsrf_neg = sin(theta) * alpha + cos(theta) * beta

    zero = zero

    return d_ddsrf_pos, q_ddsrf_pos, d_ddsrf_neg, q_ddsrf_neg, zero
# =============================================================================
# </Function: calculate the Park Transform (DDSRF)>
# =============================================================================


# =============================================================================
# <Function: convert to complex number>
# =============================================================================
def to_complex(r, x, real_offset=0, imag_offset=0):
    
    real = r * cos(x) + real_offset
    
    imag = r * sin(x) + imag_offset
    
    return (real + 1j * imag)
# =============================================================================
# </Function: convert to complex number>
# =============================================================================
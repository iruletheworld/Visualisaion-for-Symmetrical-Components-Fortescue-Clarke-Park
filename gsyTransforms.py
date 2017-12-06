# -*- coding: utf-8 -*-
"""
Calculations for the following transforms:
Fortescue (3-phase symmetrical components), Clarke (DSOGI), Park (normal & DDSRF)

Author : Dr. GAO, Siyu

Version : 0.1.0

Last Modified : 2017-11-30
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

    Accepts complex forms of three-phase inputs. Returns the positive sequence,
    the negative sequence and the zero sequence.

    .. math ::

        A = e^{j \\frac{2}{3} \pi} = \\angle 120^{\circ}
    
    Commonly, the lowercase of :math:`A`, :math:`\\alpha`, is used to avoid confusion with :math:`a` (/eɪ/).

    .. math ::

        \left[\\begin{matrix} 
        a_{+} \\\\ b_{+} \\\\ c_{+}
        \end{matrix}\\right] 
        = \\frac{1}{3} 
        \left[\\begin{matrix} 
        1 & A & A^2 
        \\\\ A^2 & 1 & A
        \\\\ A & A^2 & 1 
        \end{matrix}\\right] 
        \left[\\begin{matrix} 
        a \\\\ b \\\\ c 
        \end{matrix}\\right]

        \left[\\begin{matrix} 
        a_{-} \\\\ b_{-} \\\\ c_{-}
        \end{matrix}\\right] 
        = \\frac{1}{3} 
        \left[\\begin{matrix} 
        1 & A^2 & A
        \\\\ A & 1 & A^2
        \\\\ A^2 & A & 1 
        \end{matrix}\\right] 
        \left[\\begin{matrix} 
        a \\\\ b \\\\ c 
        \end{matrix}\\right]
         
    .. math ::

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
        

    Returns
    -------
    
    
    Examples
    --------
    
    .. code :: python


    """

    # 120 degree rotator
    ALPHA = np.exp(1j * 2/3 * np.pi)
        
    # positive sequence
    a_pos = 1/3 * ( a + b * ALPHA + c * (ALPHA ** 2) )
    
    b_pos = 1/3 * ( a * (ALPHA ** 2) + b + c * ALPHA )
    
    c_pos = 1/3 * ( a * ALPHA + b * (ALPHA ** 2) + c )
    
    # negative sequence
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
        

    Returns
    -------
    
    
    Examples
    --------
    
    .. code :: python


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
    
    # based on the DSOGI 
    
    QUAD = np.exp(-1j * np.pi/2)
    
    # calculate the Clarke components
    alpha, beta, zero = cal_clarke(a, b, c)
    
    # positive alpha and beta
    alpha_pos_dsogi = 1/2 * ( alpha - beta * QUAD )
    
    beta_pos_dsogi = 1/2 * ( alpha * QUAD + beta )
    
    # negative alpha and beta
    alpha_neg_dsogi = 1/2 * ( alpha + beta * QUAD )
    
    beta_neg_dsogi = 1/2 * ( -1 * alpha * QUAD + beta )

    # zero sequence
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
    
def to_complex(r, x, offset=0):
    
    real = r * cos(x) + offset
    
    imag = r * sin(x)
    
    return (real + 1j * imag)
    
    
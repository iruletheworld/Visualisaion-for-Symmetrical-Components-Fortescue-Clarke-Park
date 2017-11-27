# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 09:50:56 2017

@author: 212612902
"""

import numpy as np

from numpy import sqrt, sin, cos

# =============================================================================
# <Function: calculate the symmetrical components (Fortescue)>
# =============================================================================
def cal_symm(a, b, c):
    
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
    
    alpha = 2/3 * ( a - 1/2 * (b + c) )
    
    beta = 2/3 * ( sqrt(3)/2 * (b - c) )
    
    zero = 2/3 * 1/2 * (a + b + c)
    
    return alpha, beta, zero
# =============================================================================
# </Function: calculate the amplitude invariant Clarke Transform>
# =============================================================================


# =============================================================================
# <Function: calculate the symmetrical components for the amplitude invariant Clarke Transform>
# =============================================================================
def cal_clarke_symm(a, b, c):
    
    # based on the DSOGI 
    
    QUAD = np.exp(-1j * np.pi/2)
    
    # calculate the Clarke components
    alpha, beta, zero = cal_clarke(a, b, c)
    
    # positive alpha and beta
    alpha_pos = 1/2 * ( alpha - beta * QUAD )
    
    beta_pos = 1/2 * ( alpha * QUAD + beta )
    
    # negative alpha and beta
    alpha_neg = 1/2 * ( alpha + beta * QUAD )
    
    beta_neg = 1/2 ( -1 * alpha * QUAD + beta )
    
    return alpha_pos, beta_pos, alpha_neg, beta_neg, zero
# =============================================================================
# </Function: calculate the symmetrical components for the amplitude invariant Clarke Transform>
# =============================================================================    


# =============================================================================
# <Function: calculate the Park Transform>
# =============================================================================
def cal_park(theta, alpha, beta, zero):
    
    # Park transform
    
    length_theta = len(theta)
    
    length_alpha = len(alpha)
    
    length_beta = len(beta)
    
    length_zero = len(zero)
    
    if all( x == length_theta for x in (length_theta, length_alpha, length_beta, length_zero) ):
        
        pass
    
    else:
        
        raise ValueError('Element length mismatch.'
                         + 'The length of theta, alpha, beta and zero must be all the same')    
    
    d = cos(theta) * alpha + sin(theta) * beta
    
    q = -sin(theta) * alpha + cos(theta) * beta
    
    zero = zero
    
    return d, q, zero
# =============================================================================
# </Function: calculate the Park Transform>
# =============================================================================
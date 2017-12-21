# -*- coding: utf-8 -*-
"""
Calculations for the following transforms:
Fortescue (3-phase symmetrical components), Clarke (normal and DSOGI), Park (normal and DSRF).

Module Name : gsyTransforms

Author : Dr. GAO, Siyu

Version : 0.1.2

Last Modified : 2017-12-14

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
* cal_park_dsrf_
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

    Accepts complex form of three-phase inputs. Returns the Positive sequence,
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

    ===================== ============================================================
    where:
    ===================== ============================================================
    :math:`A`               is the :math:`120^{\circ}` shifter;
    :math:`a`               is the Phase-A input;
    :math:`b`               is the Phase-B input;
    :math:`c`               is the Phase-C input;
    :math:`a_+`             is the positive sequence of Phase-A input;
    :math:`b_+`             is the positive sequence of Phase-B input;
    :math:`c_+`             is the positive sequence of Phase-C input;
    :math:`a_-`             is the negative sequence of Phase-A input;
    :math:`b_-`             is the negative sequence of Phase-B input;
    :math:`c_-`             is the negative sequence of Phase-C input;
    :math:`a_{Zero}`        is the zero sequence of Phase-A input;
    :math:`b_{Zero}`        is the zero sequence of Phase-B input;
    :math:`c_{Zero}`        is the zero sequence of Phase-C input.
    ===================== ============================================================

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
    a_pos : complex or a list of complex
        Phase-A Positive sequence.

    b_pos : complex or a list of complex
        Phase-B Positive sequence.

    c_pos : complex or a list of complex
        Phase-C Positive sequence.

    a_neg : complex or a list of complex
        Phase-A Negative sequence.

    b_neg : complex or a list of complex
        Phase-B Negative sequence.

    c_neg : complex or a list of complex
        Phase-C Negative sequence.

    Zero : complex or a list of complex
        Ther Zero sequence. Since all zero sequence components are
        the same, only one is returned.
    
    
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

    Accepts complex form of three-phase inputs. Returns the :math:`\\alpha` component,
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

    ===================== ============================================================
    where:
    ===================== ============================================================
    :math:`a`               is the Phase-A input;
    :math:`b`               is the Phase-B input;
    :math:`c`               is the Phase-C input;
    :math:`\\alpha`         is the :math:`\\alpha` component of the Clarke Transform;
    :math:`\\beta`          is the :math:`\\beta` component of the Clarke Transform;
    :math:`Zero`            is the :math:`Zero` sequnece component.
    ===================== ============================================================
    
    Parameters
    ----------
    a : complex or a list of complex
        Phase-A input

    b : complex or a list of complex
        Phase-B input

    c : complex or a list of complex
        Phase-C input

    Returns
    -------
    alpha : complex or a list of complex
        The :math:`\\alpha` component.

    beta : complex or a list of complex
        The :math:`\\beta` component.

    zero : complex or a list of complex
        The :math:`Zero` sequence.
    
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
    on the method of the Double Second-Order Generalised Integrator (DSOGI). 

    Accepts complex form of three-phase inputs. Returns the :math:`\\alpha_+`,
    :math:`\\beta_+`, :math:`\\alpha_-`, :math:`\\beta_-` and the :math:`Zero` component.

    The Zero sequence is calculated by using the Clarke Transform.

    For more information of the DSOGI [#]_:

    .. [#] Teodorescu, R., Liserre, M., and Rodríguez, P., *Grid Converters for Photovoltaic 
        and Wind Power Systems*. 2011: John Wiley & Sons, Ltd. 

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

    ===================== ============================================================
    where:
    ===================== ============================================================
    :math:`quad`            is the :math:`-90^{\circ}` shifter;
    :math:`\\alpha`         is the :math:`\\alpha` component of the Clarke Transform;
    :math:`\\beta`          is the :math:`\\beta` component of the Clarke Transform;
    :math:`\\alpha_+`       is the positive sequnece of the :math:`\\alpha` component;
    :math:`\\beta_+`        is the positive sequnece of the :math:`\\beta` component;
    :math:`\\alpha_-`       is the negative sequnece of the :math:`\\alpha` component;
    :math:`\\beta_-`        is the negative sequnece of the :math:`\\beta` component.
    ===================== ============================================================

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
    alpha_pos_dsogi : complex or a list of complex
        The :math:`\\alpha_+` component.

    beta_pos_dsogi : complex or a list of complex
        The :math:`\\beta_+` component.

    alpha_neg_dsogi : complex or a list of complex
        The :math:`\\alpha_-` component.

    beta_neg_dsogi : complex or a list of complex
        The :math:`\\beta_-` component.

    zero : complex or a list of complex
        The :math:`Zero` sequence.
    
    Examples
    --------
    
    .. code :: python

        import gsyTransforms as trf

        (alpha_pos_dsogi, beta_pos_dsogi,
         alpha_neg_dsogi, beta_neg_dsogi,
         zero)                              = trf.cal_clarke_dsogi(phaseAdata,
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

    return alpha_pos_dsogi, beta_pos_dsogi, alpha_neg_dsogi, beta_neg_dsogi, zero
# =============================================================================
# </Function: calculate the DSOGI symmetrical components for the amplitude invariant Clarke Transform>
# =============================================================================


# =============================================================================
# <Function: calculate the Park Transform (normal)>
# =============================================================================
def cal_park(theta, alpha, beta, zero=0):

    """
    .. _cal_park :

    Calculates the Park Transform. 

    Accepts complex form of the Clarke Transform inputs 
    and the angle of the Synchronous Reference Frame (SRF). This angle
    is commonly provided by the Phase-Locked Loop (PLL) but not always.
    This angle also has huge impact on the outputs of the Park Transform 
    since the changes in the frequencies of the inputs are strongly related
    to this angle.

    Returns the :math:`d`, :math:`q`, :math:`Zero` components.

    .. math ::

        \left[\\begin{matrix}d \\\\ q \\\\ Zero \end{matrix}\\right]
        = 
        \left[
        \\begin{matrix} 
        \cos\\theta & \sin\\theta  & 0
        \\\\ 
        -\sin\\theta & \cos\\theta  & 0
        \\\\
        0 & 0 & 1
        \end{matrix}
        \\right] 
        \left[
        \\begin{matrix} 
        \\alpha 
        \\\\
        \\beta
        \\\\
        Zero
        \end{matrix}
        \\right]

    ===================== ============================================================
    where:
    ===================== ============================================================
    :math:`\\theta`         is the SRF angle in radians;
    :math:`\\alpha`         is the :math:`\\alpha` component of the Clarke Transform;
    :math:`\\beta`          is the :math:`\\beta` component of the Clarke Transform;
    :math:`Zero`            is the :math:`Zero` sequence;
    :math:`d`               is the :math:`d` component of the Park Transform;
    :math:`q`               is the :math:`q` component of the Park Transform;
    ===================== ============================================================

    Parameters
    ----------
    theta : float or a list of float in radians
        The angle of the SRF, usually provided by a PLL.

    alpha : complex or a list of complex
        The :math:`\\alpha` component of the Clarke Transform

    beta : complex or a list of complex
        The :math:`\\beta` component of the Clarke Transform

    zero : any, default = 0
        The :math:`Zero` sequence. This would be output directly without manipulation, 
        since the Zero sequence does not change.

    Returns
    -------
    d : complex or a list of complex
        The :math:`d` component.

    q : complex or a list of complex
        The :math:`q` component.

    zero : as input parameter "zero"
        The Zero sequence.
    
    Examples
    --------
    
    .. code :: python

        import gsyTransforms as trf

        d, q, zero = trf.cal_park(phaseAdata,
                                  phaseBdata,
                                  phaseCdata)

    """
    
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
# <Function: calculate the Park Transform (DSRF)>
# =============================================================================
def cal_park_dsrf(theta, alpha, beta, zero=0):

    """
    .. _cal_park_dsrf :

    Calculates the Park Transform of 
    the Double Synchronous Reference Frame (DSRF). 

    Accepts complex form of the Clarke Transform inputs 
    and the angle of the Synchronous Reference Frame (SRF). 
    
    The DSRF approach is inferior to the DSOGI approach.

    Event the Decoupled-DSRF (DDSRF) is still inferior to the
    DSOGI approach since its performance is hugely dependent on the
    filters used to decouple the DSRF
    (bascially getting rid of the harmonics introudced by the DSRF).

    Returns the :math:`d_{+DSRF}, q_{+DSRF},d_{-DSRF}, q_{-DSRF}` and :math:`Zero` components.

    .. math ::

        \left[\\begin{matrix}d_{+DSRF} \\\\ q_{+DSRF} \end{matrix}\\right]
        = 
        \left[
        \\begin{matrix} 
        \cos\\theta & \sin\\theta
        \\\\ 
        -\sin\\theta & \cos\\theta
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

        \left[\\begin{matrix}d_{-DSRF} \\\\ q_{-DSRF} \end{matrix}\\right]
        = 
        \left[
        \\begin{matrix} 
        \cos\\theta & -\sin\\theta
        \\\\ 
        \sin\\theta & \cos\\theta
        \end{matrix}
        \\right] 
        \left[
        \\begin{matrix} 
        \\alpha 
        \\\\
        \\beta
        \end{matrix}
        \\right]

    ===================== ============================================================
    where:
    ===================== ============================================================
    :math:`\\theta`         is the SRF angle in radians;
    :math:`\\alpha`         is the :math:`\\alpha` component of the Clarke Transform;
    :math:`\\beta`          is the :math:`\\beta` component of the Clarke Transform;
    :math:`d_{+DSRF}`       is the DSRF positive :math:`d` component;
    :math:`q_{+DSRF}`       is the DSRF positive :math:`q` component;
    :math:`d_{-DSRF}`       is the DSRF negative :math:`d` component;
    :math:`q_{-DSRF}`       is the DSRF negative :math:`q` component.
    ===================== ============================================================

    Parameters
    ----------
    theta : float or a list of float in radians
        The angle of the SRF, usually provided by a PLL.

    alpha : complex or a list of complex
        The :math:`\\alpha` component of the Clarke Transform

    beta : complex or a list of complex
        The :math:`\\beta` component of the Clarke Transform

    zero : any, default = 0
        The :math:`Zero` sequence. This would be outputed directly without manipulation. 
        Since the Zero sequence does not change.

    Returns
    -------
    d_dsrf_pos : complex or a list of complex
        The DSRF positive :math:`d` component.

    q_dsrf_pos : complex or a list of complex
        The DSRF positive :math:`q` component.

    d_dsrf_neg : complex or a list of complex
        The DSRF negative :math:`d` component.

    q_dsrf_neg : complex or a list of complex
        The DSRF negative :math:`q` component.

    zero : as input parameter "zero"
        The :math:`Zero` sequence.
    
    Examples
    --------
    
    .. code :: python

        import gsyTransforms as trf

        (d_dsrf_pos, q_dsrf_pos,
         d_dsrf_neg, q_dsrf_neg,
         zero)                      = trf.cal_park_dsrf(phaseAdata,
                                                        phaseBdata,
                                                        phaseCdata)

    """

    # Park transform (DDSRF)
    
    length_theta = len(theta)
    
    length_alpha = len(alpha)
    
    length_beta = len(beta)
    
    if all( x == length_theta for x in (length_theta, length_alpha, length_beta) ):
        
        pass
    
    else:
        
        raise ValueError('Element length mismatch.'
                         + 'The length of theta, alpha and beta must be all the same')

    d_dsrf_pos = cos(theta) * alpha + sin(theta) * beta

    q_dsrf_pos = -1 * sin(theta) * alpha + cos(theta) * beta

    d_dsrf_neg = cos(theta) * alpha + (-sin(theta)) * beta

    q_dsrf_neg = sin(theta) * alpha + cos(theta) * beta

    zero = zero

    return d_dsrf_pos, q_dsrf_pos, d_dsrf_neg, q_dsrf_neg, zero
# =============================================================================
# </Function: calculate the Park Transform (DSRF)>
# =============================================================================


# =============================================================================
# <Function: convert to complex number>
# =============================================================================
def to_complex(r, x, real_offset=0, imag_offset=0):

    """
    .. _to_complex :

    Converts to complex number according to given parameters. 

    .. math ::

        Real &= r \cdot \cos(x) + Offset_{real} 

        Imag &= r \cdot \sin(x) + Offset_{imag} 

        Complex &= Real + j \cdot Imag 

    ===================== =====================================
    where:
    ===================== =====================================
    :math:`r`             is the radius of the complex number;
    :math:`x`             is the angle in radians;
    :math:`Offset_{real}` is the offset to the real part;
    :math:`Offset_{imag}` is the offset to the imaginary part;
    :math:`j`             is the imaginary unit.
    ===================== =====================================

    Parameters
    ----------
    r : float or a list of float
        The radius of the complex number.

    x : float or a list of float in radians
        The angle of the phasor/vector.

    real_offset : float or a list of float
        The offset to the real part, like a DC offset, whose imagnary part is zero.

    imag_offset : float or a list of float
        The offset to the imaginary part.

    Returns
    -------
    complex or a list of complex
        The complex number caculated according to the given parameters.
    
    Examples
    --------
    
    .. code :: python

        import gsyTransforms as trf
        import numpy as np

        a = trf.to_complex(1, np.pi*2/3)
    """
    
    real = r * cos(x) + real_offset
    
    imag = r * sin(x) + imag_offset
    
    return (real + 1j * imag)
# =============================================================================
# </Function: convert to complex number>
# =============================================================================
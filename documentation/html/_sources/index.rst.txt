.. Dynamic Visualisation for Symmetrical Components documentation master file, created by
   sphinx-quickstart on Tue Nov 28 10:33:20 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Dynamic Visualisation for Symmetrical Components (Fortescue, Clarke and Park)
==================================================================================

The purpose of this project is to dynamically visualise all the three-phase symmetrical components. 
This includes the following definitions for symmetrical components: 

* The orginal definition proposed by **Fortescue**, which is at its centenary this year (2018)
* Symmetrical components for the **Clarke Transform** (amplitude invariant), according to the DSOGI
* Symmetrical components for the **Park Transform**, calculated from the DSOGI Clarke Transform symmetrical components

This project would allow the user to define the three-phase inputs and the PLL angle to allow studies of
different situations.

This project would provide the plots in both the time-domain and the polar-domain.

This project would allow the user to export the plots in various formats.

This project would allow the user to export the raw data in CSV.

This project would save user-defined inputs automatically in an INI file.

The GUI of this project is built with Qt designer.

Preview
-------------------------------------------------------------------------------
GUI and Input fields:

.. figure:: examples/exp01_inputfields.png
    :height: 426
    :width: 446.25
    :alt: The user interface

Time-domain plots:

.. figure:: examples/exp01_fig_time.svg

Polar-domain plots:

.. figure:: examples/exp01_fig_polar.svg


Table of Contents
==================================================================================

.. toctree::
    :maxdepth: 3
    :numbered:

    preface
    intro
    gsySymmMain
    gsyTransforms
    gsyPlt
    gsyIO
    gsyINI
    appendix
    bio

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
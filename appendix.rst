Appendix : Conversion of Qt UI files and resource files to Python scripts
=========================================================================

To convert an Qt5 UI file to PY file, use the following command:

.. code::

    pyuic5 -x [UI filename (*.ui)] -o [Python script name (*.py)]

To convert an Qt5 resource file to PY file, use the following command:

.. code::

    pyrcc5 -o [Python script name (*.py)] [resource file filename (*.qrc)]

If you are using different version of Qt, change the numbers in "pyuic5" and "pyrcc5" accordingly.
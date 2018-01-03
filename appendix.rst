Appendix A : Conversion of Qt UI files and resource files to Python scripts
============================================================================

To convert an Qt5 UI file to PY file, use the following command:

.. code::

    pyuic5 -x [UI filename (*.ui)] -o [Python script name (*.py)]

To convert an Qt5 resource file to PY file, use the following command:

.. code::

    pyrcc5 -o [Python script name (*.py)] [resource file filename (*.qrc)]

If you are using different version of Qt, change the numbers in "pyuic5" and "pyrcc5" accordingly.

Reference:

* https://www.youtube.com/watch?v=Dmo8eZG5I2w
* https://stackoverflow.com/questions/36673900/importing-resource-file-to-pyqt-code

Appendix B : Convert SVG to EMF
============================================================================

To convert SVG to EMF for Windows, you can use use inkscape from cmd.

You need to make sure inkscape is installed and it is in your PATH (or you are 
in the installation directory).

The command is in the form of:

.. code::

    inkscape foo.svg --export-emf=bar.emf

You can of course write a batch file for this.

I might write a small Python program for this in the future.

The idea is to get all SVG files in a folder (recursive), and then form the commands and then 
run the commands.

Reference:

* http://inkscape.13.x6.nabble.com/Export-SVG-to-EMF-using-command-line-td4972514.html
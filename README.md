# NRSC-5-Metadata
Parse and Display FM IBOC Metadata output by nrsc5

This is a Python3/GTK script meant to work with @theori-io's nrcs5 proof of concept code.  It will parse data sent to
stderr and present a window showing Station, Artist, and Title.

To run:

nrsc5 104300000 0 2> >(./nrsc5.py)

This command runs nrsc5, tunes the SDR to 104.3 MHz, decodes channel 0, and redirects the output of stderr to stdin of
nrsc5.py.

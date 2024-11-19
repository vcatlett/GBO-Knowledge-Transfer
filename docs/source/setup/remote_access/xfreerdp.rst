***************************
XFreeRDP for Windows Access
***************************

If you need to access Windows hosts remotely, you can use ``xfreerdp``.

You may find that ``xfreerdp`` crashes vncserver/FastX randomly. One solution is to run xfreerdp natively on your local display, tunneling the connection using ssh through prospero. For example, to get into the LASSI Windows host, you might do the following:

Setup the tunnel:

.. code:: bash
    
    ssh -L 3389:lassi.ad.nrao.edu:3389 ssh.gb.nrao.edu

Then, run xfreerdp locally. For example: 

.. code:: bash
    
    xfreerdp --no-nla --plugin cliprdr -g 95% localhost:3389 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:54:01 2023

@author: juan
"""
#!/usr/bin/env python

import pyvista as pv

filename='zNormal.vtp'

mesh = pv.PolyData(filename)
#cpos = mesh.plot()
p = pv.Plotter()
#p.camera_position = [(0,0,900),(0, 0, 450),(0,0,1)]
p.add_mesh(mesh, scalars='U')
p.view_xy()
p.add_title("Estela con IT=5%",font='arial')
#p.show_grid()
#p.show(auto_close=True)
p.save_graphic('zNormal.svg')
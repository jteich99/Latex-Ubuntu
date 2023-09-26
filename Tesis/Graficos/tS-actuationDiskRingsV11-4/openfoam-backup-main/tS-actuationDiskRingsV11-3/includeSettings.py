print("Desea cambiar el archivo includeSettings? [Y/N]")
rta=input()
while rta not in ["N","n","NO","No","no","Y","y","YES","Yes","yes"]:
    print("Corregir respuesta. Desea cambiar el archivo includeSettings? [Y/N]")
    rta=input()

if rta=="N" or rta=="n" or rta=="NO" or rta=="No" or rta=="no":
    print("ok")
elif rta=="Y" or rta=="y" or rta=="YES" or rta=="Yes" or rta=="yes":
    import math

    f = open("includeSettings" ,"w")
    f2 = open("ppSettings", "w")
    print("Diametro en [mts]: ")
    D = float(input())

    # input para el calculo de las esquinas del mallado
    print("Cantidad de diametros aguas abajo: ")
    Dx = float(input())
    Lx=Dx*D
    print("Cantidad de diametros de ancho de tunel: ")
    Dy = float(input())
    Ly=Dy*D
    print("Cantidad de diametros de alto de tunel: ")
    Dz = float(input())
    Lz=Dz*D

    # calculo las esquinas del mallado
    f.write("// esquinas del mallado x=x1, y=x2, z=x3\n")
    for i in range(0,8):
        if i==0 or i==3 or i==4 or i==7:
            globals()['x_%s' % i] = 0
        elif i==1 or i==2 or i==5 or i==6:
            globals()['x_%s' % i] = Lx
        if i==0 or i==1 or i==4 or i==5:
            globals()['y_%s' % i] = 0
        elif i==2 or i==3 or i==6 or i==7:
            globals()['y_%s' % i] = Ly
        if i==0 or i==1 or i==2 or i==3:
            globals()['z_%s' % i] = 0
        elif i==4 or i==5 or i==6 or i==7:
            globals()['z_%s' % i] = Lz
        f.write(str('x_%s' % i) + " " + str(globals()['x_%s' % i]) + ";\n")
        f.write(str('y_%s' % i) + " " + str(globals()['y_%s' % i]) + ";\n")
        f.write(str('z_%s' % i) + " " + str(globals()['z_%s' % i]) + ";\n")

    f.write("\n")

    # definicion de celdas en cada direccion para el mallado

    print("Cantidad de celdas por diámetro, en zona menos densa: ")
    c_D=int(input())
    f2.write("# cantidad de celdas por diametro\n")
    f2.write("c_Diam=" + str(c_D) + "\n")
    l_celda = D/c_D
    print("Longitud de celda: " + str(l_celda))
    f.write("// cantidad de celdas en cada dirección (c_x c_y c_z)\n")
    c_x = Dx*c_D
    f.write("c_x " + str(c_x) + ";\n")
    c_y = Dy*c_D
    f.write("c_y " + str(c_y) + ";\n")
    c_z = Dz*c_D
    f.write("c_z " + str(c_z) + ";\n")

    f.write("\n")

    # grado de expansión de celdas en cada dirección. Dejo constante por ahora
    f.write("// grado de expansión de celdas en cada dirección (ce_x ce_y ce_z)\n")
    f.write("ce_x 1;\n")
    f.write("ce_y 1;\n")
    f.write("ce_z 1;\n")

    f.write("\n")

    ## zona de refinado de mallado. es toda la estela.
    print("¿A cuantos diametros del inlet se tiene a la turbina?")
    x_turb=float(input())
    print("Se considera tunel de viento con actuador en el centro de la altura.")
    print("Se considera un refinado del mallado de 2Dx2D, centrado en el actuador, comenzando desde donde se puso el actuador en x, hasta el fondo del tunel")
    f.write("// zona de refinado de la turbina\n")
    f.write("// se considera actuador en el centro de la altura del tunel\n")
    x1b_0=x_turb*D
    f.write("x1b_0 " + str(x1b_0) + ";\n")
    x1b_1=Lx
    f.write("x1b_1 " + str(x1b_1) + ";\n")
    x2b_0=(Ly*0.5)-1.5*D
    f.write("x2b_0 " + str(x2b_0) + ";\n")
    x2b_1=(Ly*0.5)+1.5*D
    f.write("x2b_1 " + str(x2b_1) + ";\n")
    x3b_0=(Lz*0.5)-1.5*D
    f.write("x3b_0 " + str(x3b_0) + ";\n")
    x3b_1=(Lz*0.5)+1.5*D
    f.write("x3b_1 " + str(x3b_1) + ";\n")

    f.write("\n")

    ## para el topoSetDict, se necesitan las 2 esquinas que encasillan al actuador.
    ## se considera espesor de 3 celdas, según como se pone como ideal en tesis Navarro
    ## en la zona de refinado se tiene el doble de celdas por diámetro
    print("Se considera actuador con 3 celdas de ancho.")
    f.write("// para el topoSectDict armo las esquians de la box que encasilla al actuador\n // considero un actuador con 3 celdas de ancho\n")
    c_Dref=c_D*2
    l_celda_ref=D/c_Dref
    x1d_1=x_turb*D
    f.write("x1d_1 " + str(x1d_1) + ";\n")
    x1d_2=x1d_1 + 3*l_celda_ref
    f.write("x1d_2 " + str(x1d_2) + ";\n")
    x2d_1=Ly/2 - D/2
    f.write("x2d_1 " + str(x2d_1) + ";\n")
    x2d_2=Ly/2 + D/2
    f.write("x2d_2 " + str(x2d_2) + ";\n")
    x3d_1=Lz/2 - D/2
    f.write("x3d_1 " + str(x3d_1) + ";\n")
    x3d_2=Lz/2 + D/2
    f.write("x3d_2 " + str(x3d_2) + ";\n")

    f.write("\n")

    ## variables para el fvOptions
    f.write("// variables para el fvOptions\n")

    print("Velocidad de entrada uniforme [m/s]:")
    Uinf=float(input())
    f.write("Uinf " + str(Uinf) + ";\n")
    f2.write("Uinf=" + str(int(Uinf)) + "\n")

    Ct=0.65
    print("se considera Ct=" + str(Ct))
    f.write("Ct " + str(Ct) + ";\n")

    Cp=0.3
    print("se considera Cp=" + str(Cp))
    f.write("Cp " + str(Cp) + ";\n")

    yaw=0
    print("se considera yaw=" + str(yaw))
    f.write("yaw " + str(yaw) + ";\n")

    pitch=0
    print("se considera pitch=" + str(pitch))
    f.write("pitch " + str(pitch) + ";\n")

    omega=1
    print("se considera omega=" + str(omega) + " rad/s")
    f.write("omega " + str(omega) + ";\n")

    cellSize=10
    print("se considera cellSize=" + str(cellSize))
    f.write("cellSize " + str(cellSize) + ";\n")

    Area=math.pi*0.25*D**2
    f.write("Area " + str(Area) + ";\n")

    # diskPoint es el centro del disco.
    diskPoint_x=D*x_turb
    f.write("diskPoint_x " + str(diskPoint_x) + ";\n")
    diskPoint_y=Ly/2
    f.write("diskPoint_y " + str(diskPoint_y) + ";\n")
    diskPoint_z=Lz/2
    f.write("diskPoint_z " + str(diskPoint_z) + ";\n")

    ## variables para el initalConditions
    Uinlet=Uinf
    f.write("Uinlet " + str(Uinlet) + ";\n")

    ## valor de k turbulenta
    print("para al energía cinetica turbulenta, estimo la intensidad turbulenta en 5%")
    IT=0.05
    f.write("TI " + str(IT) + ";\n")
    TKE=1.5*(Uinlet*IT)**2
    f.write("TKE " + str(TKE) + ";\n")

    C_mu=0.09
    l=0.07*D
    TEpsilon=(C_mu*TKE**(1.5))/l
    f.write("TEpsilon " + str(TEpsilon) + ";\n")

    TOmega=math.sqrt(TKE)/l
    f.write("TOmega " + str(TOmega) + ";\n")

    f.close()

postProcess -func sample -latestTime

source ppSettings
#echo $((c_Diam))

#consulto al usuario el mallado
#echo Cuantas celdas por diámetro tiene el mallado?
#read cel_D

#loop para barrer a los distintos archivos con su nombre según cuantos diametros aguas abajo del actuador esta
for i in 1 2 4 6 8 10 12 15
do
  #copio directo a la carpeta de latex
  mkdir -p ~/LaTex/Tesis/Graficos/001/U${Uinf}_vs_y_${i}D/
  cp -r $(find -name D${i}_U.csv) ~/LaTex/Tesis/Graficos/001/U${Uinf}_vs_y_${i}D/D${i}_U${Uinf}_${c_Diam}.csv
done

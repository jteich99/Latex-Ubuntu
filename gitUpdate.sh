git add .

echo Nombre del commit
read nombre_commit

git commit -m $nombre_commit
git push

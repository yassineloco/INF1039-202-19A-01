#!/bin/sh

# --------------------------------------
#
#  Correction Capstone I
#
#
# --------------------------------------

ETUDIANTS=(
300065026
300111441
300111824
300114153
300115065
300115140
300116370
300116593
300116670
300116685
300116973
300117029
300117178
300117314
300117444
300117705
300117782
300117784
300117806
300117864
300118075
300118196
300118524
)
   
echo "# Participation"
echo "\n## Légende\n"

echo "| Signe              | Signification                 |"
echo "|--------------------|-------------------------------|"
echo "| :heavy_check_mark: | Prêt à être corrigé           |"
echo "| :x:                | Projet inexistant             |"


echo "\n## Résultat\n"
echo "|:hash:| Boréal :id:                | :100:              |"
echo "|------|----------------------------|--------------------|"

i=1


for id in "${ETUDIANTS[@]}"
do
   FILE=${id}.py
   OK="| ${i} | [${id}](${FILE}) | [:heavy_check_mark:](Correction.md#etudiant-${id}) | "
   KO="| ${i} | [${id}](${FILE}) | [:x:](Correction.md#etudiant-${id})                | "
   if [ -f "$FILE" ]; then
       echo ${OK}
   else
       echo ${KO}
   fi
   let "i++"
done

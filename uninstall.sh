
grep -v "python3 password" "../usr/etc/bash.bashrc" > temp; mv temp ../usr/etc/bash.bashrc
rm password.txt
echo "Successfully uninstalled!" 

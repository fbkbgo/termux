
grep -v "python password.py" ../usr/etc/bash.bashrc > temp; mv temp ../usr/etc/bash.bashrc
echo "python3 password.py" >> "../usr/etc/bash.bashrc"

python3 password.py

APM
====
Arduino Package Manager now is only a Arduino's finder and installer package from git hub. In the future it will be **similar** to pip.

Getting started
===============

Only for Arduino >= 1.6

Installs:

git clone git@github.com:jcabdala/apm.git
cd apm
sudo pip install -r requirements.txt


Use:

*Standar mode*:

This mode find in github the package with more forks and shows the 5 first options. 
When you choice one, apm clones the repositorie in /home/<user>/Arduino/libraries/. 

$python apm.py install [name of component]

Ej: python apm.py install dht


*Lucking mode*:

Download and install the first options by default.
 
$python apm.py install -lucky [name of component] 

Ej: python apm.py install -lucky dht



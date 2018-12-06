# Item Catalog Project
This project uses sqlite database by Python that implements website reads categories and items information from a database. also,
to insert,update and delete items (CRUD) that belongs to you after signing in with google +

# Getting Started
To start on this project, you'll need database software (provided by a Linux virtual machine) and run the following line command in order:

python database_setup.py
python seeder.py
python app.py

then visit the website: http://localhost:5000/category/

# Prerequisites
1. Install Vagrant and VirtualBox
2. Clone the fullstack-nanodegree-vm
3. Launch the Vagrant VM (vagrant up)
4. Type 'vagrant ssh' or with windows: winpty vagrant ssh
5. Download and add all application's files locally in the vagrant/catalog directory


# Installing
This project uses Linux-based virtual machine (VM) you can download it and install it from this website
https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
you need to install vagrant you can download it and install it from this website
https://www.vagrantup.com/downloads.html
you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.
Download and add all application's files locally in the vagrant/catalog directory.

# Running the tests and Deployment
To run this project using your Git Bash terminal, you need to type this command to point inot your directory that it has the app.py file
$ cd '<yourDirectory/vagrant/catalog>'

then, you could run the Python application by order running three line commands as the following:
$ python database_setup.py
$ python seeder.py
$ python app.py

then visit the website: http://localhost:5000/category/

You can do a quick check using the pep8 command-line tool, you need to install it by 
$ pip install pep8
in the terminal type the following to check each error
$ pep8 --show-source --show-pep8 * .py
or by using command line
$ pycodestyle * .py


# Built With
Git Bash 
virtual machine
vagrant
Sublime Text editor

# Authors
HADIL SALEH ALSUDIES

# Acknowledgments
All the activities we have done during the virtual session by: MS. MASHAEL ELSAEEDI helped me, Thank you MS. MASHAEL.
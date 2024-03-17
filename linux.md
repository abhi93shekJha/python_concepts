### Linux
- It is an open-source software. Many individuals and communities have created their own version of linux called linux distributions.
- Each distributions fits their specific needs like running servers, desktop computers, mobile phones etc.
- Example of linux distributions are Ubuntu, Debian, Alpine, Fedora, Centos etc. There are 1000s of them present.
- Most of the linux commands are same for these, sometimes they differ.
- Ubuntu is most popular linux distribution widely used.

### Few linux commands
- whoami - shows current user
- echo $0 - shows location of bash program
- history - shows all the commands used
- Package manager - apt (advanced package tool)
- There are many packages available in ubuntu database, but some of them are not installed.
- apt list - list all the packages available (installed and not installed)
- apt update - will get me all the list of pacakges
- apt install nano - this will install nano package
- apt remove nano
- In linux, everything is a file.
- pwd (print working directory).
- ls -1: list the items (one item per line).
- cd ../.. : takes you 2 levels up.
- ls /bin : it will list all the commands kept as program files.
- cd ~ : takes you the home directory. home is for other users, root is for root user. starting with / means path starting from the root.

### Few more commands:
- mkdir test
- mv test docker: moves or renames a directory. (here renames test to docker)
- touch hello.txt file1.tex file2.txt: creates new empty files.
- rm hello.txt file1.txt: removes files
- rm file* : removes file1.txt, file2.txt
- rm -r docker/: removes the directory with all its content recursively.
- nano file1.txt: edit file with nano
- cat file1.txt: shows file content if it is short
- more file1.txt: to open a large file, press enter to scroll down only. exit with q.
- less file1.txt: to open a large file (apt install less), we can scroll up and down with arrow, press space to go to next page, enter (just like more) , then press q to exit.
- head -n 5 file1.txt: shows first 5 line of this file.
- tail -n 5 file1.txt: shows last 5 line of this file.
- cat file1.txt > new_file.txt : reads from file1 and writes it to new_file using redirection command (>).
- cat file1.txt new_file.txt > combined.txt : concatenates data from file1 and new_file and writes it on combined.txt.
- echo hello > hello.txt : writes it to hello.txt
- ls -l /etc > files.txt : writes ths list to file files.txt.
- < is to redirect text from a file to bash prompt, not used much.

### Some linux terms:
- Shell - General name for command line interface. (Ex. Bash, Zsh etc.)
- Bash - Command line shell to interact with an operating system in Unix-like environment.
- ssh - secure shell.
- shell configuration files: For Bash, ~/.bashrc, ~/.bash_profile, ~/.bash_login, ~/.profile are the configuration files present.
- We add commands to these files to perform some operation when the terminal starts.
- Used to automate redundant tasks.
- Example- connecting to ssh with an alias using "sshpass", this way no need to type in password and entire command everytime we login to remote server.
- Just typing in the alias name will do. Not very secure. Below are the steps involved.
- Add line "alias alias_name='sshpass -p password ssh user_name_@xx.xxx.xx.xxx'", to bashrc.
- Restart terminal(or reload bashrc using, "source ~/.bashrc") and simply type in command "alias_name" to connect to remote server.

### Linux
- It is an open-source software. Many individuals and communities have created their own version of linux called linux distributions.
- Each distributions fits their specific needs like running servers, desktop computers, mobile phones etc.
- Example of linux distributions are Ubuntu, Debian, Alpine, Fedora, Centos etc. There are 1000s of them present.
- Most of the linux commands are same for these, sometimes they differ.
- Ubuntu is most popular linux distribution widely used.

  

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

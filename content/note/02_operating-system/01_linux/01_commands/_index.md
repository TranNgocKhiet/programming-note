---
title: "Commands"
weight: 1
---

## ```echo```

Input
```bash
echo "Hello"
```

---

## Show User and Group Information | ```whoami``` and ```id```

Input
```bash
whoami
```

Output
```
yourusername
```
  
Input
```bash
id
```

Output
```
uid=5000(labex) gid=5000(labex) groups=5000(labex),27(sudo),121(ssl-cert),5002(public)
```

- ```uid```: Your User ID (a unique numerical identifier).
- ```gid```: Your primary Group ID.
- ```groups```: All the groups you are a member of.

Input
```bash
id root
```

Output
```
uid=0(root) gid=0(root) groups=0(root)
```

- ```root``` is the superuser – like the administrator of the system!

---

##  Download the latest list of all available software and updates from the software servers | ```apt update```

- ```sudo```: Super User DO, do something with aministrator permission
- ```apt```: Application Manager Tool on systems like Ubuntu
- ```update```: Synchronize app packages on your computer with Internaet Repositpories

Input
```bash
sudo apt update
```

---

##  Interactive process viewer for Unix systems | ```htop```

### To install

- ```htop``` is like Task Manager on Windows
  
Input
```bash
sudo apt install htop
```

### To run

Input
```bash
htop
```

---

## Displays current location in the file system | ```pwd```

- ```pwd``` stands for "print working directory"
  
Input
```bash
pwd
```

---

## Display relationship between the current directory and the home directory | ```echo ~```

Input
```bash
echo ~`
```

---

## Show contents of current directory | ```ls```

Input
```bash
ls
```

---

## Show contents of home directory | ```ls ~```

Input
```bash
ls ~
```

---

## Go to a folder | ```cd```

Input
```bash
cd foldername
```

---

## Go to an above folder | ```cd ..```

Input
```bash
cd ..
```

---

## Go to home directory | ```cd ~```

Input
```bash
cd ~
```

---

## Create an empty file | ```touch```

- The ```touch``` command is used to create an empty file. If the file already exists, it updates the file's timestamp without changing its content. It's a simple way to create new, empty files.
  
Input
```bash
touch file1.txt
```

---

## Write to a file | ```>```

- ```echo`` is a command that prints text.
- The ```>``` symbol redirects the output of echo into a file named ```file2.txt```. If the file doesn't exist, it's created. If it does exist, its content is replaced.

Input
```bash
echo "Hello, Linux" > file2.txt
```

---

## Create hidden file | ```.```

- This creates a hidden file. In Linux, any file or directory name that starts with a dot (```.```) is considered hidden.

Input
```bash
echo "Hidden file" > .hiddenfile
```

---

## Create a directory | ```mkdir testdir```

- The ```mkdir``` command (short for "make directory") creates a new directory named ```testdir```

Input
```bash
mkdir testdir
```

---

## Detailed listing | ```ls -l```

Input
```bash
ls -l
```

---

## Show hidden files | ```ls -a```

Input
```bash
ls -a
```

---

## Combine options | ```ls -la```

- This combines the long format (```-l```) with showing all files (```-a```).

Input
```bash
ls -la
```

---

## List contents of a specific directory | ```ls -l testdir```

- This lists the contents of the testdir directory

Input
```bash
ls -l testdir
```

---

## 


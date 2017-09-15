# Vagrant
http://www.vagrantup.com/

* 全般 - http://qiita.com/daichi87gi/items/d5da33c76295ee32a735
* OS
  * https://app.vagrantup.com/boxes/search
  * http://www.vagrantbox.es/
  * https://app.vagrantup.com/Sliim
  * https://puphpet.com/

## Ubuntu16.04 - ctf
BOX
```
$ vagrant box add ubuntu16-04 https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-vagrant.box
$ vagrant init ubuntu16-04
$ vagrant up
$ vagrant ssh
```

Lib
```
$ sudo apt update
$ sudo apt install gdb python-pip
$ sudo apt-get install lib32z1

// peda
$ git clone https://github.com/longld/peda.git ~/peda
$ echo "source ~/peda/peda.py" >> ~/.gdbinit

// pwntools
$ sudo apt install libssl-dev
$ pip install pwntools

// radare2
$ git clone https://github.com/radare/radare2
$ cd radare2 && sys/install.sh
$ sys/install.sh
$ sys/user.sh
```

## Kali
BOX
```
$ vagrant box add unisec/kali-linux-2017.1-amd64
$ vagrant init unisec/kali-linux-2017.1-amd64
$ vagrant up
// user:root, pass:toor
```
Setup
```
$ passwd
$ apt-get update
$ apt-get upgrade
$ service postgresql start
$ update-rc.d postgresql enable
$ service metasploit start
$ service metasploit stop
$ apt-get install vim
$ mkdir .msf5
$ echo "spool /root/msf_console.log" > /root/.msf5/msfconsole.rc
// hostname
$ vim /etc/hostname
$ vim /etc/hosts
$ reboot
```

## Windows
BOX

```
DL: https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/
$ unzip win10.zip
$ vagrant box add win10 "win10.box"
$ vagrant init win7
$ vagrant up
// initial password: Passw0rd!
```

Tool
* IDA
* OllyDbg
* Stiring
* PEiD

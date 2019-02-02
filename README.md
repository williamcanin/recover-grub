
# Recover Grub ![An image](https://raw.githubusercontent.com/williamcanin/recover-grub/master/logo/recover-grub-64x64.png)

![](https://img.shields.io/github/languages/top/williamcanin/recover-grub.svg?colorB=blue&style=flat-square)
![](https://img.shields.io/github/commit-activity/y/williamcanin/recover-grub.svg?style=flat-square) 
![](https://img.shields.io/github/last-commit/williamcanin/recover-grub.svg?style=flat-square)
![](https://img.shields.io/github/last-commit/williamcanin/recover-grub/master.svg?style=flat-square)
![](https://img.shields.io/github/watchers/williamcanin/recover-grub.svg?style=flat-square)
![](https://img.shields.io/github/stars/williamcanin/recover-grub.svg?style=flat-square)
![](https://img.shields.io/github/forks/williamcanin/recover-grub.svg?style=flat)

Leia em [Português - Brasil](https://github.com/williamcanin/recover-grub/blob/master/README-PtBr.md).

***VERSION - 3.1.0***

## [ ABOUT ]

  "Recover Grub" is a Python script that allows the recovery of Grub
   Linux in a more automatic way, not needing the user
   remember and enter complicated commands.

## [ REQUIREMENTS ]

  > Python 3.+

## [ COMPATIBILITY ]

  Linux systems.

## [ USAGE ]

  **A** - Insert the CD / DVD (or Bootable Pendrive) from a Linux distribution
      on the machine and boot.

  **B** - With the internet active, download the
      "Recover Grub". To do this, execute the command below:

  ~~~shell
  # curl -L git.io/recover_grub.py -o recover_grub.py
  ~~~

  ou

  ~~~shell
  # wget git.io/recover_grub.py
  ~~~

  **C** -  With "Recover Grub" in hand, the next step is to give permission for the file
       "recover_grub.py" and choose the device on the machine where the distribution
       Linux is installed.

  ~~~shell
  # chmod +x recover_grub.py
  ~~~

  ~~~shell
  # ./recover_grub.py device
  ~~~

  **D** - After choosing, the "Recover Grub" will enter the chroot section
      for you to run the Grub recovery command. The command is:

  ~~~shell
  # recover_grub.py start
  ~~~

  **E** - The "Recover Grub" is very intuitive, after finishing, it will say to
      quit the chroot with the "exit" command and then
      restart the machine.

  Run the commands:

  ~~~shell
  # exit
  ~~~

  ~~~shell
  # reboot
  ~~~

## [ DEVELOPER ]

  **Preparing machine for development:**

  A - Create a virtual machine:

~~~shell
   git clone https://github.com/williamcanin/recover-grub.git; cd recover-grub
   python3 -m env
~~~

  B - Enable virtual machine:

  ~~~shell
   . env/bin/activate
  ~~~

  **Tests:**

  The file to run tests can be found in the **tests** folder. The file
  **runtests.sh** will run the "Recover Grub" tests (*script/recover_grub.py*).
  
  The Python module used for testing is the **unittest**.

  **Deploy:**

  The file **.deploy.git** is a simple shell script to perform the deploy and merge of this project. It's intuitive.

## [ LICENSE ]

  MIT License (MIT) <https://opensource.org/licenses/MIT>

 ***Since 2016 © Recover Grub. William C. Canin. All rights reserved. ®***

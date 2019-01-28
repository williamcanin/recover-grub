Leia em [Português - Brasil](https://github.com/williamcanin/recover_grub.py/blob/master/README-PtBr.md).


# Recover Grub <img src="https://raw.githubusercontent.com/williamcanin/recover_grub.py/master/logotype/recover_grub.py-icon.png" alt="Recover Grub Logotype" width="7%" height="7%"/>

***VERSION - 3.1.0***



**[ ABOUT ]**

  "Recover Grub" is a Python script that allows the recovery of Grub
   Linux in a more automatic way, not needing the user
   remember and enter complicated commands.

**[ REQUIREMENTS ]**

  - Python 3.+

**[ COMPATIBILITY ]**

  Linux systems.

**[ USAGE ]**

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

**[ LICENSE ]**

  MIT License (MIT)
  https://opensource.org/licenses/MIT


 ***since 2016 © Recover Grub. William C. Canin. All rights reserved. ®***

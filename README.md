Leia em [Português - Brasil](https://github.com/williamcanin/recover-grub/blob/master/README-PtBr.md).


# Recover Grub <img src="https://raw.githubusercontent.com/williamcanin/recover-grub/master/logotype/recover-grub-icon.png" alt="Recover Grub Logotype" width="7%" height="7%"/>

***VERSION - 3.0 (Beta)***



**[ ABOUT ]**

  "Recover Grub" is a Python script that allows the recovery of Grub
   Linux in a more automatic way, not needing the user
   remember and enter complicated commands.


**[ COMPATIBILITY ]**

  Linux systems.

**[ USAGE ]**

  **A** - Insert the CD / DVD (or Bootable Pendrive) from a Linux distribution
      on the machine and boot.

  **B** - With the internet active, download the
      "Recover Grub". To do this, execute the command below:

  ~~~shell
  # curl -L git.io/recover-grub -o recover-grub
  ~~~

  ou

  ~~~shell
  # wget git.io/recover-grub
  ~~~

  **D** -  With "Recover Grub" in hand, the next step is to give permission for the file
       "recover-grub" and choose the device on the machine where the distribution
       Linux is installed.

  ~~~shell
  # chmod +x recover-grub
  ~~~
  ~~~shell
  # ./recover-grub device
  ~~~

  **E** - After choosing, the "Recover Grub" will enter the chroot section
      for you to run the Grub recovery command. The command is:

  ~~~shell
  # recover-grub start
  ~~~

  **F** - The "Recover Grub" is very intuitive, after finishing, it will say to
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


 ***2018 © Recover Grub. William C. Canin. All rights reserved. ®***

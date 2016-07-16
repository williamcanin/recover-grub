# Recover Grub - Version 1.1.1 <img src="https://raw.githubusercontent.com/williamcanin/recover-grub/master/logotype/recover-grub-icon.png" alt="Recover Grub Logotype" width="7%" height="7%"/>



[ ABOUT ]

  "Recover Grub" is a shell script that allows recovery the Grub
  in Linux in a more automatic way, not needing the user
  remember and type complicated commands.


[ COMPATIBILITY ]

  By default, the "Recover Grub" is compatible only with the
  Arch Linux distribution.


[ USAGE ]

  A - Insert the CD / DVD (or Pendrive Bootable) of Arch Linux distribution
      the machine and give boot.

  B - After starting the terminal Arch Linux, you must make a connection
      with the internet to install Git and do clone "Recover Grub".
      If the machine is connected via a network cable, probably
      the connection is already available. If connection by Wifi,
      use the command:

        # wifi-menu

      This command will enable a setting with the internet through
      of wifi. When setting up your connection, use the following
      command to ping and test the connection to the internet:

        # ping -c3 <any site>

  C - With the active internet may have to download the
      "Recover Grub". To do this, run the following command:

        # curl -L git.io/recover-grub -o recover-grub

        or

        # wget git.io/recover-grub

  D - With the "Recover Grub" in hand, the next step is run it to
      initiate the recovery of Grub.
      However, you should know which device was installed Arch Linux,
      for example: sda, sdb, sdc,... etc.
      ATTENTION !!! Not the partition, is the disk. (sda, sdb, etc ...)
      After, run the following command:
        
        # chmod +x recover-grub
        # recover-grub device <sda|sdb|sdc...>

  E - After the "Recover Grub" start, you will enter the assembly section
      to mount the partition where the Arch Linux is installed and
      subsequently to the recovery section of Grub where will ask the
      user to enter the recovery command.
      Follow the steps, you can not go wrong!


[ LICENSE ]

  MIT License (MIT)
  https://opensource.org/licenses/MIT


 © Recover Grub. William C. Canin. All rights reserved. ®
# Recover Grub - Version 2.0 <img src="https://raw.githubusercontent.com/williamcanin/recover-grub/master/logotype/recover-grub-icon.png" alt="Recover Grub Logotype" width="7%" height="7%"/>



[ ABOUT ]

  "Recover Grub" is a shell script that allows recovery the Grub
  in Linux in a more automatic way, not needing the user
  remember and type complicated commands.


[ COMPATIBILITY ]

  By default, the "Recover Grub" is compatible only with the
  Archlinux.

[ USAGE ]

  A - Insert the CD / DVD (or Pendrive Bootable) of Arch Linux distribution
      the machine and give boot.

  B - After starting the terminal Arch Linux, you must make a connection
      to the Internet to perform the download the "Recover Grub" and
      then run it.
      If the machine is connected via a network cable, probably
      the connection is already available (if not, set).
      If connection by Wifi, use the command:

      # wifi-menu

      This command will enable a setting with the internet through
      of wifi. When setting up your connection, use the following
      command to ping and test the connection to the internet:

      # ping -c3 archlinux.org

      If the answer is not "ping: unknown host archlinux.org", your connection is active.

  C - With the active internet may have to download the
      "Recover Grub". To do this, run the following command:

      # curl -L git.io/recover-grub -o recover-grub

      or

      # wget git.io/recover-grub

  D - As "Recover Grub" in hand, the next step is running for permission of 
     "Recover Grub" and choose the machine device where the Arch Linux is  
      installed. 
        
      # chmod +x recover-grub
      # recover-grub device

  E - After choosing the "Recover Grub" will enter the chroot session for you 
      to run the Grub recovery command. The command is:

      # recover-grub start

  F - The "Recover Grub" is quite intuitive, after finishing, he will tell to
      restart the machine that the recovery was successful.
      Run the command:

      # reboot

[ LICENSE ]

  MIT License (MIT)
  https://opensource.org/licenses/MIT


 © Recover Grub. William C. Canin. All rights reserved. ®

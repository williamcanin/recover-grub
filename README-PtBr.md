Read in [English](https://github.com/williamcanin/recover-grub/blob/master/README.md).

# Recover Grub <img src="https://raw.githubusercontent.com/williamcanin/recover-grub/master/logotype/recover-grub-icon.png" alt="Recover Grub Logotype" width="7%" height="7%"/>

***VERSÃO - 3.0.1***



**[ SOBRE ]**

  "Recover Grub" é um script em Python que permite a recuperação do Grub
  Linux de uma forma mais automática, não precisando o usuário
  lembrar e digitar comandos complicados.


**[ REQUERIMENTOS]**

  - Python 3.+

**[ COMPATIBILIDADE ]**

  Sistemas Linux.

**[ USANDO ]**

  **A** - Insira o CD/DVD (ou Pendrive Bootável) de uma distribuição Linux
      na máquina e dê boot.

  **B** - Com a internet ativa, realize o download do
      "Recover Grub". Para isso, execute o comando abaixo:

  ~~~shell
  # curl -L git.io/recover-grub -o recover-grub
  ~~~

  ou

  ~~~shell
  # wget git.io/recover-grub
  ~~~

  **D** -  Com "Recuperar Grub" na mão, o próximo passo é dar permissão de para o
       arquivo "recover-grub" e escolher o dispositivo na máquina onde a
       distribuição Linux está instalada.

  ~~~shell
  # chmod +x recover-grub
  ~~~
  ~~~shell
  # ./recover-grub device
  ~~~

  **E** - Após escolher, o "Recover Grub" irá entrar na seção de chroot
      para você executar o comando de recuperação do Grub. O comando é:

  ~~~shell
  # recover-grub start
  ~~~

  **F** - O "Recover Grub" é bem intuitivo, após terminar, ele irá dizer para
      sair do chroot com o comando "exit" e logo em seguida pedir para  
      reiniciar a máquina.

  Execute os comandos:

  ~~~shell
  # exit
  ~~~
  ~~~shell
  # reboot
  ~~~

**[ LICENÇA ]**

  MIT License (MIT)
  https://opensource.org/licenses/MIT


 ***2018 © Recover Grub. William C. Canin. All rights reserved. ®***

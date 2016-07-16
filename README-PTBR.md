# Recover Grub - Version 1.1.1 <img src="https://raw.githubusercontent.com/williamcanin/recover-grub/master/logotype/recover-grub-icon.png" alt="Recover Grub Logotype" width="7%" height="7%"/>



[ ABOUT ]

  "Recover Grub" é um script shell que permite a recuperação do Grub
  Linux de uma forma mais automática, não precisando o usuário
  lembrar e digitar comandos complicados.


[ COMPATIBILIDADE ]

  Por padrão, o "Recover Grub" é compativel apenas com a
  distribuição Arch Linux.


[ USAGE ]

  A - Insira o CD/DVD (ou Pendrive Bootável) da distribuição Arch Linux
      na máquina e dê boot.

  B - Após iniciar o terminal do Arch Linux, deve realizar uma conexão
      com a internet para realizar o download o "Recover Grub" e
      posteriormente executa-lo.
      Se a máquina está conectada através de um cabo de rede, provavelmente
      a conexão já está disponivel (se não está, configure) Se for conexão
      por Wifi, use o comando:

        # wifi-menu

      Esse comando vai possibilitar uma configuração com a internet através
      do wifi. Quando configurar sua conexão, use o comando abaixo para pingar
      e testar a conexão com a internet:

        # ping -c3 <site qualquer>

  C - Com a internet ativa, já pode realizar o download do
      "Recover Grub". Para isso, execute o comando abaixo:

        # curl -L git.io/recover-grub -o recover-grub

        ou

        # wget git.io/recover-grub

  D - Com o "Recover Grub" em mãos, o próximo passo é executa-lo para
      dar inicio a recuperação do Grub.
      Pórem, você deve saber qual dispositivo o Arch Linux foi
      instalado, por exemplo: sda, sdb, sdc,... etc.
      ATENÇÃO !!! Não é a partição, é o disco. (sda,sdb,etc...)
      Após saber qual o dispositivo, execute o comando abaixo:

        # chmod +x recover-grub
        # recover-grub device <sda|sdb|sdc...>

  E - Após o "Recover Grub" iniciar, o mesmo irá entrar na seção de
      Montagem para montar a partição onde o Arch Linux está instalado e
      posteriormente entrar na seção de recuperação do Grub, onde
      irá pedir para que o usuário insira o comando de recuperação.
      Siga os passos, não tem como errar!


[ LICENSE ]

  MIT License (MIT)
  https://opensource.org/licenses/MIT


 © Recover Grub. William C. Canin. All rights reserved. ®
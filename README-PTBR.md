# Recover Grub - Version 1.1.1 <img src="https://raw.githubusercontent.com/williamcanin/recover-grub/master/logotype/recover-grub-icon.png" alt="Recover Grub Logotype" width="7%" height="7%"/>



[ ABOUT ]

  "Recover Grub" é um script shell que permite a recuperação do Grub
  Linux de uma forma mais automática, não precisando o usuário
  lembrar e digitar comandos complicados.


[ COMPATIBILIDADE ]

  Por padrão, o "Recover Grub" é compativel apenas com a
  distribuição Arch Linux e Manjaro.


IMPORTANTE !!! O "Recover Grub" NÃO é compativel com instalações usando LVM ou Sistema de Arquivos instalado com criptografia.

[ USAGE ]

  A - Insira o CD/DVD (ou Pendrive Bootável) da distribuição Arch Linux
      na máquina e dê boot.

  B - Após iniciar o terminal do Arch Linux, deve realizar uma conexão
      com a internet para realizar o download o "Recover Grub" e
      posteriormente executa-lo.
      Se a máquina está conectada através de um cabo de rede, provavelmente
      a conexão já está disponivel (se não está, configure).
      Se for conexão por Wifi, use o comando:

      # wifi-menu

      Esse comando vai possibilitar uma configuração com a internet através
      do wifi. Quando configurar sua conexão, use o comando abaixo para pingar
      e testar a conexão com a internet:

      # ping -c3 archlinux.org

      Se a resposta não for "ping: unknown host archlinux.org", sua conexão já está ativa.

  C - Com a internet ativa, realize o download do
      "Recover Grub". Para isso, execute o comando abaixo:

      # curl -L git.io/recover-grub -o recover-grub

        ou

      # wget git.io/recover-grub

  D -  Como "Recuperar Grub" na mão, o próximo passo é dar permissão de para o 
      "Recuperar Grub" e escolher o dispositivo na máquina onde o Arch Linux está instalado.

      # chmod +x recover-grub
      # recover-grub device

  E - Após escolher, o "Recover Grub" irá entrar na seção de chroot
      para você executar o comando de recuperação do Grub. O comando é:

      # recover-grub start

  F - O "Recover Grub" é bem intuitivo, após terminar, ele irá dizer para 
      reiniciar a máquina que a recuperação foi realizada com sucesso. 
      Execute o comando:

      # reboot

[ LICENSE ]

  MIT License (MIT)
  https://opensource.org/licenses/MIT


 © Recover Grub. William C. Canin. All rights reserved. ®
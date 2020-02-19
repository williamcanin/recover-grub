# Recover Grub ![An image](https://raw.githubusercontent.com/williamcanin/recover-grub/master/.github/readme/recover-grub-64x64.png)

[![Build Status](https://travis-ci.org/williamcanin/recover-grub.svg?branch=master)](https://travis-ci.org/williamcanin/recover-grub) ![](https://img.shields.io/github/languages/top/williamcanin/recover-grub.svg?colorB=blue&style=flat-square) ![](https://img.shields.io/github/commit-activity/y/williamcanin/recover-grub.svg?style=flat-square) ![](https://img.shields.io/github/last-commit/williamcanin/recover-grub.svg?style=flat-square) ![](https://img.shields.io/github/last-commit/williamcanin/recover-grub/master.svg?style=flat-square) ![](https://img.shields.io/github/watchers/williamcanin/recover-grub.svg?style=flat-square) ![](https://img.shields.io/github/stars/williamcanin/recover-grub.svg?style=flat-square) ![](https://img.shields.io/github/forks/williamcanin/recover-grub.svg?style=flat-square)

Versão atual: ![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/williamcanin/recover-grub?style=flat-square)

Read in [English](https://github.com/williamcanin/recover-grub/blob/master/README.md).

## [ SOBRE ]

"Recover Grub" é um script em Python que permite a recuperação do Grub
Linux de uma forma mais automática, não precisando o usuário
lembrar e digitar comandos complicados.

## [ REQUERIMENTOS]

> Python 3.+

## [ COMPATIBILIDADE ]

Sistemas Linux.

## [ USANDO ]

**A** - Insira o CD/DVD (ou Pendrive Bootável) de uma distribuição Linux
    na máquina e dê boot.

**B** - Com a internet ativa, realize o download do
    "Recover Grub". Para isso, execute o comando abaixo:

~~~shell
# curl -L git.io/recover_grub -o recover_grub.py
~~~

ou

~~~shell
# wget git.io/recover_grub
~~~

**C** -  Com "Recuperar Grub" na mão, o próximo passo é dar permissão de para o
     arquivo "recover_grub.py" e escolher o dispositivo na máquina onde a
     distribuição Linux está instalada.

~~~shell
# chmod +x recover_grub.py
~~~

~~~shell
# python recover_grub.py device
~~~

**D** - Após escolher, o "Recover Grub" irá entrar na seção de chroot
    para você executar o comando de recuperação do Grub. O comando é:

~~~shell
# python recover_grub.py start
~~~

**E** - O "Recover Grub" é bem intuitivo, após terminar, ele irá dizer para
    sair do chroot com o comando "exit" e logo em seguida pedir para  
    reiniciar a máquina.

Execute os comandos:

~~~shell
# exit
~~~

~~~shell
# reboot
~~~

## [ DESENVOLVEDOR ]

**Preparando máquina para desenvolvimento:**

A - Crie uma máquina virtual:

~~~shell
git clone https://github.com/williamcanin/recover-grub.git; cd recover-grub
python -m venv venv
~~~

B - Ativar máquina virtual:

~~~shell
 . venv/bin/activate
~~~

**Testes:**

Para executar os testes do Recover Grub, faça:

~~~shell
$ make tests
~~~

O módulo Python usado para os testes é o **unittest**.

## [ LICENÇA ]

MIT License [MIT](https://github.com/williamcanin/recover-grub/blob/master/LICENSE)

***Desde 2016 © Recover Grub. William C. Canin. All rights reserved. ®***

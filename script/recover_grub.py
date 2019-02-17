#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Information:

# ******************************************************************************
# Type: Python 3
# Description: Mount partition Linux and Recover the Grub on Linux
# Script Name: Recover Grub
# Project URL: https://github.com/williamcanin/recover-grub.git
# URL Script: http://git.io/recover-grub

# Tools used:
#   VS Code:
#       - wrap-guide (Preferred Line Lenght: 120)
#       - linter
#       - linter-flake8 (Max Line Length: 120)
#       -- ignore="W605"

# Author: William C. Canin
#   Contacts:
#   E-Mail: william.costa.canin@gmail.com
#   WebSite: https://williamcanin.github.io
#   GitHub: https://github.com/williamcanin

# ******************************************************************************

# # Import for Debugging
# from pdb import set_trace


class RecoverGrub_UI:
    def __init__(self):
        self._header = '\033[36mⓘ  '
        self._warning = '\033[93m⚠  '
        self._reply = '\033[95m→ '
        self._okgreen = '\033[92m✔ '
        self._error = '\033[91m✖ '
        self._end = '\033[0m'

        # Design text using figlet. Install: $ sudo apt install figlet
        # Usage: $ figlet <Text>
        print(f"""
\033[36mWelcome to\033[0m
\033[93m
 ____                               ____            _
|  _ \ ___  ___ _____   _____ _ __ / ___|_ __ _   _| |__
| |_) / _ \/ __/ _ \ \ / / _ \ '__| |  _| '__| | | | '_ \\
|  _ <  __/ (_| (_) \ V /  __/ |  | |_| | |  | |_| | |_) |
|_| \_\___|\___\___/ \_/ \___|_|   \____|_|   \__,_|_.__/\033[0m
                                    \xa9 since 2016 - v{self.config['appversion']}
        """)

    def printColor(self, type, color, message, options: object = ''):
        if type == 'print':
            return print(f'{color}{message}' + self._end)
        elif type == 'input':
            return input(f'{color}{message}' + self._end)
        elif type == 'except':
            return print(f'\n{color}{message}' + self._end, options)
        else:
            raise print('Error in first argument in "PrintColor"')


class RecoverGrub_Engine(RecoverGrub_UI):

    config = {'appname': 'Recover Grub',
              'appscript': 'recover_grub.py',
              'appconfig': '/etc/recover-grub.json',
              'execdir': '/usr/local/bin/',
              'python_version': 3,
              'appversion': '3.1.1',
              'mount_dir': '/mnt',
              'name_crypto_open': 'filesystem2',
              'crypto_type': 'crypto_LUKS',
              'author': {'name': 'William da Costa Canin',
                         'email': 'william.costa.canin@gmail.com',
                         'website': 'https://williamcanin.me',
                         'github': 'https://github.com/williamcanin'}
              }

    config.update({'pathexec': config['execdir'] + config['appscript']})

    def credits(self):
        from datetime import date
        print(f"""\033[36m
   ---------------------------------------------------------
  |            {self.config['appname']} - Version {self.config['appversion']}                 |
   ---------------------------------------------------------
  |                         Credits:                        |
  |                                                         |
  |           Author: {self.config['author']['name']}                |
  |           E-Mail: {self.config['author']['email']}         |
  |           Website: {self.config['author']['website']}              |
  |           GitHub: {self.config['author']['github']}       |
  |           Locale: Brazil - SP                           |
  |                                                         |
  |                                                         |
  |    {self.config['appname']} © 2016-{date.today().year} - All Right Reserved.       |
  |    Doc: http://github.com/williamcanin/recover-grub     |
  |---------------------------------------------------------|
        \033[0m""")

    def verify_user(self, uid):
        """
            Function to check if script is running with superuser.
        """
        from os import geteuid

        if geteuid() != uid:
            self.printColor('print', self._warning,
                            self.config['appname'] + ' can only be run with superuser (root). Aborted!')
            exit(0)
            # return False

    def select_device(self):
        """
            A function that converses with the user to make the selection of the devices of the machine, for
            the assembly.
        """
        self.printColor('print', self._header, 'Select the device in which the Grub will be recovered')

        try:
            while True:
                print()
                for index, item in enumerate(self.get_device(), start=1):
                    print(f'{index}: {item}')
                index_quit = index + 1
                print(f'{index_quit}: Quit\n')
                choice = self.printColor('input', self._reply, 'Please enter your choice (1-' + str(index + 1) + '): ')
                if not choice.isdigit():
                    self.printColor('print', self._error, 'Enter numbers only')
                    continue
                elif int(choice) == index_quit:
                    return str(self.printColor('print', self._warning, 'Aborted by user'))
                    break
                elif int(choice) > (index_quit):
                    self.printColor('print', self._error, 'Option invalid')
                    continue
                else:
                    choice = (int(choice) - 1)
                    choice_device = self.get_device()[int(choice)]
                    return choice_device
                    break
        except Exception as err:
                return self.printColor('except', self._warning, 'There was some error making the choice.', err)
        except KeyboardInterrupt as ki:
                return self.printColor('except', self._warning, 'Interrupt by user using Ctrl+C.', ki)

    def copyfiles(self, file):
        """
            Function to perform a copy of this same script for the assembled pointer.
        """
        from shutil import copy2
        from os import chmod
        if file == 'exec':
            copy2(self.config['appscript'], self.config['mount_dir'] + self.config['pathexec'])
            chmod(self.config['mount_dir'] + self.config['pathexec'], 0o775)

    def create_config(self, file, mounted, recovered, device=''):
        """
            Function to create .json configuration file.
        """
        from json import dump
        data = {"status": {"mounted": mounted, "recovered": recovered}, "device": device}
        with open(file, 'w') as outfile:
            dump(data, outfile)

    def read_config(self, path_file: object):
        """
            Function to read .json configuration file.
        """
        from json import load
        from os.path import isfile
        if isfile(path_file):
            with open(path_file) as outfile:
                data = load(outfile)
        return data

    def python_version_required(self, p_version):
        """
            Function to check the version of Python that this script uses.
        """
        import sys
        try:
            if sys.version_info[0] < p_version:
                raise Exception('Must be using Python {}'.format(p_version))
            else:
                return True
        except Exception as err:
            print('Error!', err)
            exit(1)

    def menu_args(self):
        """
            This function will return the parameters passed in the execution of the script.
        """
        from argparse import ArgumentParser, RawTextHelpFormatter
        try:
            parser = ArgumentParser(prog=self.config['appname'],
                                    usage='python3 ' + self.config['appscript'] + ' {device | start | credits | -h}',
                                    description=self.config['appname'] + ' is a script to perform Grub recovery \
                                    on Linux.',
                                    formatter_class=RawTextHelpFormatter,
                                    epilog="See you later!!")
            parser.add_argument('command', action='store', metavar="{device | start | credits | -h}",
                                type=str,
                                help=f"""
device     Performs the partition search in the distribution to be
           recovered, and the devices to install Grub.

start      It really starts the Grub recovery.
           Note: First you have to execute the "device" option.

credits    Print the {self.config['appname']} credits.
                                         """)
            args = parser.parse_args()
            return args

        except Exception as err:
            return self.printColor('except', self._warning, 'Error in passing arguments..', err)

    # @property
    def get_device(self):
        """
            A function that returns a list of SD / HS / SSD devices on the machine.
        """
        try:
            from subprocess import check_output
            command = '''lsblk -d | awk '{print "/dev/" $1}' | grep 'sd\\|hd\\|vd' '''
            out = check_output(command, shell=True, universal_newlines=True).split()
            return out
        except Exception as err:
            return self.printColor('except', self._warning, 'Unable to pick up the devices.', err)

    def get_system(self, type_):
        """
            A function gets an argument to return what type of system the machine is using. If the argument is
            'OS', it will return Windows, Linux or OSX, and the argument is 'distro', it will return the Linux
            distribution being used.
        """
        if type_.lower() == 'os':
            from sys import platform
            if platform == "linux" or platform == "linux2":
                check_sys = 'linux'
            else:
                check_sys = str(self.printColor('print', self._error,
                                                'System not compatible with this script. Use only Linux.'))
                exit(1)
        else:
            raise Exception('Error check system.')
        return check_sys

    def select_type_partition(self):
        """
            Select partitions
        """
        self.printColor('print', self._header, 'Select the partition type that the system is installed on:')
        while True:
            try:
                # For non-beta version.
                # Option 2 -> 2: {self.config['crypto_type'].title().replace('_', ' (')})
                choice = input(f"""
1: Ext3/Ext4
2: Btrfs
3: Quit

\033[95m→ Please enter your choice [1-2]: \033[0m""")

                if choice == "1":
                    type_partition = 'ext'
                    break
                elif choice == "2":
                    type_partition = 'btrfs'
                    break
                # For non-beta version.
                # elif choice == "3":
                #     type_partition = self.config['crypto_type']
                #     break
                elif choice == "3":
                    return str(self.printColor('print', self._warning, 'Aborted by user.'))
                    break
                else:
                    self.printColor('print', self._error, 'Option invalid!')
                    continue
            except Exception as err:
                return self.printColor('except', self._warning, 'Something unexpected happened :(', err)
            except KeyboardInterrupt as ki:
                return self.printColor('except', self._warning, 'Interrupt by user using Ctrl+C.', ki)

        return type_partition

    def get_distro(self, os_release, key):
        """
            Function to return the Linux distribution data.
        """
        try:
            from subprocess import check_output
            content_os_release = check_output(['cat', os_release], universal_newlines=True)
            dict_os_release = dict([i.split('=') for i in content_os_release.strip().split('\n')])
            distro_name = dict_os_release[key].replace('"', '')
            return distro_name
        except Exception as err:
            return self.printColor('except', self._warning, 'No distro was returned.', err)

    def mount_partition(self, device_type):
        """
            Function to mount the partition to be recovered by Grub.
        """
        from os.path import isfile
        from subprocess import check_output, check_call

        try:
            shell_command = '''blkid | grep ''' + device_type + ''' | awk '{print $1}' | cut -d":" -f1'''
            devices_output = check_output(shell_command, shell=True,
                                          universal_newlines=True).splitlines()
            distro_current = self.get_distro('/etc/os-release', 'NAME')
        except Exception as err:
            return self.printColor('except', self._error, 'There was an error using superuser command.', err)
        except KeyboardInterrupt as ki:
            return self.printColor('except', self._warning, 'Interrupt by user using Ctrl+C.', ki)

        if len(devices_output) == 0:
            self.printColor('print', self._warning,
                            'No device of type "' + device_type.title() + '" was found. Aborded.')
            exit(1)

        if device_type == 'ext' or device_type == 'btrfs':
            for partition in devices_output:
                if isfile(self.config["mount_dir"] + '/etc/os-release'):
                    self.printColor('print', self._warning, 'A mounted partition already exists in \
                                    ' + self.config["mount_dir"] + '. Use the "sudo umount \
                                    ' + self.config["mount_dir"] + '" command to unmount, and re-run the \
                                    ' + self.config["appname"] + '.')
                    break
                else:
                    check_output(['mount', partition, self.config["mount_dir"]])
                    if isfile(self.config["mount_dir"] + '/etc/os-release'):
                        distro_monted = self.get_distro(self.config["mount_dir"] + '/etc/os-release', 'NAME')
                        if distro_monted == distro_current:
                            try:
                                distro_pretty_name = self.get_distro(self.config["mount_dir"] + '/etc/os-release',
                                                                     'PRETTY_NAME')
                                check_output(['mount', '--bind', '/dev', self.config["mount_dir"] + '/dev'])
                                check_output(['mount', '--bind', '/dev/pts', self.config["mount_dir"] + '/dev/pts'])
                                check_output(['mount', '--bind', '/proc', self.config["mount_dir"] + '/proc'])
                                check_output(['mount', '--bind', '/sys', self.config["mount_dir"] + '/sys'])
                                self.printColor('print', self._okgreen, 'Partition containing " \
                                                ' + distro_pretty_name + '" was found and mounted on " \
                                                ' + self.config['mount_dir'] + '".')
                                self.create_config(self.config['mount_dir'] + self.config['appconfig'], 'true', 'false',
                                                   self.read_config(self.config['appconfig'])['device'])
                                self.copyfiles('exec')
                                self.printColor('print', self._warning, 'You are now in the chroot. Run \
                                                \033[36m"recover-grub start"\033[93m to start Grub recovery.')
                                # Enter in Chroot.
                                check_call(['chroot', self.config['mount_dir'], '/bin/bash'])
                                # Runs after exiting the chroot.
                                check_output(['rm', '-f', self.config['mount_dir'] + self.config['appconfig']])
                                check_output(['rm', '-f', self.config['mount_dir'] + self.config['pathexec']])
                                check_output(['umount', '-R', self.config["mount_dir"]])
                                self.printColor('print', self._warning, 'Now run the "reboot" command. Bye.')
                            except Exception as err:
                                self.printColor('except', self._warning, 'Error in performing assemblies.', err)
                                check_output(['umount', '-R', self.config["mount_dir"]])
                            break
                        elif distro_monted != distro_current:
                            check_output(['umount', self.config["mount_dir"]])
                            continue
                    else:
                        check_output(['umount', self.config["mount_dir"]])

        # For non-beta version.
        # elif device_type == self.config['crypto_type']:
        #     for partition in devices_output:
        #         if isfile(self.config["mount_dir"] + '/etc/os-release'):
        #             self.printColor('print', self._warning, 'A mounted partition already exists in ' +
        #                             self.config["mount_dir"] + '. Use the "sudo umount ' +
        #                             self.config["mount_dir"] + '" command to unmount, and re-run the ' +
        #                             self.config["appname"] + '.')
        #             break
        #         else:
        #             # cryptsetup
        #             try:
        #                 check_output('cryptsetup open ' + partition + ' ' + self.config['name_crypto_open'],
        #                              shell=True, universal_newlines=True)
        #             except KeyboardInterrupt as ki:
        #                 return self.printColor('except', self._warning, 'Interrupt by user using Ctrl+C.', ki)
        #             if not isfile(self.config["mount_dir"] + '/etc/os-release'):
        #                 print('Not system.')

    def main(self):
        """
            Main function that starts the processes.
        """
        from subprocess import check_output
        from os.path import isfile
        # Requeriments
        self.python_version_required(self.config['python_version'])
        self.get_system('os')
        self.verify_user(0)

        if self.menu_args().command == 'device':

            if not isfile(self.config['appconfig']):
                self.create_config(self.config['appconfig'], 'false', 'false',
                                   self.select_device())

            if self.read_config(self.config['appconfig'])['status']['mounted'] == 'true':
                self.printColor('print', self._warning,
                                'The partition is already mounted. Use the command "recover-grub start".')

            elif self.read_config(self.config['appconfig'])['status']['mounted'] == 'false':

                if self.read_config(self.config['appconfig'])['device'] == 'None':
                    self.printColor('print', self._error,
                                    'You did not specify the "device". There is no way to go. Repeat the steps \
                                    again with the command "recover-grub device".')
                    check_output(['rm', '-f', self.config['appconfig']])
                    exit(1)

                self.mount_partition(self.select_type_partition())

        elif self.menu_args().command == 'start':

            if isfile(self.config['appconfig']):
                if self.read_config(self.config['appconfig'])['status']['mounted'] == 'true':
                    if self.read_config(self.config['appconfig'])['status']['recovered'] == 'true':
                        self.printColor('print', self._warning, 'You have already made the recovery in this session, if \
                                        you want to do again skirt with command "exit".')
                        exit(0)

                    self.printColor('print', self._header, 'Starting Grub recovery ...')
                    check_output(['grub-mkconfig', '-o', '/boot/grub/grub.cfg'])
                    check_output(['grub-install', self.read_config(self.config['appconfig'])['device']])
                    self.create_config(self.config['appconfig'], 'true', 'true')
                    self.printColor('print', self._okgreen, 'The Grub recovery was completed. Run the "exit" \
                                     command to exit the chroot.')

                else:
                    self.printColor('print', self._warning,
                                    'The recovery partition is not mounted. Run "recover-grub device".')

            else:
                self.printColor('print', self._warning,
                                'You must specify the device and partition before starting recovery. Run \
                                "recover-grub device"')

        elif self.menu_args().command == 'credits':
            self.credits()


if __name__ == '__main__':
    recover_grub = RecoverGrub_Engine()
    recover_grub.main()

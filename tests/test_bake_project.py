#!/usr/bin/env python3

from src.recover_grub import RecoverGrub_Engine
from unittest import TestCase, main
# from tests import __tempdir__
# from pdb import set_trace


class Tests_RecoverGrub(TestCase):
    def setUp(self):
        self.engine = RecoverGrub_Engine()

    def test_get_device(self):
        device = self.engine.get_device()
        self.assertIn(device, [['/dev/sda']])

    def test_get_system(self):
        self.assertEqual(self.engine.get_system('os'), 'linux')

    def test_get_system_error(self):
         with self.assertRaises(AssertionError):
            self.assertEqual(self.engine.get_system('os'), 'win')

    def test_python_version_required(self):
        self.assertEqual(self.engine.python_version_required(3), True)

    def test_select_type_partition(self):
        self.assertIn(self.engine.select_type_partition(), ['ext', 'btrfs', 'None'])

    def test_get_distro(self):
        distro_current = self.engine.get_distro('/etc/os-release', 'NAME')
        distros = ['Ubuntu', 'Arch Linux', 'Fedora', 'Debian']
        self.assertIn(distro_current, distros)

    def test_select_device(self):
        self.assertIn(self.engine.select_device(), ['/dev/sda', 'None'])

    def test_verify_user(self):
        with self.assertRaises(SystemExit) as e:
            self.engine.verify_user(0)
        self.assertEqual(e.exception.code, 0)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

from script.recover_grub import RecoverGrub_Engine
from unittest import TestCase, main


class Tests_RecoverGrub(TestCase):
    def setUp(self):
        self.engine = RecoverGrub_Engine()

    def test_get_device(self):
        device = self.engine.get_device()
        self.assertEqual(device, ['/dev/sda'])

    def test_get_system(self):
        self.assertEqual(self.engine.get_system('os'), 'linux')

    def test_python_version_required(self):
        self.assertEqual(self.engine.python_version_required(3), True)

    # def test_select_type_partition(self):
    #     self.assertEqual(self.engine.select_type_partition(), 'ext')

    def test_get_distro(self):
        distro_current = self.engine.get_distro('/etc/os-release', 'NAME')
        self.assertEqual(distro_current, 'Ubuntu')

    # def test_select_device(self):
    #     self.assertEqual(self.engine.select_device(), '/dev/sda')


if __name__ == '__main__':
    main()

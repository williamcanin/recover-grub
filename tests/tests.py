#!/usr/bin/env python3

from script.recover_grub import RecoverGrub_Engine
from unittest import TestCase, main
from pdb import set_trace


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

    def test_select_type_partition(self):
        self.assertEqual(self.engine.select_type_partition(), 'ext')
        # self.assertEqual(self.engine.select_type_partition(), 'None')

    def test_get_distro(self):
        distro_current = self.engine.get_distro('/etc/os-release', 'NAME')
        self.assertEqual(distro_current, 'Ubuntu')

    def test_select_device(self):
        self.assertEqual(self.engine.select_device(), '/dev/sda')

    def test_verify_user(self):
        self.assertFalse(self.engine.verify_user(0))

    def test_create_config(self):
        from os.path import isfile
        from os import remove
        conf = '.' + self.engine.config['appconfig']
        if not isfile(conf):
            self.engine.create_config(conf, 'false', 'false')
            created = True
        self.assertTrue(created)
        remove(conf)


if __name__ == '__main__':
    main()

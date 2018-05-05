import unittest
import os
import shutil

from context import backup_client
from backup_client.filehandler import observer


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_observer = observer.FileObserver()
        self.test_env = os.path.join(os.getcwd(), 'filhandler')
        os.mkdir(self.test_env)

    def tearDown(self):
        shutil.rmtree(self.test_env)

    def test_observer_add_File(self):
        self.assertEqual(self.file_observer.add_file(''), 1)
        testfile = os.path.join(self.test_env, 'testfile.txt')
        open(testfile, 'w+')
        self.assertEqual(self.file_observer.add_file(testfile), 0)

    def test_observer_add_Dir(self):
        self.assertEqual(self.file_observer.add_dir(''), 1)
        testdir = os.path.join(self.test_env, 'testdir')
        os.mkdir(testdir)
        self.assertEqual(self.file_observer.add_dir(testdir), 0)


if __name__ == '__main__':
    unittest.main()
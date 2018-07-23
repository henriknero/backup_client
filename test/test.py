import unittest
import os
import sys
import shutil
import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backup_client.filehandler import observer
from backup_client.network import gitcom




class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_observer = observer.FileObserver('test_user','cisco123')
        self.test_env = os.path.join(os.getcwd(), 'filhandler')
        os.mkdir(self.test_env)

    def tearDown(self):
        shutil.rmtree(self.test_env)


    """
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
    """
class TestNetworkModule(unittest.TestCase):
    def setUp(self):
        self.file_observer = observer.FileObserver('test_user', 'cisco123')

        self.test_env = os.path.join(os.getcwd(), 'network')
        os.mkdir(self.test_env)

        self.test_repo = os.path.join(self.test_env, 'test_repo')
        os.mkdir(self.test_repo)
        self.server = 'https://nerobp.xyz/gogs/api/v1/user/repos'

    def tearDown(self):
        shutil.rmtree(self.test_env)
        requests.delete('https://nerobp.xyz/gogs/api/v1/repos/test_user/' + self.test_repo.replace('/', '_'), auth=('test_user', 'cisco123'))


    def test_add_remote_repository(self):
        """Self-explanary
        """
        #Without password
        repo_url = "https://github.com/henriknero/Realtid_Projekt"
        repo_name = os.path.basename(repo_url)
        gitcom.add_remote_repository(repo_url, os.path.join(self.test_env, repo_name))
        #With Password
        repo_url = "https://gitlab.com/backup-project/backup_client.git"
        repo_name = os.path.basename(repo_url)

    def test_create_new_repo(self):
        gitcom.create_new_repository(self.test_repo, ('test_user','cisco123'))


if __name__ == '__main__':
    unittest.main()

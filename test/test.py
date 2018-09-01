import unittest
import os
import sys
import shutil
import requests

sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backup_client.filehandler import observer
from backup_client.network import gitcom

CREDENTIALS = ("test_user", "cisco123")
REPO = "test_repo"
SERVER_ADDRESS = "https://www.nerobp.xyz/gogs"

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_observer = observer.FileObserver('test_user', 'cisco123')
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

        self.test_env = os.path.join(os.getcwd(), 'network')
        if not os.path.isdir(self.test_env):
            os.mkdir(self.test_env)

        self.test_repo = os.path.join(self.test_env, REPO)
        os.mkdir(self.test_repo)

        self.remote_repo = os.path.join(self.test_env, "remote_repo")
        os.mkdir(self.remote_repo)

    def tearDown(self):
        shutil.rmtree(self.test_repo)
        shutil.rmtree(self.remote_repo)
        requests.delete(os.path.join('https://nerobp.xyz/gogs/api/v1/repos/', CREDENTIALS[0], REPO), auth=CREDENTIALS)


    def test_1_create_new_repo(self):
        repo = gitcom.create_new_repository(self.test_repo, REPO, CREDENTIALS)
        assert repo.workdir == self.test_repo + "/"
        assert repo.remotes[0].url == os.path.join(SERVER_ADDRESS, CREDENTIALS[0], REPO) + ".git"

    #This test depends on test_1 which is not good but I dont care
    def test_2_add_remote_repository(self):
        gitcom.create_new_repository(self.test_repo, REPO, CREDENTIALS)
        repo = gitcom.add_remote_repository(self.remote_repo, REPO, CREDENTIALS)
        assert repo.workdir == self.remote_repo + "/"
        assert repo.remotes[0].url == os.path.join(SERVER_ADDRESS, CREDENTIALS[0], REPO)

    def test_commit_and_push(self):
        pass


    def test_pull(self):
        pass
        #Dunno how to test... Its stolen so it probably work
    def test_push(self):
        pass
        #Also stolen, not gonna test atm
    def get_reponame_from_path(self):
        pass

if __name__ == '__main__':
    unittest.main()

# Git Backup Client
This a backup_client that monitors folders for changes and automatically backups to a git-server running Gogs. The current setup I use for the server can be found in my repo [gogs-container](https://github.com/henriknero/gogs-container).

The client uses python modules that are compatible with both Windows and Linux so it should be possible to run on both platforms. In the current version (0.4) the program is not verified to be working on Windows. ?

## Prerequisite
* libgit2
* pygit2 v0.27.3
* wxPython 4.0.3

On ubuntu it is possible to install wxPython using 
```
sudo apt-get install python3-wxgtk4.0
```
At the time of testing "apt-get" downloads libgit2 0.26 which is not compatible with pygit2 v0.27.3. To install the correct version use the following:
```
wget https://github.com/libgit2/libgit2/archive/v0.27.0.tar.gz
tar xzf v0.27.0.tar.gz
cd libgit2-0.27.0/
cmake .
make
sudo make install
```
## Install
In the root directory of the repository run the following:
```
pip3 install -r requirements.txt
python3 setup.py install
```
## Contribute
### Install virtual environment
In the root of the repository do the following
```
python3 -m venv venv
source venv/bin/activate
```
Installing pygit2 library locally in virtual environment, the guidelines follow the guide at https://www.pygit2.org/install.html. If these does not work see if the site has updated.
```
export LIBGIT2=$VIRTUAL_ENV
wget https://github.com/libgit2/libgit2/archive/v0.27.0.tar.gz
tar xzf v0.27.0.tar.gz
cd libgit2-0.27.0/
cmake . -DCMAKE_INSTALL_PREFIX=$LIBGIT2
make
sudo make install

export LDFLAGS="-Wl,-rpath='$LIBGIT2/lib',--enable-new-dtags $LDFLAGS"
export LD_LIBRARY_PATH=$LIBGIT2/lib
```
The three Environment variables has to be manually set every time you go in to the environment.
```
export LIBGIT2=$VIRTUAL_ENV
export LDFLAGS="-Wl,-rpath='$LIBGIT2/lib',--enable-new-dtags $LDFLAGS"
export LD_LIBRARY_PATH=$LIBGIT2/lib
```

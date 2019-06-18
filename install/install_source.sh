#!/bin/bash

# load configuration
RUNDIR=$(dirname $0)
source $RUNDIR/install.cfg



# A - Ideal Solution - new baseplate supporting apache thrift, avoid fbthrift
git clone https://github.com/apache/thrift.git
cd thrift
git checkout v0.12.0
./bootstrap
./configure
make
sudo make install

git clone https://github.com/reddit/baseplate.git
cd baseplate
git checkout v0.28.7
make
sudo make install

# function clone_repo {
#     local destination=$REDDIT_SRC/${1}
#     local repository_url=https://github.com/${2}.git

#     if [ ! -d $destination ]; then
#         sudo -u $REDDIT_USER -H git clone $repository_url $destination
#     fi
# }

# function install_repo {
#     pushd $REDDIT_SRC/$1
#     sudo -u $REDDIT_USER python setup.py build
#     python setup.py develop --no-deps
#     popd
# }

# clone_repo i18n reddit-archive/reddit-i18n
# install_reddit_repo i18n





# TODO - need to install fbthrift before installing baseplate
# fbthrift needs mstch
# git clone https://github.com/no1msd/mstch
# cd mstch
# mkdir build
# cd build
# cmake ..
# make
# make install
# cd ../..

# # Update to the latest stable from https://download.libsodium.org/libsodium/releases/
# wget https://download.libsodium.org/libsodium/releases/libsodium-stable-2019-03-02.tar.gz
# tar -xzf libsodium-stable-2019-03-02.tar.gz
# cd libsodium-stable
# ./configure
# make && make check
# sudo make install
# cd ..

# git clone https://github.com/facebookincubator/fizz.git
# cd fizz
# mkdir _build && cd _build
# cmake ../fizz
# make -j $(nproc)
# sudo make install

# git clone https://github.com/facebook/wangle.git
# cd wangle/wangle
# cmake .
# make
# ctest
# sudo make install

# git clone https://github.com/facebook/zstd.git
# cd zstd
# make
# sudo make install

# git clone https://github.com/facebook/folly.git
# cd folly
# # change to 
# git checkout v2018.12.31.00
# mkdir _build && cd _build
# cmake ..
# make -j $(nproc)
# sudo make install
# cd ../..

# git clone https://github.com/facebook/fbthrift.git
# cd fbthrift
# mkdir build && cd build
# cmake ..
# make -j $(nproc)
# sudo make install
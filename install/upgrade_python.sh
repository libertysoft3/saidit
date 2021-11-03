#!/bin/bash

# python 2.7.6 to 2.7.18
apt install -y build-essential checkinstall python-dev libssl-dev libffi-dev libc6-dev libbz2-dev libreadline-gplv2-dev libncursesw5-dev
wget --no-check-certificate https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz
tar xzf Python-2.7.18.tgz
cd Python-2.7.18
# add --enable-optimizations for faster python but slow build
./configure --prefix=/usr/local --enable-unicode=ucs4 --enable-shared --with-system-expat --with-system-ffi --with-ensurepip=install
make -j $(nproc)
make install
echo '/usr/lib/python2.7/dist-packages' | sudo tee -a /usr/local/lib/python2.7/site-packages/dist-packages.pth
echo '/usr/local/lib/python2.7/dist-packages' | sudo tee -a /usr/local/lib/python2.7/site-packages/dist-packages.pth
ldconfig
source ~/.bashrc
cd ..
rm -rf Python-2.7.18*
python -m ensurepip --upgrade

# avoid having to uninstall and reinstall, was getting error "ImportError: cannot import name _AES" on "initctl emit reddit-start"
pip install --upgrade --force-reinstall pycryptodome


# verify upgrade success
# python --version
# python -c "import urllib3.contrib.pyopenssl; urllib3.contrib.pyopenssl.inject_into_urllib3();"
# python -c "import ssl; print(ssl.HAS_SNI)"
# python -c "import Crypto.Cipher.AES"
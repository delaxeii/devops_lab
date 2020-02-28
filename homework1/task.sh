#!/bin/bash

sudo yum -y install epel-release
sudo yum install git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel

git clone https://github.com/pyenv/pyenv.git
curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

#================= pyenv config =============
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi

source $HOME/.bashrc

#================ install python =============
pyenv install 3.7.6
pyenv install 2.7.17

sudo pip install virtualenv

pyenv virtualenv 3.7.6 env_3.7
pyenv virtualenv 2.7.17 env_2.7

#=============== activate python 3.7 =========
pyenv activate env_3.7

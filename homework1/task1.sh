#!/usr/bin/env python

sudo yum -y install epel-release
sudo yum install git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel

git clone https://github.com/pyenv/pyenv.git
curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi

source $HOME/.bashrc
pyenv install 3.7.6
pyenv install 2.7.17

# Commands needed for setup and troubleshooting

pyenv install 3.12.3 (for Python version 3.12.3)
pyenv global 3.12.3 (for Python version 3.12.3)
pip install virtualenv
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt

source ~/.profile
gpgconf --kill gpg-agent && gpg-agent --daemon

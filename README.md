# Enviroplus Monitor

https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-plus

## Requirements

### RPi Interfaces

Ensure I2C interface is activated.

### Pyenv

Install using

```sh
sudo apt-get update
sudo apt-get upgrade
sudo apt install git
sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev
curl https://pyenv.run | bash
```

Add the following lines to your ~/.bashrc, or ~/.zshrc,

```sh
export PATH="~/.pyenv/bin:~/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

## Running

### Create Virtual Environment

```sh
pyenv install 3.8.3
pyenv global 3.8.3
```

### Install Dependencies

```sh
# Create a virtual environment called enviroplus that is based on 3.8.3
pyenv virtualenv 3.8.3 enviroplus
# Install poetry into the enviroplus virtual env
pyenv activate enviroplus
python -m pip install poetry
# Check installed poetry version
poetry --version
# Leave the virtual env
pyenv deactivate
# Add the enviroplus virtual env to the globally available envs
pyenv global 3.8.3 enviroplus
# Check poetry still accessible
poetry --version
# That is poetry since 1.0.0
poetry config virtualenvs.in-project true
poetry install
```

```sh
# Install pre-commit into the enviroplus virtual env
pyenv activate enviroplus
python -m pip install pre-commit
# Leave the virtual env
pyenv deactivate
# As the enviroplus venv has already been added, it will work directly
pre-commit --version
```

Set up hooks for pre-commit, using

```sh
# in the top level folder
pre-commit install && pre-commit install -t pre-push
```

Run using,

```sh
chmod +x enviroplusmonitor/enviroplusmonitor.py
poetry run enviroplusmonitor/enviroplusmonitor.py
```

```sh
pip install nox
nox
```

If using a [DHT22 sensor](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup) need to also run

```sh
sudo apt install libgpiod2
```

Run using

```sh
pip install -r requirements.txt
python -m enviroplusmonitor
```

## Debugging

To debug install. See https://medium.com/python-pandemonium/debugging-an-inactive-python-process-2b11f88730c7

```bash
sudo apt-get install gdb python3-dbg
```

To find process use

```bash
ps -ef | grep python
```

To run debugger use

```bash
gdb python process_id
```

At gdb prompt type `py-bt`.


## References:

* Continuous Integration: https://realpython.com/python-continuous-integration/
* pytest-docker-tools:
* https://hynek.me/talks/python-foss
* Testing in Python: https://realpython.com/python-testing/
* fake-rpi


#
* https://docs.pytest.org/en/latest/capture.html
* https://docs.pytest.org/en/latest/tmpdir.html
* https://docs.pytest.org/en/latest/fixture.html
* https://docs.pytest.org/en/latest/goodpractices.html

pytest.fixture
unittest.mock

## Run script as service

Add following to `/etc/systemd/system`, using `sudo cp enviroplusmonitor.service /etc/systemd/system`.

```bash
[Unit]
Description=Enviro+ Monitor
After=multi-user.target

[Service]
User=pi
Group=pi
WorkingDirectory=/home/pi/enviroplus-monitor
Type=simple
ExecStart=/usr/bin/python -m enviroplusmonitor
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Activate service using

```bash
sudo chmod 644 /etc/systemd/system/enviroplusmonitor.service
sudo systemctl daemon-reload
sudo systemctl enable enviroplusmonitor.service
sudo systemctl start enviroplusmonitor.service
```

### Check status

```bash
sudo systemctl status hello.service
```

### Start service

```bash
sudo systemctl start hello.service
```

### Stop service

```bash
sudo systemctl stop hello.service
```

### Check service's log

```bash
sudo journalctl -f -u hello.service
```


import platform
platform.node()

import socket
socket.gethostname()

# To run in background use

```bash
nohup python -m enviroplusmonitor > enviroplusmonitor.log &
```

To debug

```

Difficult to maintain consistency.service
Deviations in the topics
Deviations in the messages
AsyncAPI - single source of truth
Lack of tool support -

AsyncAPI Toolkit - Xtext and Eclipse.

Buiding AsyncAPI with Mercure protocol (new)
API Platform for WebAI
@dunglas
Les-Tilleuls.coop
EventSource protocol SSE (HTTP connection which remains open)
HTTP2 supports passing of data (websocket obsolete in HTTP2&3)

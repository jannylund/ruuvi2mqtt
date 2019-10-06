# Minimal ruuvi2mqtt using python and hcitool

This is a simple proxy to pass ruuvi tag data forward to mqtt. It is tested on raspberry pi 3b and raspberry pi zero w, but should work on any linux machine with hcitool.

## Prerequirements

Assuming a standard raspbian image is in use, the following things need to be installed.

```
sudo apt-get install git python3-pip bluez bluez-hcidump
```

As we don't want to run python as root, let's loose up the requirements for hcitool.

```
sudo setcap 'cap_net_raw,cap_net_admin+eip' `which hcidump`
sudo setcap 'cap_net_raw,cap_net_admin+eip' `which hcitool`
```

# Setup

- Clone (or download) the repo.
- Install the python libs `make install`.

# Running

To test interactively, just run `SERVER=<mqtt-server-ip> make run`.

# Running as a service
To run as a service and allow autostart on reboot, first we need to install `supervisor`: 
```
sudo apt-get install supervisor
```

Then copy the file `supervisord.sample` into `/etc/supervisor/conf.d/ruuvi2mqtt.conf`
Edit the conf file and add the path to your `ruuvi2mqtt` folder as well as populate the ip if `SERVER=<mqtt-server-ip>`.

Finally we need to restart `supervisord` using `sudo service supervisor restart`. You can confirm after that `ruuvi2mqtt` started by looking at `sudo service supervisor status`.

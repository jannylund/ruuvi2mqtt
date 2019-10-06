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
- Install the python libs `make install`
- Make the initial configuration in `config.env` by copying `config.sample` to `config.env`

# Running

To test interactively, just run `make run`


# airglow-rpi-filterwheel

# Setup for Raspberry Pi
Install Raspberry Pi OS 32-bit

Switch from DHCPCD to NetworkManager

Enable SSH and Serial Port in Configuration

`sudo apt install xrdp`

`sudo adduser airglowrdp`

RDP to RPi need to be from a different user `airglowrdp` and not the default one `airglow`

Delete the command that use serial0 on RPi:

# For Serial Communication
`sudo nano /boot/cmdline.txt`

and ONLY delete `console=serial0,115200`, keep the rest of the line unchanged

Run:

`python3 main.py`

# For Network Communication
Run:

`python3 main_network.py`

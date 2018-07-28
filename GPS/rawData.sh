stty -F /dev/ttyS0 9600 cs8 -cstopb -parenb
stty -F /dev/ttyS0 -echo
sudo hexdump -C </dev/ttyS0

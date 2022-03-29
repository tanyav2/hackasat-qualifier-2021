#!/bin/bash

# ended up not using this in favor of the solve.py

# create a socket on the pseudo path
exec 3<>/dev/tcp/localhost/12345;
head -1 <&3 | (read a b c d; echo "$((a + c))") | awk '{print $0}' >&3;

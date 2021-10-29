#!/bin/bash

head -n 3 Tux.ppm > Tux.header
tail -n +4 Tux.ppm > Tux.body
# encrypt Tux.body with your ECB implementation, save the encrypted file as Tux.body.ecb
python3 P2.py
cat Tux.header Tux.body.gcm > Tux.gcm.ppm
cat Tux.header Tux.boby.gcm.dec > Tux.gcm.dec.ppm
#!/bin/bash

FILE_NAME=$1

head -n 3 "$FILE_NAME.ppm" > "$FILE_NAME.header"
tail -n +4 "$FILE_NAME.ppm" > "$FILE_NAME.body"
# encrypt Tux.body with your ECB implementation, save the encrypted file as Tux.body.ecb
python3 P2.py $FILE_NAME.body
cat "$FILE_NAME.header" "$FILE_NAME.body.enc" > "$FILE_NAME.enc.ppm"
cat "$FILE_NAME.header" "$FILE_NAME.body.dec" > "$FILE_NAME.dec.ppm"
#!/bin/bash
SCRIPT="clahe.py"
EXT="jpg"
OUTPUT="${SCRIPT%.*}"

for I in 0.05 0.1 0.5 1 2 5 10; do
	for J in $(seq -w 1 2 65); do
		python "${SCRIPT}" -i input.png -c ${I} -t ${J} ${J} -o "${OUTPUT}.c${I}t${J}.${EXT}"
	done
done

for I in $(seq -w 0.05 0.2 10); do
	for J in 1 4 9 16 32 64; do
		python "${SCRIPT}" -i input.png -c ${I} -t ${J} ${J} -o "${OUTPUT}.c${I}t${J}.${EXT}"
	done
done

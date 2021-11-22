#!/bin/bash
SCRIPT="${0%.*}.py"
EXT="png"
OUTPUT="${SCRIPT%.*}"
OUTPUTS=("${OUTPUT}-a.${EXT}" "${OUTPUT}-b.${EXT}" "${OUTPUT}-c.${EXT}" "${OUTPUT}-d.${EXT}" "${OUTPUT}-e.${EXT}")
OPTIONS=('' '-c 0.05 -t 3 3' '-c 0.5 -t 8 8' '-c 2 -t 16 16' '-c 6 -t 32 32')

for I in $(seq 0 $((${#OUTPUTS[@]} - 1))); do
	OPTION=${OPTIONS[${I}]}
	OUTPUT=${OUTPUTS[${I}]}
	python "${SCRIPT}" ${OPTION} -o "${OUTPUT}"
done

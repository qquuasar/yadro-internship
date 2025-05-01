#!/bin/bash
#скрипт, который передает файл и искомое слово как параметры
fileName="$1"
searchWord="$2"

grep -i "$searchWord" "$fileName"

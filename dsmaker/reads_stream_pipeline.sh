p=parameter.txt

python reads_stream.py $p | python reads_flatten.py $p | python reads_encode.py $p | python reads_compress.py

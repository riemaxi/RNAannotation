p = parameter.txt

python contigs_stream.py $p | python contigs_flatten.py $p | python contigs_encode.py $p | python contigs_compress.py > data/pre_dataset.txt

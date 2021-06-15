for f in *.out; do 
    mv -- "$f" "${f%.out}.webp"
done

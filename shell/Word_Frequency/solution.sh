# grep -oE '\b\w+\b' words.txt |sort |uniq -c |sort -nr|awk '{print $2, $1}'

awk '{for(i=1;i<=NF;i++) w[$i]++}END{for(k in w) print k,w[k]}' words.txt |sort -k2 -nr

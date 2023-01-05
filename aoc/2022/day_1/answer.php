<?php
$cal = [];
$fh = fopen('./c.txt', 'r');

while ($line = fgets($fh)) {

    $cal[] = (int) $line;
}

fclose($fh);

$a = array_chunk($cal, 3);
$a = array_map('array_sum', $a);
rsort($a);

echo $a[0] . "\n"; // 1st answer
echo array_sum(array_slice($a, 0, 3)) . "\n"; // 2nd answer

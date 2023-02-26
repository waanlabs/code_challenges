<?php
$lines = file('D:\projects\code-challenges\aoc\2022\day-1\puzzle-input.txt', FILE_IGNORE_NEW_LINES);

$calories_sum_list = array();
$calories_sum = 0;

foreach ($lines as $line) {
    if ($line !== '') {
        $calories_sum += (int) $line;
    } else {
        array_push($calories_sum_list, $calories_sum);
        $calories_sum = 0;
    }
}

array_push($calories_sum_list, $calories_sum);
rsort($calories_sum_list);

echo max($calories_sum_list) . "\n"; // 1st answer
echo array_sum(array_slice($calories_sum_list, 0, 3)) . "\n"; // 2nd answer

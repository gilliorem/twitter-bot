<?php

$file = "/var/www/html/twitter-bot/isConnected";
$current = "Un jour de plus sans être une énorme sans salope.";
$file_content = file_put_contents($file, $current);
echo($current);
error_reporting(E_ALL); ini_set("display_errors", 1);

?>
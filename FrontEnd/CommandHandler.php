<?php
$jsonOut = json_encode(array(
    "mode"=>"write",
    "group"=>$_GET["group"],
    "target"=> $_GET["target"],
    "data"=> $_GET["data"]
));

$host = "192.168.178.34";
$port = 12345;
$f = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_set_option($f, SOL_SOCKET, SO_SNDTIMEO, array('sec' => 1, 'usec' => 500000));
socket_connect($f, $host, $port);
socket_sendto($f, $jsonOut, strlen($jsonOut), 0, $host, $port);
socket_close($f);

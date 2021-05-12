<?php

$mode = $_GET["mode"];
if($mode == "read") {
    $string_out = json_encode(array(
        "mode"=>$mode,
        "group"=>$_GET["group"]
    ));
    echo json_encode(sendToServer($string_out, true));
} else if ($mode == "write") {
    $string_out = json_encode(array(
        "mode"=>$mode,
        "group"=>$_GET["group"],
        "target"=> $_GET["target"],
        "data"=> $_GET["data"]
    ));
    sendToServer($string_out);
} else die("Unknown mode");


function sendToServer($string_out, $receive=false) {
    $received = array();
    $servers = json_decode(file_get_contents(dirname(__FILE__)."/Controller-Server.json"), true) or die("Unable to open and read file!");
    foreach ($servers as $server) {
        $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
        socket_set_option($socket, SOL_SOCKET, SO_SNDTIMEO, array('sec' => 1, 'usec' => 500000));
        socket_connect($socket, $server["address"], $server["port"]);
        socket_sendto($socket, $string_out, strlen($string_out), 0, $server["address"], $server["port"]);
        if($receive) {
            $json_in = json_decode(socket_read($socket, 2048), true);
            $received = array_merge_recursive($received, $json_in);
        }
        socket_close($socket);
    }
    if($receive)
        return $received;
    else return array();
}

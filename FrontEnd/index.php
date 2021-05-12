<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Server Control</title>
    <link rel="stylesheet" href="main.css">
    <script defer src="msh-api.js"></script>
    <script defer src="msh-buildSite.js"></script>
</head>
<body>

<?php ?>
<!--?php
function parseBool($boo) {
    if(gettype($boo) == gettype(true))
        return $boo;
    return strtolower($boo) == "true";
}

function createSwitch($name, $state, $group, $target) {
    $checked = ($state ? 'checked' : '');
    echo "<div class='switchContainer'>";
    echo "<h3>".$name."</h3>";
    echo "<label class='toggle'>";
    echo "<input name='checkbox' type='checkbox' class='checkbox' onchange='sendControlData(\"".$group."\", \"".$target."\", this.checked)' ".$checked."/>";
    echo "<span class='slider round'></span></label></div>";
}

$jsonOut = json_encode(array(
    "mode"=>"read",
    "group"=>"all",
));
$host = "192.168.178.34";
$port = 12345;
$f = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_set_option($f, SOL_SOCKET, SO_SNDTIMEO, array('sec' => 1, 'usec' => 500000));
socket_connect($f, $host, $port);
socket_sendto($f, $jsonOut, strlen($jsonOut), 0, $host, $port);
$json_in = json_decode(socket_read($f, 2048), true);
socket_close($f);

foreach (array_keys($json_in) as $group) {
    foreach ($json_in[$group] as $switch) {
        createSwitch($switch['name'], parseBool($switch['state']), $group, $switch['id']);
    }
}

?>


</body>
</html>



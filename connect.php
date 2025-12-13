<?php
$host = "crossover.proxy.rlwy.net";
$user = "root";
$pass = "YVhiWDayyMuALJChfnhSaeOPmurKpFPq";
$db   = "railway";
$port = 23404;

$conn = new mysqli($host, $user, $pass, $db, $port);
if ($conn->connect_error) {
    die("Kết nối thất bại: " . $conn->connect_error);
}
?>


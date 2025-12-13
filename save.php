<?php
require "connect.php";

$content = mysqli_real_escape_string($conn, $_POST['content']);
$conn->query("INSERT INTO test_data (content) VALUES ('$content')");

header("Location: index.php");
?>


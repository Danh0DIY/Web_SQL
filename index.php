<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Test MySQL Railway</title>
</head>
<body>

<h2>Nhập dữ liệu</h2>
<form action="save.php" method="POST">
    <input type="text" name="content" required>
    <button type="submit">Lưu</button>
</form>

<h2>Dữ liệu trong MySQL</h2>
<?php
require "connect.php";
$result = $conn->query("SELECT * FROM test_data ORDER BY id DESC");
while ($row = $result->fetch_assoc()) {
    echo "<p>".$row['id']." : ".$row['content']."</p>";
}
?>

</body>
</html>


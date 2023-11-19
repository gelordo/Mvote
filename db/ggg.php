<?php
$servername = "localhost"; // Usually "localhost"
$username = "root";
$password = "";
$database = "mm";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Connected successfully";

// Perform your database operations here

// Close connection
$conn->close();
?>




<?php
$servername = "your_database_host";
$username = "your_username";
$password = "your_password";
$database = "your_database_name";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$database", $username, $password);
    // Set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully";

    // Perform your database operations here

} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

// Close connection (not strictly necessary with PDO)
$conn = null;
?>

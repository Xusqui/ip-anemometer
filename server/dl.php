<?php
/* Send an update file (a .zip) to the client, if it exists on the server and its md5 differs from
 * the one provided by the client (if any).
 */

require_once 'common.php';

if (!file_exists(CLIENT_UPDATE_FILENAME)) {
  exit;
}

$contents = file_get_contents(CLIENT_UPDATE_FILENAME);
$md5 = md5($contents);
if ($md5 === $_GET['md5']) {
  exit;
}

header('Content-Description: File Transfer');
header('Content-Type: application/octet-stream');
header('Content-Disposition: attachment; filename='.basename(CLIENT_UPDATE_FILENAME));
header('Expires: 0');
header('Cache-Control: must-revalidate');
header('Pragma: public');
header('Content-Length: ' . strlen($contents));

echo $contents;
?>
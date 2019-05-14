<?php

require '../MwrClient.php';

use Mwr\Client\MwrClient;

$client = new MwrClient('calc');

echo $client->add($_REQUEST['a'], $_REQUEST['b']);
echo '<br>';
echo $client->minus($_REQUEST['a'], $_REQUEST['b']);
echo '<br>';
echo $client->multiply($_REQUEST['a'], $_REQUEST['b']);
echo '<br>';
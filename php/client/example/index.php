<?php

require '../MwrClient.php';

use Mwr\Client\MwrClient;

echo (new MwrClient('calc'))->add($_REQUEST['a'], $_REQUEST['b']).'<br>';
echo (new MwrClient('calc'))->minus($_REQUEST['a'], $_REQUEST['b']).'<br>';
echo (new MwrClient('calc'))->multiply($_REQUEST['a'], $_REQUEST['b']).'<br>';
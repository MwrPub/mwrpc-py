<?php

require '../MwrClient.php';

use Mwr\Client\MwrClient;

echo (new MwrClient('calc'))->add($_REQUEST['a'], $_REQUEST['b']);
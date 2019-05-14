<?php
require '../MwrClient.php';
echo (new \Mwr\Client\MwrClient('calc'))->add($_REQUEST['a'], $_REQUEST['b']);
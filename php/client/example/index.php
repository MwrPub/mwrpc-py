<?php
require '../MwrClient.php';
echo (new \Mwr\MwrClient('calc'))->add($_REQUEST['a'], $_REQUEST['b']);
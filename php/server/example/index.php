<?php
define('MWR_PATH', __DIR__ . '/');
date_default_timezone_set('PRC');
require(MWR_PATH . '../MwrServer.php');

use Mwr\Server\MwrServer;

(new MwrServer())->run();
# Method Working Remotely

Yet Another RPC Framework :D

![GitHub](https://img.shields.io/github/license/mwr-wiki/method-working-remotely.svg?color=blue&style=flat-square)
![Packagist Version](https://img.shields.io/packagist/v/mwr-wiki/method-working-remotely.svg?color=orange&style=flat-square)

## PHP Version

> Server Side
* index.php

```php
<?php
define('MWR_PATH', __DIR__ . '/');
date_default_timezone_set('PRC');
require('[PATH_TO_MWR]/MwrServer.php');

use Mwr\Server\MwrServer;

(new MwrServer())->run();
```

* CalcMwr.php
```php
class CalcMwr
{
    public function add($a, $b)
    {
        return $a + $b;
    }
}
```
> Client Side

```php
use \Mwr\Client\MwrClient;

echo (new MwrClient('calc'))->add($_REQUEST['a'], $_REQUEST['b']);
```

## Python Version

> Client Side

```python

```
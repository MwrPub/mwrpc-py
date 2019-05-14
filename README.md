# Method Working Remotely

Yet Another RPC Framework :D

![GitHub](https://img.shields.io/github/license/mwr-wiki/method-working-remotely.svg?color=blue&style=flat-square)
![Packagist Version](https://img.shields.io/packagist/v/mwr-wiki/method-working-remotely.svg?color=orange&style=flat-square)
![PyPI](https://img.shields.io/pypi/v/method-working-remotely.svg)

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

> Install

```shell
pip install method_working_remotely
```

> Server Side 

```python
from method_working_remotely import MwrServer

server = MwrServer()

@server.func(endpoint='calc')
def add(a, b):
    return a + b

if __name__ == '__main__':
    server.run()
```

> Client Side

```python
from method_working_remotely import MwrClient

client = MwrClient(endpoint='calc')

print(client.add(1,2))
```
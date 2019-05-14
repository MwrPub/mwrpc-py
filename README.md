# Method Working Remotely

Yet Another RPC Framework :D

![License](https://img.shields.io/github/license/mwr-wiki/method-working-remotely.svg?color=blue&style=flat-square)
![GitHub release](https://img.shields.io/github/release/mwr-wiki/method-working-remotely.svg?logo=github&style=flat-square)
[![Composer](https://img.shields.io/github/release/mwr-wiki/method-working-remotely.svg?color=777bb3&label=composer&logo=php&style=flat-square)](https://packagist.org/packages/mwr-wiki/method-working-remotely)
[![PyPI](https://img.shields.io/pypi/v/method-working-remotely.svg?color=3776AB&logo=python&logoColor=white)](https://pypi.org/project/method-working-remotely/)

## PHP Version

> Install

Composer :

```text
{
  ...
  "require": {
    ...
    "mwr-wiki/method-working-remotely": "0.1.*"
    ...
  }
  ...
}
```

> Server Side

* index.php

```php
<?php

require "vendor/autoload.php";

define('MWR_PATH', __DIR__ . '/');
date_default_timezone_set('PRC');

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
<?php

require "vendor/autoload.php";

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

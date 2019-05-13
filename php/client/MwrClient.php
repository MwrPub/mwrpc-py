<?php

class MwrClient
{
    private $url;

    public function __construct($url = 'http://localhost/mwr')
    {
        $this->url = $url;
    }

    public function __call($name, $arguments)
    {

        $content = json_encode(['func' => $name, 'a' => $arguments[0], 'b' => $arguments[1]]);
        $params = ['http' => ['method' => 'POST', 'header' => ['User-Agent: MineBlog', 'CONTENT_TYPE: application/json'], 'content' => $content]];
        $ctx = stream_context_create($params);
        $fp = @fopen($this->url, 'rb', false, $ctx);
        if (!$fp) {
            die('Can\'t open');
        }
        $response = @stream_get_contents($fp);
        if ($response === false) {
            die('Can\'t get content');
        }
        return json_decode($response, true)['result'];
    }
}
<?php

namespace Mwr\Client;

class MwrClient
{
    private $url;
    const MWR_VER = '0.1.4';

    public function __construct($endpoint = 'mwr', $host = 'localhost', $port = 6495, $isHttps = false)
    {
        $scheme = $isHttps ? 'https://' : 'http://';
        $this->url = $scheme . $host . ':' . $port . '/' . $endpoint . '/';
    }

    public function __call($name, $arguments)
    {
        $content = json_encode(['param' => $arguments]);
        $params = ['http' => ['method' => 'POST', 'header' => ['MWR_VER: ' . self::MWR_VER, 'CONTENT_TYPE: application/json'], 'content' => $content]];
        $ctx = stream_context_create($params);
        $fp = @fopen($this->url . $name, 'rb', false, $ctx);
        if (!$fp) {
            die('Mwr Call Failed. Can\'t open endpoint');
        }
        $response = @stream_get_contents($fp);
        if ($response === false) {
            die('Mwr Call Failed. Can\'t get response content');
        }
        $json = json_decode($response, true);
        if (isset($json['result'])) {
            return $json['result'];
        } else {
            return null;
        }
    }
}
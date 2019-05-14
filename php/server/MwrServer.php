<?php

namespace Mwr\Server;

class MwrServer
{
    const MWR_VER = '0.1.4';

    public function run()
    {
        spl_autoload_register([$this, 'loadClass']);
        $request_url = $_SERVER['REQUEST_URI'];
        $position = strpos($request_url, '?');
        $request_url = ($position === false) ? $request_url : substr($request_url, 0, $position);
        $request_url = trim($request_url, '/');
        $url_array = explode('/', $request_url);
        $url_array = array_filter($url_array);
        $endpoint = ucfirst($url_array[0]);
        array_shift($url_array);
        $func_name = $url_array ? $url_array[0] : '';
        $content = file_get_contents('php://input');
        $request = json_decode($content, true);
        $param = $request['param'];
        $class_name = $endpoint . 'Mwr';
        if (!class_exists($class_name)) {
            header("Content-Type: application/json; charset=UTF-8");
            echo json_encode(['code' => -1, 'err' => 'endpoint not exists']);
            die();
        }
        if (method_exists($class_name, $func_name)) {
            $dispatch = new $class_name();
            try {
                $result = call_user_func_array([$dispatch, $func_name], $param);
                header("Content-Type: application/json; charset=UTF-8");
                echo json_encode(['code' => 0, 'result' => $result]);
            } catch (\ArgumentCountError $argumentCountError) {
                header("Content-Type: application/json; charset=UTF-8");
                echo json_encode(['code' => -3, 'err' => 'too few arguments']);
                die();
            }
        } else {
            header("Content-Type: application/json; charset=UTF-8");
            echo json_encode(['code' => -2, 'err' => 'method not exists']);
            die();
        }
    }

    private static function loadClass($class)
    {
        $classFile = MWR_PATH . 'mwr/' . $class . '.php';
        if (file_exists($classFile)) {
            include $classFile;
        }
    }
}
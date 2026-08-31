<?php
//configurações iniciais
define('BASE_DIR', dirname(__FILE__,2));
define('VIEW', BASE_DIR.'/miniMVC/View');
define('URL_BASE', '/miniMVC'); //fotos

$_ENV['db']['host'] = 'localhost';
$_ENV['db']['user'] = 'root';
$_ENV['db']['pass'] = '';
$_ENV['db']['database'] = 'mini_julian';
<!-- 
require_once('waf.php')

PHPCMS V9 \phpcms\base.php
PHPWIND8.7 \data\sql_config.php
DEDECMS5.7 \data\common.inc.php
DiscuzX2   \config\config_global.php
Wordpress   \wp-config.php
Metinfo   \include\head.php
-->

<?php

function customError($errno, $errstr, $errfile, $errline) {
	echo "<b>Error number:</b> [$errno],error on line $errline in $errfile<br />";
	die();
}

set_error_handler("customError", E_ERROR);
$getfilter="'|(and|or)\\b.+?(>|<|=|in|like)|\\/\\*.+?\\*\\/|<\\s*script\\b|\\bEXEC\\b|UNION.+?SELECT|UPDATE.+?SET|INSERT\\s+INTO.+?VALUES|(SELECT|DELETE).+?FROM|(CREATE|ALTER|DROP|TRUNCATE)\\s+(TABLE|DATABASE)";
$postfilter="\\b(and|or)\\b.{1,6}?(=|>|<|\\bin\b|\\blike\\b)|\\/\\*.+?\\*\\/|<\\s*script\\b|\\bEXEC\\b|UNION.+?SELECT|UPDATE.+?SET|INSERT\\s+INTO.+?VALUES|(SELECT|DELETE).+?FROM|(CREATE|ALTER|DROP|TRUNCATE)\\s+(TABLE|DATABASE)";
$cookiefilter="\\b(and|or)\\b.{1.6}?(=|>|<|\\bin\\b|\\blike\\b)|\\/\\*.+?\\*\\/|<\\s*script\\b|\\bEXEC\\b|UNION.+?SELECT|UPDATE.+?SET|INSERT\\s+INTO.+?VALUES|(SELECT|DELETE).+?FROM|(CREATE|ALTER|DROP|TRUNCATE)\\s+(TABLE|DATABASE)";
function DefendAttack($StrFiltKey, $StrFiltValue, $ArrFiltReq) {
	if(is_array($StrFiltValue)) {
		$StrFiltValue = implode($StrFiltValue);
	}
	if(preg_match("/".$ArrFiltReq."/is", $StrFiltValue)==1) {
		//slog("<br><br>操作IP: ".$_SERVER["REMOTE_ADDR"]."<br>操作时间: ".strftime("%Y-%m-%d %H:%M:%S")."<br>操作页面: ".$_SERVER["PHP_SELF"]."<br>提交方式: ".$_SERVER["REQUEST_METHOD"]."<br>提交参数: ".$StrFiltKey."<br>提交参数: ".$StrFiltValue);
		print "360WebSec notice: Illegal operation!";
		exit();
	}
}
//$ArrPGC = array_merge($_GET, $_POST, $_COOKIE);
foreach ($_GET as $key => $value) {
	DefendAttack($key, $value, $getfilter);
}
foreach ($_POST as $key => $value) {
	DefendAttack($key, $value, $postfilter);
}
foreach ($_COOKIE as $key => $value) {
	DefendAttack($key, $value, $cookiefilter);
}

if (file_exists(filename)) {
	# code...
}

function slog($logs) {
	$toppath = $_SERVER["DOCUMENT_ROOT"]."/log.htm";
	$Ts=fopen($toppath, "a+");
	fputs($Ts, $logs."\r\n");
	fclose($Ts);
}

?>
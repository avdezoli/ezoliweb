#!/usr/bin/env php
<?php
error_reporting(0);
function userinput($message){
  global $white, $bold, $greenbg, $redbg, $bluebg, $cln, $lblue, $fgreen;
  $yellowbg = "\e[100m";
  $inputstyle = $cln . $bold . $lblue . "[#] " . $message . ": " . $fgreen ;
echo $inputstyle;
}
function readcontents($urltoread){
  $arrContextOptions=array(
      "ssl"=>array(
            "verify_peer"=>false,
            "verify_peer_name"=>false,
        ),
    );
    $filecntns = file_get_contents($urltoread, false, stream_context_create($arrContextOptions));
    return $filecntns;
}
$rhversion = "2.0.0";
$white = "\e[97m";
$black = "\e[30m\e[1m";
$yellow = "\e[93m";
$orange = "\e[38;5;208m";
$blue   = "\e[34m";
$lblue  = "\e[36m";
$cln    = "\e[0m";
$green  = "\e[92m";
$fgreen = "\e[32m";
$red    = "\e[91m";
$magenta = "\e[35m";
$bluebg = "\e[44m";
$lbluebg = "\e[106m";
$greenbg = "\e[42m";
$lgreenbg = "\e[102m";
$yellowbg = "\e[43m";
$lyellowbg = "\e[103m";
$redbg = "\e[101m";
$grey = "\e[37m";
$cyan = "\e[36m";
$bold   = "\e[1m";
function ezoli_banner(){
  echo "\e[91;1m
                                \e[36m Web Attack\e[91m And\e[32m Site Scanning\e[91m


          ███████╗███████╗ ██████╗ ██╗     ██╗        ██╗    ██╗███████╗██████╗ 
          ██╔════╝╚══███╔╝██╔═══██╗██║     ██║        ██║    ██║██╔════╝██╔══██╗
          █████╗    ███╔╝ ██║   ██║██║     ██║        ██║ █╗ ██║█████╗  ██████╔╝
          ██╔══╝   ███╔╝  ██║   ██║██║     ██║        ██║███╗██║██╔══╝  ██╔══██╗
          ███████╗███████╗╚██████╔╝███████╗██║        ╚███╔███╔╝███████╗██████╔╝


\e[32m";
}
require 'functions.php';
echo $cln;
system("clear");
ezoli_banner();

echo "\n";
echo $yellow . " [1]  Web Scan and  Attacking\n$yellow [2]  IP Adress System\n$red [Q]  Quit! \n\n" . $cln;
userinput("Choose Any Scan OR Action From The Above List");
$start = trim(fgets(STDIN, 1024));

if (!in_array($start, array(
  '1',
  '2'
), true))
{
  echo $bold . $red . "\n[!] Invalid Input! Please Enter a Valid Option! \n\n" . $cln;
  goto askscan;
}
else {
  if ($start == "1"){
    thephuckinstart:
    echo "\n";
    userinput("Enter The Website You Want To Scan ");
    $ip = trim(fgets(STDIN, 1024));
    
    
    if (strpos($ip, '://') !== false)
      {
        echo $bold . $red . "\n[!] (HTTP/HTTPS) Detected In Input! Enter URL Without Http/Https\n" . $CURLOPT_RETURNTRANSFER;
        goto thephuckinstart;
      }
    elseif (strpos($ip, '.') == false)
      {
        echo $bold . $red . "\n[!] Invalid URL Format! Enter A Valid URL\n" . $cln;
        goto thephuckinstart;
      }
    elseif (strpos($ip, ' ') !== false)
      {
        echo $bold . $red . "\n[!] Invalid URL Format! Enter A Valid URL\n" . $cln;
        goto thephuckinstart;
      }
    else
      {
        echo "\n";
        userinput("Enter 1 For HTTP OR Enter 2 For HTTPS"); 
        echo $cln . $bold . $fgreen;
        $ipsl = trim(fgets(STDIN, 1024));
        if ($ipsl == "2")
          {
            $ipsl = "https://";
          }
        else
          {
            $ipsl = "http://";
          }
    scanlist:
    
        system("clear");
        echo $bold . $blue . "
          +--------------------------------------------------------------+
          +                  List Of Scans Or Actions                    +
          +--------------------------------------------------------------+
    
                $lblue Scanning Site : " . $fgreen . $ipsl . $ip . $blue . "
          \n\n";
        echo $yellow . " [1]  Start Scanning\n$yellow [2]  Dos Attack \n$red [Q]  Quit! \n\n" . $cln;
    askscan:
        userinput("Choose Any Scan OR Action From The Above List");
        $scan = trim(fgets(STDIN, 1024));
    
        if (!in_array($scan, array(
            '1',
            '2'
        ), true))
          {
            echo $bold . $red . "\n[!] Invalid Input! Please Enter a Valid Option! \n\n" . $cln;
            goto askscan;
          }
        else
          {
            if ($scan == "1")
              {
                $reallink = $ipsl . $ip;
                $lwwww    = str_replace("www.", "", $ip);
                echo "\n$cln" . $lblue . $bold . "Scanning started...\n";
                echo $blue . $bold . "Scanning site:\e[92m $ipsl" . "$ip \n";
                echo "\n\n";
                $urlgip    = "http://api.hackertarget.com/geoip/?q=" . $lwwww;
                $resultgip = readcontents($urlgip);
                $geoips    = explode("\n", $resultgip);
                foreach ($geoips as $geoip)
                  {
                    echo $bold . $lblue . "[İNFO]$green $geoip \n";
                  }
                echo $bold . $lblue . "[iNFO] " . $green ,"Site Title: " . $green;
                echo getTitle($reallink);
                echo $cln;
                $wip = gethostbyname($ip);
                echo $lblue . $bold . "\n[iNFO] " . $green ,"IP adrres: " . $green . $wip . "\n" . $cln;
                echo $bold . $lblue . "[iNFO] " . $green ,"Web Server: ";
                WEBserver($reallink);
                echo $lblue . $bold . "\n[iNFO] " . $green ,"Cloudflare: ";
                cloudflaredetect($lwwww);
                echo $lblue . $bold . "[iNFO] " . $green ,"Robots File: " , "\e[92m" . robotsdottxt($reallink) . $cln;
                echo "\n\n";
                echo $bold . $yellow . "[*] Scanning Complete. Press Enter To Continue OR CTRL + C To Stop\n\n";
                trim(fgets(STDIN, 1024));
                goto scanlist;
              }
              elseif ($scan == "2")
              {
                echo $bold . $lblue . "Website URL: " . $fgreen ;
                $url = trim(fgets(STDIN));
    
                echo $bold . $lblue . "Enter 1 For HTTP OR Enter 2 For HTTPS: ". $fgreen ;
                $cevap1 = trim(fgets(STDIN));
    
                echo $bold . $lblue . "How many threads: ". $fgreen ;
                $sayı = trim(fgets(STDIN));
    
                echo $bold . $lblue . "Delay interval: ". $fgreen ;
                $slep = trim(fgets(STDIN));
    
                echo $bold . $lblue . "Do you have proxy (n or 12.34.56.78:8000): ". $fgreen ;
                $proxy = trim(fgets(STDIN));
    
                $command = "python3 dos.py " . escapeshellarg($url) . " " . escapeshellarg($cevap1) . " " . escapeshellarg($sayı) . " " . escapeshellarg($slep) . " " . escapeshellarg($proxy);
    
                $output = [];
                $return_var = 0;
                exec($command, $output, $return_var);
    
                if ($return_var !== 0) {
                    echo "?" . implode("\n", $output);
                } else {
                    echo "!\n";
                    echo implode("\n", $output);
                }
              }
            }
          }
    
  }
  elseif ($start == "2"){
    echo "\n";
    echo $yellow . " [1]  IP tester\n$yellow [2]  Port tester\n$red [Q]  Quit! \n\n" . $cln;
    userinput("Choose Any Scan OR Action From The Above List");
    $start1 = trim(fgets(STDIN, 1024));

    if ($start1 == "1"){
      $pythonFilePath = 'ip.py';

      $descriptorspec = [
        0 => ["pipe", "r"],
        1 => ["pipe", "w"],
        2 => ["pipe", "w"]
      ];
  
      $process = proc_open("python3 " . escapeshellarg($pythonFilePath), $descriptorspec, $pipes);
  
      if (is_resource($process)) {
        echo "\n";
        echo $yellow . $bold . " [1] Find your IP\n";
        echo $yellow . $bold . " [2] Test IP for your local ip\n";
        echo $yellow . $bold . " [3] Test with 192.168.1.xxx\n";
        echo $red . $bold . " [Q] Quit!\n";
        echo "\n";
        userinput("Choose Any Scan OR Action From The Above List");
        $userInput = trim( fgets(STDIN));
        fwrite($pipes[0], $userInput . PHP_EOL);
        fclose($pipes[0]);
  
        $output = stream_get_contents($pipes[1]);
        fclose($pipes[1]);
  
        $error = stream_get_contents($pipes[2]);
        fclose($pipes[2]);
  
        proc_close($process);
  
      if ($output) {
          echo "!\n" . $output;
      }
      if ($error) {
          echo "?\n" . $error;
      }
      } else {
        echo "Süreç başlatılamadı.";
      }
    }
    
    
    elseif ($start1 == "2"){
      echo $bold . $lblue . "Enter the IP address to scan: " . $fgreen ;
      $port = trim(fgets(STDIN));
    
      echo $bold . $lblue . "Enter the start port: ". $fgreen ;
      $first = trim(fgets(STDIN));
    
      echo $bold . $lblue . "Enter the end port: ". $fgreen ;
      $last = trim(fgets(STDIN));
    
      $command = "python3 port.py " . escapeshellarg($port) . " " . escapeshellarg($first) . " " . escapeshellarg($last);
    
      $output = [];
      $return_var = 0;
      exec($command, $output, $return_var);
    
      if ($return_var !== 0) {
        echo "?" . implode("\n", $output);
      } else {
        echo "!\n";
        echo implode("\n", $output);
      }
    }
  }
}
?>

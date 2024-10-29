<?php
function getTitle($url) {
  $data = readcontents($url);
  $title = preg_match('/<title[^>]*>(.*?)<\/title>/ims', $data, $matches) ? $matches[1] : null;
  return $title;
}


function WEBserver($urlws){
  stream_context_set_default( [
    'ssl' => [
        'verify_peer' => false,
        'verify_peer_name' => false,
    ],
]);
  $wsheaders = get_headers($urlws, 1);
  if (is_array($wsheaders['Server'])) { $ws = $wsheaders['Server'][0];}else{
    $ws = $wsheaders['Server'];
  }
  if ($ws == "")
    {
      echo "\e[91mNot Detected\e[0m";
    }
  else
    {
      echo "\e[92m$ws \e[0m";
    }
}
function cloudflaredetect($reallink){

  $urlhh    = "http://api.hackertarget.com/httpheaders/?q=" . $reallink;
  $resulthh = file_get_contents($urlhh);
  if (strpos($resulthh, 'cloudflare') !== false)
    {
      echo "\e[91mDetected\n\e[0m";
    }
  else
    {
      echo "\e[91mNot Detected\n\e[0m";
    }
}
function robotsdottxt($reallink){
  $rbturl    = $reallink . "/robots.txt";
  $rbthandle = curl_init($rbturl);
  curl_setopt($rbthandle, CURLOPT_SSL_VERIFYPEER, false);
  curl_setopt($rbthandle, CURLOPT_RETURNTRANSFER, TRUE);
  $rbtresponse = curl_exec($rbthandle);
  $rbthttpCode = curl_getinfo($rbthandle, CURLINFO_HTTP_CODE);
  if ($rbthttpCode == 200)
    {
      $rbtcontent = readcontents($rbturl);
      if ($rbtcontent == "")
        {
          echo "Found But Empty!";
        }
      else
        {
          echo "\e[92mFound \e[0m\n";
          echo "\e[36m\n-------------[ contents ]----------------  \e[0m\n";
          echo $rbtcontent;
          echo "\e[36m\n-----------[end of contents]-------------\e[0m";
        }
    }
  else
    {
      echo "\e[91mCould NOT Find robots.txt! \e[0m\n";
    }
}
?>

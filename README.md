# ctfs

CTFメモ

### ジャンル別メモ
* [Pwn note](https://github.com/kobadlve/ctfs/blob/master/pwn.md)


# CTF関連サイト
* CTFtimes - https://ctftime.org/
* Pwnable - http://pwnable.kr/
* MMACTF - https://ctf.mma.club.uec.ac.jp/
* MAGURO - https://score.maguro.run/#/
* ksnctf - http://ksnctf.sweetduet.info/
* OverTheWire - http://overthewire.org/wargames/
* ReversingKr - http://reversing.kr/
* LSE CTF - https://ctf.lse.epita.fr/
* list
	* Pwnlist - http://pastebin.com/uyifxgPu
	* Crypto Challenges List(2015) (by eshiho) - http://pastebin.com/cSfZW2yX
	* Crypto Challenges List(2016) (by eshiho) - http://pastebin.com/28SrvQ9b
	* Web Challenges List 2016 (by 193s) - http://pastebin.com/6EH6X0yL
	* rev challenges list (by N4NU) - http://pastebin.com/q7LGi8w5

# Write up
* CTFs - https://github.com/ctfs
* p4 - https://github.com/p4-team/ctf

# 参考資料
## Pwn
* ももテク - http://inaz2.hatenablog.com/
* rop - https://www.slideshare.net/inaz2/rop-illmatic-exploring-universal-rop-on-glibc-x8664-ja
* rop-x86 - http://v0ids3curity.blogspot.jp/2013/07/some-gadget-sequence-for-x8664-rop.html
* bataさんスライド - https://speakerdeck.com/bata_24

## Reversing
* Malware Unicorn - Reverse Engineering Malware 101 Material
https://securedorg.github.io/RE101/
## Crypto

## Network

## Web

## Forensic

## Misc

## その他
* MMAToolsSWiki - https://wiki.mma.club.uec.ac.jp/CTF/Toolkit
* Assembly list - http://softwaretechnique.jp/OS_Development/Tips/IA32_Instructions/TEST.html

# Tools
## Pwn
* shellstorm - http://shell-storm.org/shellcode/
* libc db - http://libcdb.com/
* request bin - http://requestb.in/
* web decompile - https://retdec.com/decompilation/
* pwntools - https://github.com/Gallopsled/pwntools
* gdb-peda - https://github.com/zachriggle/peda
* rop - rp++, ROPgadget

## Reversing
* objdump
* readelf
* gdb
* strace, ltrace, ptrace
* IDA
* OllyDbg
* Immunity debug
* radare2
* Java
	* JAD
	* Java Decompiler
	* Procyon
	* Ref: http://code.google.com/p/umjammer/wiki/JavaReverseEngineering
* .NET Framework
	*	ILSpy
* for Android
	* apktool
	* smali/baksmali (逆アセンブラ)
	* dex2jar (Javaに変換して逆コンパイル可能に)
	* https://apkstudio.codeplex.com/ apkファイルを直接修正
	* https://bytecodeviewer.com
	* jadx

## Crypto
* mouse code - http://morsecode.scphillips.com/translator.html

## Network
* Wireshark
* netcat, socat
* nmap, zmap
* tcpdump
* tcpreplay
* tcprewrite
* ssldump
* ngrep
* tcptrace


## Web
* curl
* Fiddler
* nikto
* 各種ブラウザ（特にFirefox, Chrome)
* HTTP通信を覗くツール(Live HTTP Headers(Firefox)やWiresharkなど)
* mitmproxy
* JavaScript Debugger(FirefoxならFireBug, OperaならDragonFlyなど…)
* dotjs 特定ドメインにアクセス時に指定したJavaScriptを実行する
* jsdetox (JavaScript難読化解除)
* cadaver(ftp likeなWebDav Client)

## Forensic
* foremost
* PhotoRec/TestDisk
* OSFMount (WindowsでHDDイメージをマウントしたいとき
* The Sleuth Kit / Autopsy
* qemu-nbd
* kpartx
* 7zip
* zip repair zipファイルの復元
* http://sourceforge.net/projects/tcpxtract/ パケットキャプチャーからファイルを取り出す
* Volatility (システムメモリダンプ解析)
* analyzeMFT (NTFSのMFT解析)
* exiftool


## Misc
* 画像変換 - http://www.bannerkoubou.com/photoeditor/conversion

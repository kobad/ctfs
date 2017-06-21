
# 動的デバッグ環境

接続先の実行ファイルをgdbで見たい。

* main.sh - `gdbserver localhost:40800 ./ropasaurusrex`
* `socat tcp-listen:40801, reuseaddr,fork exec:"./main.sh"`
* Attack
  * `perl -e 'print "A"*128 ."BBBB"' | nc localhost 408001`
* vi cmd - `file ./ropasaurusrex \n target remote localhost:40800 \n c`
* `gdb ./ropasaurusrex -q -x cmd`


# 情報収集

* plt/got - `objdump -d -M intel file | grep "@plt>:" -A1`, `readelf -r`
* ropgadget - `gdb ropgadget`
* .data - `readelf -S file | fgrep .data`
* libc system offset - `$ldd file $objdump -d /lib/i386-linux-gnu/libc.so.6 | grep "system>:"`


# Register
## 汎用レジスタ
* EAX(アキュムレータレジスタ) - 演算の結果
* ECX(カウンタレジスタ) - ループのカウントなど
* EDX(データレジスタ) - 演算に用いるデータ
* EBX(ベースレジスタ) - アドレスのベース値
* ESI(ソースインデックスレジスタ) - 一部のデータ転送命令で、データの転送元を格納
* EDI(デスティネーションインデックスレジスタ) - 一部のデータ転送命令で、データの転送先を格納

## 特殊レジスタ
* EBP(ベースポインタレジスタ) - 現在のスタックフレームにおける底のアドレスを保持
* ESP(スタックポインタレジスタ) - 現在のスタックトップのアドレスを保持
* EIP(インストラクションポインタレジスタ) - 次に実行する命令のアドレス

## フラグ
* CF(キャリーフラグ) - 演算命令で桁上がりか桁借りが発生時にセット
* ZF(ゼロフラグ) - 操作結果が0の時セット
* SF(符号フラグ) - 操作結果が負の時セット
* DF(方向フラグ) - ストリームの方向を制御
* OF(オーバーフローフラグ) - 符号付き算術演算の結果がレジスタの格納可能範囲を超えた時セット

## セグメントレジスタ
* CS(コードセグメントレジスタ) - コードセグメントのアドレス
* DS(データセグメントレジスタ) - データセグメントのアドレス
* SS(スタックセグメントレジスタ) - スタックセグメントレジスタのアドレス
* ES(エクストラセグメントレジスタ) - エクストラセグメントのアドレス
* FS(Fセグメントレジスタ) - Fセグメント(2つ目の追加セグメント)アドレス
* GS(Gセグメントレジスタ) - Gセグメント(３つ目の追加セグメント)アドレス

# 記法
* b - byte - 8bit
* s - short(16bit整数) - single(32bit浮動小数点)
* w - word - 16bit
* l - long(32bit整数) - double(64bit浮動小数点)
* q - quad(64bit)
* t - 10byte - 80bit浮動小数点
* BYTE - 8bit
* WORD - 16bit
* DWORD - 32bit
* QWORD - 64bit

# 代表命令

* `mov dest, src` - dest = src
* `lea dest, src` - dest = srcAddress
* `xchg dest1, dest2` - xchange dest1 dest2
* `lodsb - lodsw - lodsd` - [DS:ESI]のメモリ内容を、(b, word, dword)バイト分(b)ALレジスタに読み込み、ESIレジスタをDFレジスタに基づいて読み込んだサイズ分加算・減算。
* `stosb` - ALレジスタの値を(b, word, dword)バイト分、[ES:ESI]メモリに書き込み、EDIレジスタをDFレジスタに基づいて読み込んだサイズ分加算・減算
* `push s r c` - argオペランドの値をスタックにpush. ESPレジスタの値をレジスタ幅分(32bit -> 4byte, 64bit -> 8byte)減算し、argオペランドをESPレジスタのさすスタックのトップに格納
* `pop dest` - スタックからargオペランドへpop. ESPレジスタの指すスタックのトップの値をargオペランドへ格納し、ESPレジスタの値をレジスタ幅分(32bit -> 4byte, 64bit -> 8byte)減算
* `add dest, src` - src = src + dest
* `sub dest, src` - src = src - dest
* `mul` - srcオペランドにEAXレジスタの値を乗算し、結果の上位４位バイトをEDXレジスタに格納し下位４バイトをEAXに格納
* `div src` - EDX:EAXの８バイトをsrcバイトの値で除算する。商をEAXレジスタに剰余をEDXレジスタに格納
* `inc dest` - dest++
* `dec dest` - dest--
* `cmp src1, src2` - 減算するが結果は破棄され、結果に伴ってフラグレジスタを変化させる。
* `shr/shl dest, count` - destオペランドcountオペランドで指定したビット数分、それぞれ左、右にビットシフトし、結果をdestに格納。
* `ror/rol dest, count` - destオペランドcountオペランドで指定したビット数分、ローテートさせ、結果をdestに格納。
* `xor dest, src` - dest xor src. xor eax eax で初期化
* `test src1, src2` - 論理積を取る。結果からフラグレジスタを変化
* `jmp arg` - フラグレジスタを参照して、分岐
* `call arg` - jmpの拡張。分岐後にret命令で戻れるように、callの次の命令アドレスを戻り先としてスタックに保存
* `ret` - call元の次の命令へと実行を戻す
* `leave` - データ転送命令。retとセットで使われる。retの前に呼ばれ、スタックポインタをベースポインタと同じ位置に戻し、ベースポインタを復元。`mov esp, edp, pop edp`と同じ動作。

# 分岐

* ZF = 0           : JE(jump if equal), JZ(jump if zero)
* ZF = 0           : JNE(jump if not equal), JNZ(jump if not zero)
* ZF = 0 && SF = OF: JG(jump if greater)
* SF <> OF         : L(jump if less)

# 呼び出し規約

* stdcall  - 後ろの引数からpushされ、返り値はeaxに格納
* cdecl    - 後ろの引数からpushされ、ESPレジスタの値を戻す処理が呼ばれて、返り値をeaxに格納
* fastcall - 左から右への引数リストで見つかる最初の 2 つの DWORD またはこれより小さい引数は、ECX および EDX レジスタに渡されます。他の引数はすべてスタック上で右から左へ渡されます。 ESPレジスタの値を戻す処理が呼ばれて、返り値をeaxに格納

# セキュリティ機構

* RELRO(RELocation ReadOnly) - データのどこにReadOnly属性をつけるか。checksecで調べる
  * No RERLO
  * Partial RELRO(Lazy)
  * Full RELRO(Now) - GOTOverWriteできない
* Stack Smash Protection - スタック上でのBOFを防ぐ。スタックフレームのローカル変数領域とSaved EBPの間にCanaryを挿入し、関数終了時に書き換えられてるかを判定して検出し強制終了。
  * Canaryの値は乱数。先頭がNULLバイトになるようにして、ローカル変数に置かれた文字列がNULLバイトで終わっていなかった時に、Canaryが流出するのを防ぐ。
  * -fno-stack-protector オプションで無効化
* NX bit(No eXecute bit), DEP(Data Execution Prevention) - メモリ上の実行する必要のないデータを実行不可能に設定して、不正に実行されるのを防ぐ。
  * -z execstack オプションで無効化
* ASLR(Address Layout Randomization) - スタックやヒープ、共有ライブラリなどをメモリに配置する際にアドレスの一部をランダム化しアドレス推測を困難にする。
  * OFF: sudo sysctl -w kernel.randomize_va_space=0
  * ON : sudo sysctl -w kernel.randomize_va_space=2
* PIE(Position Independent Executable) - 実行コード内のアドレス参照を全て相対アドレスで行い、実行ファイルがメモリのどこに置かれても実行できるようにコンパイルされたファイル。



# Return to PLT(Procedure Linkage Table)
PLTに書かれた短いコード片を関数として呼び出すと、動的リンクされたライブラリのアドレスを解決してライブラリ内の関数を実行してくれる。

# Return to libc
system関数などのlibc内の関数を呼び出す。

# ROP (Return Oriented Programming)
ret命令で終わる命令列の先頭へのジャンプを繰り返すことで、任意の命令列を実行させる


# メモリレイアウト

|name|exp|
|:--:|:--:|
|.text|アセンブリコード|
|.data|初期値有りデータ|
|.bss|初期値無しデータ|
|heap ↓|動的確保領域|
|shared object|共有オブジェクト(libc.so)|
|stack ↑|スタック領域|
|kernel-area|カーネルが使用|

`$gdb-peda vmmap`か、`cat /proc/$PPID/maps`で確認

`0x1000`倍数で確保される(ページ)。プロセス起動時にmmapで確保。

ユーザからは仮想メモリしか見れない。

ASLR(アドレス空間配置のランダム化.下位7bitランダム化)、PIE(位置独立実行形式.下位4bitランダム化)、NS(text領域以外の実行権限を落とす)の確認ができる。

外部ライブラリ(*.so)のアドレスを保存するテーブル(GOT)の権限を決めるのがRELRO

# ヒープ

malloc()でヒープ領域からメモリ確保、free()で解放。

利用中
```
prev_size
size
data - sizeが8の倍数になるようにパディング
```
sizeの下位３bit
1. PREV_INUSE - 直前チャンクが利用中かどうか
2. IS_MMAPED - mmapで確保されたアドレスかどうか
3. IS_NON_MAINARENA - メインのARENAから確保したかどうか

解放済み
```
prev_size
size
fd - 次のfree済みチャンクのアドレス
bk - 前のfree済みチャンクのアドレス
```

free()したときに、すぐ隣にfree済みチャンクがあれば結合

|P2|
|:--:|
|P|
|P->fd|
|P->dk|

free(P2)した時、P2とPを結合するためにPを一旦リストから外す(unlink. `P->fd->bk = P->bk, P->dk->fd = P->fd`)

## Use After free

1. new で確保(ptr)
2. delete - この時、バグでこのアドレスに読み書きができてしまうとする
3. new で確保(ptr2)。たまたまptrで確保したアドレスから確保
4. ptr2がオブジェクトなら仮想関数テーブル(vptr)を持っている
5. ptrがまだ利用可能で、ptrを書き換えるとvptrを変更できてしまう。

## Unlink Attack

ヒープBOF時に直下がfree済みチャンクの時、fd/dkメンバを上書きできる

* P->fd->bk == P
* P->bk->fd == P
の時、発動できる

## fastbins

高速化のためにデータサイズごとにリストを作る(8の倍数)

# スタック

## Stack BOF

* サイズ制限がなければ自由に上書きできる -> Return先も指定可

リターン先アドレス（例えばシェルコード）のアドレスを推測するには？

* nop-sled - shellcodeまでをnop(0x90)で埋めれば、nop-sledのどこかにたどり着けばshellcodeまでたどり着ける。
* ret2esp - jmp esp, call espなどを使いshellcodeを呼ぶ
* Stager - 短いアセンブリコードを送り込み、shellcodeを追加読み込みさせる

## スタック実行不可(NX) - stack,heap領域を実行不可にする

回避するには？？

書き込み可能な固定アドレスを作り、シェルコードを書き込み実行する。

ここでplt(外部関数アドレスを動的に求める機構)を使う。 -> ret2plt
* ret2plt - ret2pop(コード中のpopを呼び出す)を組み合わせるとret2pltを連続で呼べる
  * pedaで ropgadgetで見つかる

使いたい関数がpltにない場合 -> ret2libc

# テクニック
## ret2libc

libc内の関数オフセットはファイルでもメモリでも固定なので、ベースアドレスを加算されるだけ。

使いたい関数のオフセットを調べておき、あとはlibc.soの先頭アドレスに加算すれば良い。

* libc内の関数アドレス調査
  * ldd ropasaurusrex - libc path
  * objdump -d path2libc | grep "system>:"
* libc内の固定文字列調査
  * strings -tx /lib/i386-linux-gnu/libc.so.6 | grep 'bin/sh'

対象と自分の環境でアドレスが変わる場合は0x1000ごとにブルートフォース

ret2libcの対策としてASLR(アドレスのランダム化)

* ASLRの回避
  * GOTを利用。一度解決されたGOTには元の外部アドレスが書かれる。ここからlibcのベースアドレスを求め、オフセットを足して目的の関数を計算。

## ROP

.text内のコードの断片(rop gadget)を組み合わせていく。

ropgadgetの探索 -> rp++

.text内に、ropgadgetが少ない場合にlibc内のガジェットを利用もできる。

大量のBOF量が必要なので、-> stack pivot

* stack pivot
  * bss(適当なところ)にROPを読み込んで置いて、最後にleaveでbssへ飛ばして、bssをスタックとして続けていく。
  * off-by-one stack bof(1バイトしかbofしない)にも有効。

* __libc_csu_init - スタックからレジスタへ値を入れられる汎用ガジェット
* alarm(x) - exa/raxにropで任意の値を入れたい
  * alarm(x) -> alarm(0)と実行するとeax/raxにxが入る
* Repeat-code - サンドボックスによりシステムコールが制限されているケース
  * libcにある\xEB\xFEを活用し１バイトずつ特定していく
* One-gadget-RCE - libc内に自動的にexecve("/bin/sh",0,0)を呼ぶアドレスがあるx64のみ
* ROP発展
  * JOP - jumpをベースにしたROP
  * COP - callをベースにしたrop
  * SROP - シグナル割り込みからの復帰を使って、レジスタを書き換えropを簡略化
  * BROP - 手元にバイナリがない状態でのROP

GOT Overwrite
* 気をつける関数 - strlen(), strcmp, memcmp, atoi, strtol, free

libcオフセット特定
* http://libcdb.com/

その他
* ret2dl_runtime_resolve
* _IO_jump_t Overwrite
* ld specific ptr Overwrite
* canary brute force
* master canary forging
* partial Overwrite
* gmesg command

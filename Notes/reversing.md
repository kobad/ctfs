## Tools

* IDA
* OllyDbg
* Immunity debugger
* ILSpy
* PE
  * PEiD
  * PEView
  * lordPE
  * exeinfope
* bin Editor
  * Stirling
  * binText

## MFC

## パッキング
### UPX
独自にアンパッキング機能もあり、アンパックが可能なのであまり意味をなさない。アンパックできないように改造されている場合がある。

OllyDbgで最後のjmp命令にブレークポイントをつけて、trace overで進めると感染させずに、ほとんどのコードが解凍されアドレスリークが可能

PEP - パッキングされたエントリポイント

OEP - オリジナルエントリポイント


## Keygenの解析
1. スキャン - パッキングされているかどうか。パッキングされているとIATが壊される
2. APIの確認 - インポート情報からどんなAPIが使われるか確認し、APIからどんな動きをするプログラムなのか予測できる
3. ImageBaseの確認 - このアドレスからプログラムが始まる(基本的に400000番地)


TLS(Thread Local Storage)コールバック - プロセスが作成された時に、メインスレッドが初期化される前に実行されるコード. Data Directory にある.ここに任意のアドレスを入れておくと、実際のコードより先にそのアドレスに存在するコードが実行される。

違う値同士のxorには注意

答えのみでなく、過程・背景知識・作成者の意図を考えるのも重要

## アンチデバッグ

### 古典的なものはシグネチャで判定(デバッカー名)
### IsDebuggerPresent() - kernel32.dll
IsDebuggerPresent()でデバック中なら0以外を返す関数がある(Win32 API)がもう簡単に無力化される。ので、手動で実装した方が良い。
例
```
BOOL IsDebuggerPresent()
{
  BOOL bDebugging = FALSE;
  __asm
  {
    mov eax, dword ptr fs:[0x18] // TEB(Thread Environment Block)
    mov eax, dword ptr ds:[eax+0x30] // PEB(Process Environment block)
    movzx eax, byte ptr ds:[eax+2]
    mov bDebugging, eax
  }
  return bDebugging;
}
```
### NtQueryInformationProcess() - ntdll.dll
kernel32.dllのCheckRemoteDebugger()も同じ(中でNtQueryInformationProcessを呼ぶ)。

* デバッグポートを定期的に監視する
* Debug Object Handleを取得
* NoDebugInherit

### NtQueryObject
デバッグ中はカーネル内にDebugObject型のオブジェクトが生成される。NtQueryObject()で全てのオブジェクトを取得できるのでそこからDebugObjectを取得する

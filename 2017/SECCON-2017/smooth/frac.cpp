/*********************************************
 * 素因数分解
 *********************************************/
#include <iostream>  // for cout, cin
#include <stdio.h>   // for printf, scanf

using namespace std;

/*
 * 計算クラス
 */
class Calc
{
    // 宣言
    int a;

    public:
        // 素因数分解
        void decompositPrime(int a);
};

/*
 * 素因数分解
 */
void Calc::decompositPrime(int n)
{
    // 割る数の初期値
    a = 2;
    // √n ≧ a ( n ≧ a * a ) の間ループ処理
    while (n >= a * a) {
        // a で割り切れたら、a は素因数
        // そして、割られる数を a で割る
        // a で割り切れなかったら、 a を 1 増加させる
        if (n % a == 0) {
            printf("%d * ", a);
            n /= a;
        } else {
            a++;
        }
    }
    // 最後に残った n は素因数
    printf("%d\n", n);
}

/*
 * メイン処理
 */
int main()
{
    int  iNum;

    try
    {
        // 計算クラスインスタンス化
        Calc objCalc;

        while (1) {
            // 自然数入力
            cout << "自然数 ( 0 : 終了 )：";
            cin  >> iNum;
            if (cin.fail()) break;
            if (iNum < 1) break;

            // 素因数分解
            objCalc.decompositPrime(iNum);
        }
    }
    catch (...) {
        cout << "例外発生！" << endl;
        return -1;
    }

    // 正常終了
    return 0;
}

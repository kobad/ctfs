#! ruby -Ks

def gcd(a, b)
  a = -a if a < 0
  b = -b if b < 0
  while b > 0
    a, b = b, a % b
  end
  a
end

def f(x, a, n)
  (x * x + a) % n
end

def pollard_rho(n)
  print "rho"
  x = y = rand(n)     # 0≦x, y≦n-1
  a = 1 + rand(n-3)   # 1≦a≦n-3
  begin
    x = f(x, a, n)
    y = f(y, a, n)
    y = f(y, a, n)    # f() を2回適用する
    d = gcd(x-y, n)
  end until d > 1
  d
end

def factor(n)
  d = pollard_rho(n)
  print "#{d}"
  while n > d
    n /= d
    d = pollard_rho(n)
    print " * #{d}"
  end
end


print "start"
factor(149767527975084886970446073530848114556615616489502613024958495602726912268566044330103850191720149622479290535294679429142532379851252608925587476670908668848275349192719279981470382501117310509432417895412013324758865071052169170753552224766744798369054498758364258656141800253652826603727552918575175830897)

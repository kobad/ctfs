socat TCP-LISTEN:10001,reuseaddr,fork EXEC:"strace ./write432"

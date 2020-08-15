import sys, termios

# 標準入力のファイルディスクリプタ取得
fd = sys.stdin.fileno()

# 属性を取得 old は戻す用
old = termios.tcgetattr(fd)
new = old.copy()
# 設定を変更
new[3] &= ~termios.ICANON
new[3] &= ~termios.ECHO

try:
# 設定を反映
    termios.tcsetattr(fd, termios.TCSANOW, new)
    ch = sys.stdin.read(1)

finally:
# 設定を元に戻す
    termios.tcsetattr(fd, termios.TCSANOW, old)


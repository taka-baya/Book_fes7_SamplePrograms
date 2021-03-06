import numpy as np
x = np.array([2,1,0,30]) #入力
w = np.array([0.1,0.7,-0.6,-0.02]) #出力

y = np.sum(x*w) #ベクトルxとwの内積
print("y : {0}".format(y))

# 組み込み関数roundを利用することにより、
# yの計算結果を0か1で四捨五入
# ※Pythonの仕様により、0.5は0として四捨五入されます。
u = np.round(y) #θ

print("u : {0}".format(u)) #0 or 1
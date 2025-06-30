med = float(input('Uma distância em metros:'))
km = med / 1000
hm = med / 100
dam = med / 10
dm = med * 10
cm = med * 100
mm = med * 1000
print('Converção:')
print("{} km\n{} hm \n{} dam \n{} dm \n{:.0f} cm \n{:.0f} mm" .format(km, hm, dam, dm, cm, mm))
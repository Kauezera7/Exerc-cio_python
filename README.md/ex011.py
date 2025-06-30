lar = float(input('Largura da parede:'))
alt = float(input('Altura da parede: '))
area = lar * alt
tinta = area / 2
print('Sua parece tem a dimensão de {}x{} e sua área é de {}m\u00B2.' \
'\nPara pintar essa parede, você precisará de {}L de tinta.'
.format(lar, alt, area, tinta))

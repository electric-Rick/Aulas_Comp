
def esgotar_sol():
	t_inicial = 385*(10**24)
	t_1min = t_inicial*60
	t_1h = t_1min*60
	t_dia = t_1h*24
	t_ano = t_dia*365
	massa_solarkg = 2*(10**30)
	c = 300000**2
	energy_total = massa_solarkg*(c)
	result = 0 
	ano = 0
	while True:
		ano = ano + 1
		energy_total = energy_total - t_ano
		print(ano, 'anos')
		print(energy_total)
		if energy_total == 0:
			break
mc()

# Não, não devemos nos preocupar e nem com a geração futura, pois o sol terá massa o suficiente para se sustentar ainda durante bilhões de anos. 

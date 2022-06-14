import pandas as pd
from create_insert_sql import createInsertTable

def dataProcessing(csv_name, path, sheet):
    print('Reading file...')
    dataframe = pd.read_excel(path, sheet_name=sheet)

    print('Renaming columns...')
    dataframe.rename(columns = {'Jan':'01', 'Fev':'02', 
                        'Mar':'03', 'Abr':'04', 'Mai':'05', 'Jun':'06',  'Jul':'07', 'Ago':'08', 
                        'Set':'09', 'Out':'10', 'Nov':'11', 'Dez':'12'}, inplace = True)

    print('Unpivot dataframe...')
    dataframe = pd.melt(dataframe, id_vars=['COMBUSTÍVEL', 'ANO', 'REGIÃO', 'ESTADO'], 
                    var_name = 'MES', value_name = 'melt_total')
    
    print('Preprocessing dataframe...')
    dataframe.drop(dataframe.index[dataframe['MES'] == 'TOTAL'], inplace = True)

    dataframe['DATA'] = dataframe['MES'] + '-' + dataframe['ANO'].astype(str) 

    dataframe['DATA'] = pd.to_datetime(dataframe['DATA'])

    switchToUF = {
		"ACRE":"AC",
		"ALAGOAS":"AL",
		"AMAZONAS":"AM",
		"AMAPÁ":"AP",
		"BAHIA":"BA",
		"CEARÁ":"CE",
		"DISTRITO FEDERAL":"DF",
		"ESPÍRITO SANTO":"ES",	
		"GOIÁS":"GO",	
		"MARANHÃO":"MA",	
		"MINAS GERAIS":"MG",	
		"MATO GROSSO DO SUL":"MS",	
		"MATO GROSSO":"MT",	
		"PARÁ":"PA",	
		"PARAÍBA":"PB",	
		"PERNAMBUCO":"PE",	
		"PIAUÍ":"PI",	
		"PARANÁ":"PR",	
		"RIO DE JANEIRO":"RJ",	
		"RIO GRANDE DO NORTE":"RN",	
		"RONDÔNIA":"RO",	
		"RORAIMA":"RR",	
		"RIO GRANDE DO SUL":"RS",	
		"SANTA CATARINA":"SC",	
		"SERGIPE":"SE",	
		"SÃO PAULO":"SP",	
		"TOCANTINS":"TO"	
    }

    dataframe['uf'] = dataframe['ESTADO'].map(switchToUF)

    dataframe = dataframe.drop(labels=['REGIÃO', 'ANO', 'MES', 'ESTADO'], axis=1)
    
    dataframe['COMBUSTÍVEL'] = dataframe['COMBUSTÍVEL'].str.replace('(m3)',"",regex = False).str.strip().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    
    dataframe.rename(columns = {'COMBUSTÍVEL':'product', 'ESTADO':'uf', 'melt_total':'volume', 'DATA': 'year_month'}, inplace = True)

    dataframe['unit'] = 'm3'
    
    dataframe['volume'] = dataframe['volume'].fillna(0)
    
    print('Reordering columns...')
    dataframe = dataframe[['year_month','uf','product','unit','volume']]
    
    print('Saving csv file...')
    dataframe.to_csv(f'../assets/csv/{csv_name}.csv', index=False)

    print('Finished process!\n')

print('FUEL DATA')
dataProcessing('fuel', '../assets/vendas-combustiveis-m3.ods', 'DPCache_m3')
print('DIESEL DATA')
dataProcessing('diesel', '../assets/vendas-combustiveis-m3.ods', 'DPCache_m3_2')
createInsertTable('fuel')
createInsertTable('diesel')
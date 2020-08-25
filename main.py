import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('23082020.xlsx', 'Sheet1')

df.columns = df.columns.str.replace(' ', '_')
df.replace({'MCLAREN P23 QTR RH 23AE358CP': 'McLaren RQ RH'}, inplace = True)
df.replace({'MCLAREN P23 QTR LH 23AE357CP': 'McLaren RQ LH'}, inplace = True)
df.replace({'MCLAREN P23 LWR SPLIT FIXED LH 23AE005CP': 'McLaren SD LH'}, inplace = True)
df.replace({'MCLAREN P23 LWR SPLIT FIXED RH 23AE006CP': 'McLaren SD RH'}, inplace = True)
df.replace({'MCLAREN P23 ASSY WS 23AD832CP': 'McLaren WS'}, inplace = True)
df.replace({'MCLAREN P23 DOOR UPR RH 23AE288CP': 'McLaren SR RH'}, inplace = True)
df.replace({'MCLAREN P23 DOOR UPR LH 23AE287CP': 'McLaren SR LH'}, inplace = True)
df = df[df.columns[[0, 33, 2, 4]]]

#df.replace({'Tipo_de_Notificación': {'APROBADO': True, 'RECHAZO': False}}, inplace = True)
df_ens = df[df.Puesto_de_trabajo == '31ENSAM']
df_ins = df[df.Puesto_de_trabajo == '34INSPE']

df_ens.groupby(['Orden', 'Descripción_material']).Tipo_de_Notificación.value_counts(normalize = True)

df_ins.groupby(['Orden', 'Descripción_material']).Tipo_de_Notificación.value_counts(normalize = True)

table = pd.pivot_table(df_ins, index=['Descripción_material', 'Orden'],columns=['Tipo_de_Notificación'], values=['Tipo_de_Notificación'], aggfunc = {'value_counts'})

ax = table.plot(kind='bar', stacked = True, figsize=(10,7))
ax.legend(["Aprobado", "Rechazado"])

totals = []

for i in ax.patches:
    totals.append(i.get_height())

# set individual bar lables using above list
for i in ax.patches:
    
    ax.text(i.get_x()+.1, i.get_height()+.5, str(int(i.get_height())), fontsize=10, color='dimgrey')

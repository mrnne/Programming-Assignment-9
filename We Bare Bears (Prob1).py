import pandas as pd
M= {'Student':['Ice Bear','Panda','Grizzly'],
        'Math':[80,95,79]}
E= {'Student':['Ice Bear','Panda','Grizzly'],
        'Electronics':[85,81,83]}
G= {'Student':['Ice Bear','Panda','Grizzly'],
        'GEAS':[90,79,93]}
S= {'Student':['Ice Bear','Panda','Grizzly'],
        'ESAT':[93,89,88]}

math=pd.DataFrame(M,columns=['Student','Math'])
electronics=pd.DataFrame(E,columns=['Student','Electronics'])
geas=pd.DataFrame(G,columns=['Student','GEAS'])
esat=pd.DataFrame(S,columns=['Student','ESAT'])

wbb=pd.merge(math,electronics,how='inner', on='Student')
wbb2=pd.merge(wbb,geas,how='inner', on='Student')
wbb3=pd.merge(wbb2,esat,how='inner', on='Student')

longformat= wbb3.melt(id_vars=['Student'], var_name='Subject', value_name='Grades')
longformat2= longformat.sort_values('Student')



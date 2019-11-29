import pandas as pd

B1= {'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],
         'Dimension':['Length','Width','Height','Length','Width','Height'],
         'Value':[6,4,2,5,3,4]}

messy=pd.DataFrame(B1,columns=['Box','Dimension','Value'])
tidy=messy.pivot(index='Box',columns='Dimension',values='Value').reset_index()

hlw= tidy[['Height','Length','Width']].transpose().prod().tolist()

vlm= {'Box':['Box1','Box2'],
         'Volume':hlw}
volume=pd.DataFrame(vlm,columns=['Box','Volume'])

TidyVolume=pd.merge(tidy,volume,how='inner', on='Box')
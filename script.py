import pandas as pd
import os
try:
  df = pd.read_excel(r'./initial.xlsx')
  df = pd.DataFrame(df)
except:
  print('File not found')
  exit()
else:
  try:
        payment_amount = []

        for index,row in df.iterrows():
            if pd.notnull(row['credit']) and pd.notnull(row['debit']):
                diff = row['credit']-row['debit']
                if diff>0:
                    payment_amount.append(f'+{diff:.2f}')
                else:
                    payment_amount.append(f'{diff:.2f}')
            else:
                if pd.notnull(row['credit']):
                    payment_amount.append(row['credit'])
                elif pd.notnull(row['debit']):
                    payment_amount.append(f"-{row['debit']}")
                else:
                    payment_amount.append('0')

        df['payment_amount'] = payment_amount
        df['Total Amount Paid to ME A/c'] = payment_amount
        if os.path.exists('./files/final.xlsx'):
            os.remove('./files/final.xlsx')
            df.to_excel('./files/final.xlsx')
            print('File with same name overwritten successfully')
        else:
            df.to_excel('./files/final.xlsx')
            print('File created successfully')
  
  except:
      print('Something went wrong while processing the file')


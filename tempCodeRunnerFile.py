
                if pd.notnull(row['credit']):
                    payment_amount.append(f'+{diff:.2f}')
                elif pd.notnull(row['debit']):
                    payment_amount.append(f'{diff:.2f}')
                else:
                    payment_a
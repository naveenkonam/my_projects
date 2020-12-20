import pandas as pd

names = ['bob','jess','mary','john']
grades = [76,95,77,79]

Gradelist = zip(names,grades)

df = pd.DataFrame(data=Gradelist, columns = ['names','grades'])

writer = pd.ExcelWriter('/home/konam/Desktop/dataframe.xlsx',engine='xlsxwriter')

df.to_excel(writer,sheet_name='Sheet1')

writer.save()



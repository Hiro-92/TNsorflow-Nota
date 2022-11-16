import pandas as pd

df = pd.read_csv("accident_2015.csv")
king = df.groupby(['발생지시도'])['사망자수'].sum()
print(king)
# list = []

# for line in range:
#     if line.startwith('#'):
#         continue
#     print(line)
    
# m_data = line.split()
# print(m_data)

# fig = px.bar(df, x= '사망자수', y= '발생지시도', orientation='h')
# fig.show()
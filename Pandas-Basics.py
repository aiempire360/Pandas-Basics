import pandas as pd


df = pd.read_csv('ecommerce_sales_data.csv')

print(df)

print(df.head(10))

print(df.tail(10))

print(df.describe())

print(df.columns)

print(df.dtypes)

print(df.index)

print(df.Category.unique())

print(df.Category.value_counts())

print(df.columns)

print(df[["Year", "Category", "Units_Sold", "Revenue"]])

print(df)

print(df.Year > 2021)

print(df[df.Year < 2021])

print(df[df.Year >= 2021])

print(df[(df.Year > 2021) & (df.Year < 2024)])

print(df[df.Category == 'Books'])

print(df.describe())

print(df.Customer_Rating.min())

print(df.Customer_Rating.max())
print(df.Customer_Rating.mean())

print(df.Customer_Rating.std())

print(df.Customer_Rating.sum())
print(df.Customer_Rating.count())
print(df.Customer_Rating ==  df.Customer_Rating.max())
print(df.Customer_Rating == df.Customer_Rating.mean())

print(df[df.Customer_Rating ==  df.Customer_Rating.max()])

df["no_of_year_for_sale"] = df ["Year"].apply(lambda x : 2026 - x)
print(df)


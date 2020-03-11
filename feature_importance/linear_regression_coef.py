lr = LinearRegression()

# ...

plt.barh(X.columns, lr.coef_.flatten())
plt.xlabel('Вес признака')
plt.ylabel('Признаки')

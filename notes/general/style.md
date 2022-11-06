<pre>
# императивный стиль
target = []  # создать пустой список
for item in source_list:  # для каждого элемента исходного списка
    trans1 = G(item)  # применить функцию G()
    trans2 = F(trans1)  # применить функцию F()
    target.append(trans2)  # добавить преобразованный элемент в список
</pre>
<br>
<br>
<pre>
# функциональный стиль
# языки ФП часто имеют встроенную функцию compose()
compose2 = lambda A, B: lambda x: A(B(x))
target = map(compose2(F, G), source_list)
</pre>

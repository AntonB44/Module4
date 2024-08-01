def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()

#inner_function()
'''
В том случае, когда мы вызываем inner_function внутри test_function
ничего не происходит, потому что объемлющая функция не вызвана, она не выполняется.
Однако после вызова test_function внутри нее происходит вызов вложенной функции
inner_function и выводится на печать текст.
Но, если мы попытаемся вызвать вложенную функцию извне, python выдаст ошибку (скрин прикреплен к решению).
'''


def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()
# inner_function() -  попытка вызова вложенной функции вне 'test_function()' приводит к ошибке:
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

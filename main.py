from views import views

file = views.read_file('data.txt')
array = views.split_hours(file)
views.pay_employee(array)

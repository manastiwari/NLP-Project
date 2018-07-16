

import cgi
import cgitb
form=cgi.FieldStorage()
first_name=form.get_value('first_name').capitalize()
print("hello")
print(first_name)
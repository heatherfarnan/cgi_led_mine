#!/usr/bin/python37all

import cgi
datas = cgi.FieldStorage()
# s1 = datas.getvalue('slider1')

# with open('led-pwm.txt', 'w') as f:  
#   f.write(str(s1))

# datab = cgi.FieldStorage()
# b1 = datab.getvalue('option')

import json

s1 = datas.getvalue('slider1')
b1 = datas.getvalue('option')
data = {'slider1':s1, "option":b1}

with open('led-pwm_new.txt', 'w') as f:
  json.dump(data,f)

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/led-pwm_new.py" method="POST">')

print('  <input type="radio" name="option" value="a"> LED 1 <br>')
print('  <input type="radio" name="option" value="b"> LED 2 <br>')
print('  <input type="radio" name="option" value="c"> LED 3 <br><br>')

print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value="Change LED brightness">')
print('</form>')
print('Brightness = %s' % s1)
print('</html>')

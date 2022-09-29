import cgi, os, datetime, locale, io, sys
from pathlib import Path

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

myPath = str(Path(__file__).resolve().parent) + '//'

def makeFilename(dataString):
    return myPath + dataString + '.txt'


html = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>My Schedule</title>
<link rel="stylesheet" type="text/css" href="../style.css" />
</head>
<body>
<h2>my schedule</h2>
<p><a href="../index.html"> back </a></p>
%s
</body>
</html>
'''
#output = datetime.datetime.now()
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
d = datetime.date.today()
length = 10
output = '<table border="1">\n'
output += '<tr><th>day</th><th>schedule</th></tr>\n'

fs = cgi.FieldStorage()
dateGot = fs.getfirst('date')
scheduleGot = fs.getfirst('schedule')
if not dateGot is None:
  filename = makeFilename(dateGot)
  if scheduleGot is None:
    os.remove(filename)
  else:
    with open(filename, 'w', encoding='utf-8', newline='\n') as f:
      f.write(scheduleGot)

for i in range(length):
  filename = makeFilename(d.strftime('%Y%m%d'))
  if(os.path.isfile(filename)):
    with open(filename, 'r', encoding='utf-8') as f:
      schedule = '<p>' + f.read().replace('\n', '<br>') + '</p>'
  else:
    schedule = ''

  output += '<tr><th>' + d.strftime('%Y/%m/%d （%A）') + \
    '</th><td>' + schedule + '<a href="scheduleInput.py?date=' + \
    d.strftime('%Y%m%d') + '">Edit</a></td></tr>\n'
  d += datetime.timedelta(days=1)

output += '</table>'
print('Content-Type: text/html; charset=utf-8')
print(html % output)
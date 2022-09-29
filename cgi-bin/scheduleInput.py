
import cgi, io, os, sys
from pathlib import Path

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>My Schedule Edit</title>
<link rel="stylesheet" type="text/css" href="../style.css" />
</head>
<body>
<h2>my schedule input</h2>
<p><a href="scheduleMain.py"> back </a></p>

<form method="get" action="scheduleMain.py">
date: <input name="date" value="%s" readonly><br>
schedule: <textarea name="schedule"> %s</textarea><br>
<button type="submit"> Save </button>
</form>
</body>
</html>
'''

fs = cgi.FieldStorage()
dateGot = fs.getfirst('date')
filename = str(Path(__file__).resolve().parent) + \
  '\\' + dateGot + '.txt'
if(os.path.isfile(filename)):
  with open(filename, 'r', encoding='utf-8') as f:
    schedule = f.read()
else:
  schedule = ''

print('Content-Type: text/html; charset=utf-8')
print(html % (dateGot, schedule))
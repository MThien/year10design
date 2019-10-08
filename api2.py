import requests
import webbrowser
myfile = open("apisite.html", "w")
tag = input("Enter Your Clash Royale Player Tag: #")
headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImExZjQwMDQ4LWY5NmItNDg1MS1iNDhiLTYwNDQ1ZDhiNTdjYSIsImlhdCI6MTU2OTM0MjcyNSwic3ViIjoiZGV2ZWxvcGVyL2MyYjY1NmYzLWE4MGMtOWU4Mi03MTdmLTcwY2I2YWYwZjY3YSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI2OS43Ny4xNjAuMiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.eErRvzKaBIS1vfhw3qHtaQ8RJ4LSWMkspX7I723Lnuk4k4tosdHHtLPl8RbHrbdYjGUimOe4AOIVqVD6Zxekbw'
}
response = requests.get("https://api.clashroyale.com/v1/players/%23" + tag.upper(), headers=headers)

userdata = response.json()
king_tower = str(userdata['expLevel'])
player_name = (userdata['name'])
myfile.write("<h1>Clash Royale Statistics</h1>")
myfile.write("<p>Michael Thien</p>")
myfile.write("<p> King Tower Level: "+ king_tower + "</p>")
myfile.close()
filename = 'file:///Users/mikey.thien/Desktop/Year-10/Design/' + 'apisite.html'
webbrowser.open_new_tab(filename)
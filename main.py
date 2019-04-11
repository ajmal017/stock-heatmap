#!/usr/bin/python

import requests
from colour import Color
import os
import datetime
current_time = datetime.datetime.now().time()

start_time = "09:00" #UTC Times
end_time = "15:30"

start_hour = int(str(start_time)[:2])
start_min = int(str(start_time)[:5][-2:])

end_hour = int(str(end_time)[:2])
end_min = int(str(end_time)[:5][-2:])

pwd = os.path.dirname(os.path.realpath(__file__))

def heatmap():
    filename = pwd +'\\heatmap.php'
    print (filename)
    f = open(filename, "w")

    #Initializing JSON

    positions = requests.get('https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/foSecStockWatch.json').json()
    
    endp = len(positions['data'])
    

    #Counting Colours
    positive_stocks=0
    i=0
    for x in range(i, endp):
        value = float(positions['data'][x]['per'])
        if value >= 0 : positive_stocks = positive_stocks+1
    negative_stocks = endp-positive_stocks
    
    # Initializing Colours
    positive_colors = list(Color("green").range_to(Color("#BDD051"),positive_stocks))
    negative_colors = list(Color("#DFA4A4").range_to(Color("red"),negative_stocks))

    #HTML Output
    f = open(filename, "a")
    f.write("<table>\n    <tbody>\n       <tr>")
    i,j,k=0,0,0
    for x in range(i, endp):
        symbol = positions['data'][x]['symbol']
        value = float(positions['data'][x]['per'])
        if (i!=0 and i%13 == 0) : f.write("</tr>\n<tr>")
        if value >= 0 :
            f.write('<td style="background: '+str(positive_colors[j])+'; ">'+symbol+'<br/><div class="per">'+str(value)+'%<div></td>')
            j = j+1
        else :
            f.write('<td style="background: '+str(negative_colors[k])+'; ">'+symbol+'<br/><div class="per">'+str(value)+'%<div></td>')
            k=k+1
        i=i+1

    f.write("</tr>\n    </tbody>\n       </table>")
    f.write("Last Updated at "+str(current_time)+".")
    print("Last Updated at "+str(current_time)+".")
    f.close()


    import ftplib
    session = ftplib.FTP('host','usernaem','password')
    file = open(filename,'rb')                  # file to send
    session.storbinary('STOR heatfno200.php', file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()

def job ():
    print(current_time)
    if (current_time.hour>start_hour and current_time.hour<end_hour) : heatmap()
    elif (current_time.hour==start_hour and current_time.minute>=start_min)  :  heatmap()
    elif (current_time.hour==end_hour and current_time.minute<=end_min)  :  heatmap()
    else : pass

job()


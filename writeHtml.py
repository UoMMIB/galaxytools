import pandas as pd

def writeHtml(df, orphan):
   df =pd.DataFrame(df, columns = ['plate' , 'part'])
   output =[]
   df=df.sort_values(by=['part'])
   outF = open("selectPlates.html", "w")
   outF.write("<!DOCTYPE html>\n"+
   "<html>\n"+
   "  <head>\n"+
   "    <title>Window title of the page</title>\n"+
   " <style>\n"+
   "     * {\n"+
   "         box-sizing: border-box;\n"+
   "     }\n"+
   " 	div {\n"+
   "         padding: 10px;\n"+
   "         background-color: #f6f6f6;\n"+
   "         overflow: hidden;\n"+
   "     }\n"+
   " 	input[type=text], textarea, select {\n"+
   "         font: 17px Calibri;\n"+
   "         width: 100%;\n"+
   "         padding: 12px;\n"+
   "         border: 1px solid #ccc;\n"+
   "         border-radius: 4px;\n"+
   "     }\n"+
   "     input[type=button]{ \n"+
   "         font: 17px Calibri;\n"+
   "         width: auto;\n"+
   "         float: right;\n"+
   "         cursor: pointer;\n"+
   "         padding: 7px;\n"+
   "     }\n"+
   " </style>\n"+
   "  </head>\n"+
   "  <body>\n"+
   " <form action=\"action_form.php\" method=\"get\">\n")
   old=""
   outF.write("<p>the following parts were missing from the plate director: "+str(orphan)+"</p><br>\n")
   for index, row in df.iterrows():
      if row['part'] != old:
         if len(str(old)) != 0:
                 outF.write("</select><br>\n")
         output.append(str(row['part']))
         outF.write("<p>select plate for part: "+str(row['part'])+"</p>")
         old = row['part']
         #outF.write("<input type = \"text\" list = \""+str(row['part'])+"\" name=\""+str(row['part'])+"\">\n" )      
         outF.write("<select id = \""+str(row['part'])+"\">\n")
         outF.write("  <option value = "+str(row['plate'])+">"+str(row['plate'])+"</option>\n")
      else:
         outF.write("  <option value = "+str(row['plate'])+">"+str(row['plate'])+"</option>\n")
      print(row['part'])
   outF.write("</select>")
   outF.write("<br>")
   outF.write("<input type=\"button\" id=\"bt\" value=\"Save data to file\" onclick=\"saveFile()\" />\n"+
   "</form>\n"+
   "</body>\n"+
   "    </html>\n"+
   "   <script> \n"+
   "  let saveFile = () => {\n")
   for x in output:
      outF.write("const "+str(x)+" = document.getElementById(\'"+str(x)+"\');\n")
   outF.write("\nlet data = \n")
   p=0
   for x in output:
      p =p+1
      if p ==0:
        outF.write("\\r")
      outF.write("\'"+str(x)+":,\'  + "+str(x)+".value");
      if p <len(output):
        outF.write(" + \' \\r\\n \' + \n")

   outF.write(";\n");
   outF.write("     const textToBLOB = new Blob([data], { type: \'text/plain\' });\n"+

   " const sFileName = \'formData.csv\';\n"+
   "     let newLink = document.createElement(\"a\");\n"+
   "     newLink.download = sFileName;\n"+
   "     if (window.webkitURL != null) {\n"+
   "         newLink.href = window.webkitURL.createObjectURL(textToBLOB);\n"+
   "     }\n"+
   "     else {\n"+
   "         newLink.href = window.URL.createObjectURL(textToBLOB);\n"+
   "         newLink.style.display = \"none\";\n"+
   "         document.body.appendChild(newLink);\n"+
   "     }\n"+

   "     newLink.click();\n"+ 
   " }\n"+
   " </script> \n"+
   " </html>");
   outF.close()


df= [["tap", "taper"], ["tap", "blah"], ["tap", "taper"], ["tap2", "taper"]]
orphan =""
writeHtml(df,"")


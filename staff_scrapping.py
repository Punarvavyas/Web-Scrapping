	
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup


# In[35]:


page_cs = requests.get("https://www.dal.ca/faculty/computerscience/faculty-staff.html")
page_be = requests.get("https://www.dal.ca/faculty/school-biomedical-engineering/our-people/our-faculty-atok.html")
page_ee = requests.get("https://www.dal.ca/faculty/engineering/electrical/faculty-staff.html")
print(page_cs.status_code)
print(page_cs.content)
soup_cs = BeautifulSoup(page_cs.content, 'html.parser') 
soup_be = BeautifulSoup(page_be.content, 'html.parser') 
soup_ee = BeautifulSoup(page_ee.content,'html.parser')


# In[126]:


proffesor_name = soup_cs.find_all('div', attrs={ "class" : "text parbase section"})
proffesor_detail= soup_be.find_all('div', attrs={ "class" : "text parbase section"})
proffesor_names=soup_ee.find_all('div',attrs={"class":"text parbase section"})
#print(proffesor_name)
file1 = open("cs.xml","w+") 
file2 = open("be.xml","w+")
file3=open("department.xml","w+")
xml_str = "<root>"

ctr=1
for ele in proffesor_name:
    links = ele.find_all('a')
#     print(links)
    for i, names in enumerate(links):
        if not '@' in names.text:
            if 'Dr' in names.text or 'Mr' in names.text: 
                print(names.text)
                xml_str = xml_str + "<record><field name=\"professor_id\">"+str(ctr)+"</field><field name=\"professor_name\">"+names.text+"</field><field name=\"professor_lname\">"+names.text.replace("Dr.","").split(" ")[2]+"</field><field name=\"iddepartment\">1</field></record>"
                ctr=ctr+1
xml_str+="</root>"
file1.write(xml_str)
                
file1.close()       
print ("endddddddddddd")   
xml_str = "<root>"
ctr=37
for ele in proffesor_detail:
    links = ele.find_all('a')
    
    for names in links:
        if not '@' in names.text:
            if not 'http:' in names.text and not 'www.' in names.text:
                print(names.text)
                xml_str = xml_str + "<record><field name=\"professor_id\">"+str(ctr)+"</field><field name=\"professor_name\">"+names.text+"</field><field name=\"professor_lname\">"+names.text.split(" ")[1]+"</field><field name=\"iddepartment\">2</field></record>"
                ctr=ctr+1
                

xml_str+="</root>" 
file2.write(xml_str)
                
file2.close() 
print("enddddddddddddddddddddddddddddddddd")    

file3.write("<root><record><field name=\"iddepartment\">1</field><field name=\"department name\">Computer_Science</field></record><record><field name=\"iddepartment\">2</field><field name=\"department name\">Biomedical engineering</field></record></root>")
file3.close()
for ele in proffesor_names:
    links = ele.find_all('td')
    #print(links)
    #link_temp=links[5:]
    #print(link_temp)
    
    for names in links[5:-2]:
        
        if not '@' in names.text:
            if not '(902)' in names.text and not 'www.' in names.text:
                
                    print(names.text) 
                   # print("hi")
       


LOAD XML INFILE  'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/cs.xml'
    -> INTO TABLE faculty
    -> ROWS IDENTIFIED BY '<record>';
LOAD XML INFILE  'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/untitled1.xml'
    -> INTO TABLE faculty
    -> ROWS IDENTIFIED BY '<record>';
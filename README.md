# Introduction
This program is used to generate text from template. It will run python script between ```<py> </py>``` in template.

# Steps
1. Put your template in template.txt<br>
2. Put your data in data.py<br>
3. Execute generator.py<br>
<br>

#Example
template.txt:<br>
```
public class <py>print class_name,</py> implements Serializable {

  private static final String docType = <py>print '"'+doc_type+'";'</py>
<py>
for field in field_list:
    print "  private " + field[0] + " " + field[1] + ';\n',
</py>
```

data.py:<br>
```
class_name = 'AlEvent'
doc_type = 'alEvent'
field_list = [('int','eventId'),('String','stationName')]
```

Execution output:<br>
```
@Entity
public class  AlEvent  implements Serializable {

  private static final String docType =  "alEvent";
  private int eventId;
  private String stationName;
```

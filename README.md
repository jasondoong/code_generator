code_generator
==============

put your template in template.txt<br>
put your data in data.py<br>
then run generator.py<br>
<br>
template example:<br>
public class <py>print class_name,</py> implements Serializable {<br>
<br>
  private static final String docType = <py>print '"'+doc_type+'";'</py><br>
<py><br>
for field in field_list:<br>
    print "  private " + field[0] + " " + field[1] + ';\n',<br>
</py><br>


data example:<br>
class_name = 'AlEvent'<br>
doc_type = 'alEvent'<br>
field_list = [('int','eventId'),('String','stationName')]<br>

execution result:<br>
@Entity<br>
public class  AlEvent  implements Serializable {<br>
<br>
  private static final String docType =  "alEvent";<br>
  private int eventId;<br>
  private String stationName;<br>


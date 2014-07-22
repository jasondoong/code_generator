code_generator
==============

put your template in template.txt
put your data in data.py
then run generator.py

template example:
public class <py>print class_name,</py> implements Serializable {

  private static final String docType = <py>print '"'+doc_type+'";'</py>
<py>
for field in field_list:
    print "  private " + field[0] + " " + field[1] + ';\n',
</py>


data example:
class_name = 'AlEvent'
doc_type = 'alEvent'
field_list = [('int','eventId'),('String','stationName')]

execution result:
@Entity
public class  AlEvent  implements Serializable {

  private static final String docType =  "alEvent";
  private int eventId;
  private String stationName;


from student3 import Lab 
from student3 import LabMember
from student3 import Student
from student3 import Professor

jsk = Lab()
p1 = Professor("Yamada")
s1 = Student("Suzuki")
p1.set_room(123)
s1.set_grade(4)
jsk.add_member(p1)
jsk.add_member(s1)
s1.promotion()
p2 = Professor("Inaba")
s2 = Student("Kimura")
p2.set_room(122)
s2.set_grade(3)
jsk.add_member(p2)
jsk.add_member(s2)
s2.promotion()
jsk.print_member()

anohito = Lab()
p3 = Professor("Anohito")
s3 = Student("Konohito")
p3.set_room(111)
s3.set_grade(2)
anohito.add_member(p3)
anohito.add_member(s3)
s3.promotion()
p4 = Professor("Sonohito")
s4 = Student("Donohito")
p4.set_room(112)
s4.set_grade(5)
anohito.add_member(p4)
anohito.add_member(s4)
s4.promotion()
anohito.print_member()

##書き加えたコード
list_members = []
for member in jsk.members:
    list_members.append(member)
for member in anohito.members:
    list_members.append(member)
sorted_members = sorted(list_members)
for member in sorted_members:
    print(member)

x = 1

for interface in range (x,x+48):
  print "interface gigabitethertnet 0/%d" % interface
  print "switchport mode access"
  print "switchport access vlan 100"
  print "channel-group %d mode active" % x+1000
  


  

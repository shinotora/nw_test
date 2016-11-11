x = 1

for interface in range (x,x + 24):
  print "interface gigabitethertnet 0/%d" % interface
  print "switchport mode access"
  print "switchport access vlan 100"
  interface = interface + 1000
  print "channel-group %d mode active" % interface
  


  

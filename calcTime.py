date0 = input("Data inicial") 

date1 = input("Data Final");

 

 #Subtract

 diff = Math.abs(date0 - date1);

 

 #Use mod to find times

 ms = diff % 1000;

 diff = (diff - ms) / 1000

 ss = diff % 60;

 ss = ("0" + ss).slice(-2);

 diff = (diff - ss) / 60

 mm = diff % 60;

 mm = ("0"+mm).slice(-2)

 diff = (diff - mm) / 60

 hh = diff % 24;

 hh = ("0"+hh).slice(-2)

 

 return hh + ":" + mm + ":" + ss;


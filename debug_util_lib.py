import datetime

class debugger:

	debugLevel=0
	runtime=datetime.datetime.now()

	def __init__(self,*args):
		self.runtime=datetime.datetime.now()
		if len(args)==0:
			self.debugLevel=0
			return None
		elif args[0] in [0,1,2]:
			self.debugLevel=args[0]
		return None
		

	def setLevel(self, *args):
		if len(args)==0:
			prompt="Select debug level:\n  0: off\n  1: basic\n  2: verbose\nLevel: "
			input=raw_input(prompt)
			while input not in ["0","1","2"]:
				input=raw_input(prompt)
			self.debugLevel=int(input)
			self.out("Success; debug level set to %s." % self.debugLevel)
		elif args[0] in [0,1,2]:
			self.debugLevel=args[0]
			self.out("Success; debug level set to %s." % self.debugLevel)
		else:
			self.out("Invalid debug level")
			self.setLevel()
		return 0
		# input=raw_input("""Select debug level:
		# \t0: off
		# \t1: basic
		# \t2: verbose
		# Level: """)
		# while int(input) not in ['0','1','2']:
		# 	print ()
		# #debugMode=True
		# runtime=self.runtime	
		# print "#############################"
		# print "# DEBUG ENABLED @ LEVEL %s #" 
		# print "# %02d/%02d/%02d @ %02d:%02d:%02d    #" % (runtime.month, runtime.day, runtime.year, runtime.hour, runtime.minute, runtime.second)
		# print "#############################"

	def out(self,*args):
		if len(args)==0:
			return 0
		elif self.debugLevel==1:
			print args[0]
			return 0
		elif self.debugLevel==2:
			now=datetime.datetime.now()
			print "[%02d/%02d/%02d @ %02d:%02d:%02d] %s" % (now.month, now.day, now.year, now.hour, now.minute, now.second, args[0])
			return 0
		return 0
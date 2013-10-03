################################
################################
####PLEASE NOTE THAT THIS#######
###########IS NOT THE ##########
########MOST UPDATED ###########
#########VERSION OF THE#########
#######TERSE INTERPRETER########
################################
################################


text = "".join(open(raw_input("Filename? ")))
lines = text.split("\n")
executing = True
class Function:
	def __init__(self):
		self.text = list()
		self.args = list()
	def call(self, args):
		"""call the function"""
		if args:
			for arg in args:
				locs[self.args[args.index(arg)] = arg
		for line in self.text:
			execute(line)
def array_remove_element(array, element):
	new = list()
	for e in array:
		if not e == element:
			new.append(e)
	return new
inFunction = False
fName = str()
fargs = list()
array_remove_element(lines, '')
globs = dict()
locs = dict()
funcs = dict()
subs = dict()
stack = list()
prev = None
def val(word):
	if word[0] == "@":
		return globs[word] or ""
	elif word[0] == "$":
		return locs[word] or ""
	elif word == "read":
		return f.read()
	elif word == "in":
		return raw_input("")
	elif word == "<>":
		return "\n"
	elif word == "pop":
		return stack.pop()
	else:
		try:
			return eval(word)
		except Exception:
			return word
def decl(args):
	#Declare a global variable
	globs[args[0].replace("&", "@")] = True
def push(args):
	stack.append(prev)
def pop(args):
	return stack.pop()
def out(args):
	narg = list()
	for arg in args:
		print str(arg).replace("_", " ").replace("\"", ""),
def add(args):
	global prev
	prev = sum(map(int, args))
def sub(args):
	global prev
	prev = args[0] - args[1]
def mult(args):
	global prev
	prod = 1
	for a in args:
		prod *= int(a)
	prev = prod
def div(args):
	global prev
	prev = args[0] / args[1]
def mod(args):
	global prev
	prev = args[0] % args[1]
def string(phrase):
	phrasel = list(phrase)
	nphrasel = list()
	inQuote = False
	for l in phrasel:
		if l == "\"":
			inQuote = not inQuote
		if l == " " and inQuote:
			nphrasel.append("_")
		else:
			nphrasel.append(l)
	return "".join(nphrasel)
def eq(args):
	return args[0] == args[1]
def lt(args):
	return args[0] < args[1]
def gt(args):
	return args[0] > args[1]
def execute(linet):
	global fName
	global funcs
	line = array_remove_element(linet.split("\t"), "")
	command = line[0]
	if command in subs:
		#Calling a subroutine (takes no arguments)
		subs[command].call(None)
		return
	if command == "push":
		push(prev)
		return
	args = string(line[1]).split(" ")
	for arg in args:
		args[args.index(arg)] = val(arg)
	if command[0] == "@":
		#We are defining a global variable
		globs[command] = args[0]
		return
	if command in funcs:
		#Calling a function
		funcs[command].call(args)
		return
	if command in ("eq", "lt", "gt"):
		global executing
		#Conditional statement!
		executing = eval(command)(args)
	if command == "func":
		#define a function
		global fName
		global inFunction
		inFunction = True
		global fargs
		fName = args.pop(0)
		if len(args) > 0:
			fargs = [arg.replace("&", "$") for arg in args]
			funcs[fName] = Function()
			funcs[fName].args = fargs
		else:
			subs[fName] = Function()
			subs[fName].args = fargs
		return
	eval(command)(args)
for line in lines:
	if line == "end":
		executing = True
		continue
	if line and line[0] != ";":
		if executing:
			#Either no if block, or condition is true
			if not inFunction:
				try:
					execute(line)
				except Exception as e:
					#report errors with line numbers
					print "Error @ line ", lines.index(line) + 1
					print e
					raise SystemExit()
			else:
				#adding lines to a function
				if line != "end":
					#still inside function body
					try:
						funcs[fName].text.append(line)
					except KeyError:
						#No function of that name, try it in Subroutines!
						subs[fName].text.append(line)
				else:
					#Line is "end", exit function!
					inFunction = False

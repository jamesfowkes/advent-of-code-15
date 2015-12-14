import sys
import pprint

UNARY_OPS = ["NOT"]
BINARY_OPS = ["AND", "OR", "LSHIFT", "RSHIFT"]

pp = pprint.PrettyPrinter(indent=4)

class Instruction:

	NULLARY = 0
	UNARY = 1
	BINARY = 2

	def __init__(self, ins, verbose = False):

		self.original_instruction = ins.strip()

		if any(op in ins for op in UNARY_OPS):
			self.optype = self.UNARY
		elif any(op in ins for op in BINARY_OPS):
			self.optype = self.BINARY
		else:
			self.optype = self.NULLARY
	
		self.parse_to_args()

		self.verbose = verbose

	@property
	def type(self):
	    return ["NULLARY", "UNARY", "BINARY"][self.optype]
	
	def parse_to_args(self):

		tokens = self.original_instruction.split(" ")
		if self.optype == self.NULLARY:
			try:
				self.input = [int(tokens[0])]
			except:
				self.input = [tokens[0]]

			self.operator = ""
			self.output = tokens[2]

		elif self.optype == self.UNARY:
			try:
				self.input = [int(tokens[1])]
			except ValueError:
				self.input = [tokens[1]]
			
			self.operator = tokens[0]
			self.output = tokens[3]
			
		elif self.optype == self.BINARY:
			self.input = [0, 0]
			try:
				self.input[0] = int(tokens[0])
			except ValueError:
				self.input[0] = tokens[0]

			try:
				self.input[1] = int(tokens[2])
			except ValueError:
				self.input[1] = tokens[2]
			
			self.operator = tokens[1]
			self.output = tokens[4]
		
	def __repr__(self):
		if self.optype == self.NULLARY:
			return "{} -> {}".format(self.input[0], self.output)
		elif self.optype == self.UNARY:
			return "{} {} -> {}".format(self.operator, self.input[0], self.output)
		elif self.optype == self.BINARY:
			return "{} {} {} -> {}".format(self.input[0], self.operator, self.input[1], self.output)
	
	def unaryop(self, signals):
		if self.operator == "NOT":
			self.input[0] = self.input[0] if type(self.input[0]) == int else self.input[0].run(signals) 
			return (~self.input[0] + 2**16)
		else:
			raise Exception("Unexpected unary operator {}".format(self.operator))

	def binaryop(self, signals):

		self.input[0] = self.input[0] if type(self.input[0]) == int else self.input[0].run(signals)
		self.input[1] = self.input[1] if type(self.input[1]) == int else self.input[1].run(signals)

		if self.operator == "AND":
			return self.input[0] & self.input[1]
		elif self.operator == "OR":
			return self.input[0] | self.input[1]
		elif self.operator == "RSHIFT":
			return self.input[0] >> self.input[1]
		elif self.operator == "LSHIFT":
			return self.input[0] << self.input[1]
		else:
			raise Exception("Unexpected binary operator {}".format(self.operator))

	def replace_inputs(self, signals):
		new_inputs = []
		for n, i in enumerate(self.input):
			if type(i) == str:
				new_inputs.append(signals[i])
			else:
				new_inputs.append(i)

		self.input = new_inputs

		return self

	@property
	def input_list(self):
		inputs = []
		for i  in self.input:
			if type(i) == int:
				inputs.append( str(i) )
			elif type(i) == str:
				inputs.append( i )
			else:
				inputs.append( i.output )

		return "(" + ", ".join(inputs) + ")"

	def run(self, signals):

		if self.verbose:
			print("Running signal {}, which is {} and has inputs {}".format(
				self.output, self.type, self.input_list))

		if self.optype == self.NULLARY:
			self.input[0] = self.input[0] if type(self.input[0]) == int else self.input[0].run(signals)
			return self.input[0]

		elif self.optype == self.UNARY:
			result = self.unaryop(signals)

		elif self.optype == self.BINARY:
			result = self.binaryop(signals)
		
		return result

def get_instruction_dict(instructions, verbose=False):

	instruction_dict = {}
	for ins in instructions:
		ins = Instruction(ins, verbose)
		instruction_dict[ins.output] = ins

	for key, ins in instruction_dict.items():
		ins = ins.replace_inputs(instruction_dict)
		instruction_dict[key] = ins

	return instruction_dict

def run_instructions(instructions, result_signal_name, verbose=False):
	
	instruction_dict = get_instruction_dict(instructions, verbose)
	return instruction_dict[result_signal_name].run(instruction_dict)

def replace_signal(instructions, signal_name, new_input):

	new_instructions = []

	for instruction in instructions:
		if instruction.strip().endswith("-> " + signal_name):
			new_instructions.append(new_input + " -> " + signal_name)
		else:
			new_instructions.append(instruction)

	return new_instructions 

if __name__ == "__main__":

	instructions = sys.stdin

	end_signal = sys.argv[1]
	try:
		verbose = sys.argv[2] == 'v'
	except:
		verbose = False

	#print("Running with end signal {}".format(end_signal))
	#result = run_instructions(instructions, sys.argv[1], verbose)	
	
	instructions = replace_signal(instructions, "b", "16076")
	pp.pprint(instructions)
	print("Running with end signal {}".format(end_signal))
	result = run_instructions(instructions, sys.argv[1], verbose)	
	
	print(result)
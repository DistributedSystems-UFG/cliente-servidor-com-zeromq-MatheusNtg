from constCS import * #-
import pickle
import zmq

possible_ops = {
	1: 'For add         type "+"',
	2: 'For multiply    type "*"',
	3: 'For subtraction type "-"',
	4: 'For division    type "/"',
}

def print_op_usage():
	for op in possible_ops.values():
		print(op)

print_op_usage()
operation = str(input("Chose you operation: "))
first_operand = int(input("Type the first operand (integers only): "))
second_operand = int(input("Type the second operand (integers only): "))

if operation not in ["+", "-", "/", "*"]:
	print("Invalid operation")
	exit()

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

raw_msg = {
	"operation": operation,
	"operand1": first_operand,
	"operand2": second_operand,
}
msg = pickle.dumps(raw_msg)
socket.send(msg)

#  Get the reply.
message = socket.recv()
message = pickle.loads(message)
result = message["result"]
print(f"Result {result}")

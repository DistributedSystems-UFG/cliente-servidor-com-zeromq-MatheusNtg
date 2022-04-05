from constCS import *
import pickle
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(f"tcp://*:{PORT}")

while True:
	#  Wait for next request from client
	message = socket.recv()
	unmarshaled_message = pickle.loads(message)
	operation = unmarshaled_message["operation"]
	op1 = unmarshaled_message["operand1"]
	op2 = unmarshaled_message["operand2"]

	result = 0
	if operation == "+":
		result = op1 + op2
	elif operation == "-":
		result = op1 - op2
	elif operation == "/":
		result = op1 / op2
	elif operation == "*":
		result = op1 * op2

	raw_msg = {
		"result": result
	}
	msg = pickle.dumps(raw_msg)

	#  Send reply back to client
	socket.send(msg)
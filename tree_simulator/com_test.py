from util.osc import OSCOut

osc_out = OSCOut(6006)
osc_out.log_osc = True


while True:
    address, message = input().split()
    osc_out.send(address, message)

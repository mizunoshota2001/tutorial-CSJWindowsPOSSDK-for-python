import csv
import serial

menuL = [
    ["q", "NOR", 250],
    ["w", "DX", 350],
    ["e", "GAME", 0],
    ["t", "TAKO", 0],
    ["d", "DISC", -100],
    ["h", "DISh", -50],
    ["n", "note", 0],
    ["s", "smile", 0]
]
print("hello!")

for i in range(300,999):
    print("ready: q,w,e,t,d,h,n,s")
    order = input("order:")

    if order == "exit":
        print("see you!")
        break
    
    note = None
    if "n" in order:
        note = input("note:")

    print("-------------------------")
    
    if order.count("q") >= 1 or order.count("w") >= 1:
        order += "d" * (order.count("q") + order.count("w"))
    #order += "d" * (order.count("w") // 2)
    
    orderL, totalL, total =[], [], 0  
    for j in menuL:
        print(f"{j[1]} {order.count(j[0])}個 {j[2] * order.count(j[0])}円")
        orderL.append(order.count(j[0]))
        totalL.append(j[2] * order.count(j[0]))
        total += j[2] * order.count(j[0])
    print(f"\nid:{i:03} total:{total}円\n-------------------------")

    while True:
        payment = input("payment:")
        if payment == "cancel":
            with open('sample.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([i] + [0, 0, 0, 0, 0, 0, None])
                f.close
            print("canceled\n-------------------------")
            break

        elif not payment.isdigit() or int(payment) < total:
            print("error")

        else:
            payment = int(payment)
            print(f"change:{payment-total}円\n-------------------------")
            """ with open('sample.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([i] + orderL + [total] + [note])
                f.close """
            ser = serial.Serial('COM4', 9600, timeout = 0.1)
            #レシート

            ser.write(chr(29).encode("shift_jis"))
            ser.write(chr(33).encode("shift_jis"))
            ser.write(chr(49).encode("shift_jis"))
            ser.write("{}\n\n".format("サイバーたません").encode("shift_jis"))
            ser.write(chr(29).encode("shift_jis"))
            ser.write(chr(33).encode("shift_jis"))
            ser.write(chr(16).encode("shift_jis"))
            if(orderL[0] > 0):
                ser.write("{0}  @{1} ￥{2:,}\n".format(menuL[0][1],orderL[0],totalL[0]).encode("shift_jis"))
            if(orderL[1] > 0):
                ser.write("{0}   @{1} ￥{2:,}\n".format(menuL[1][1],orderL[1],totalL[1]).encode("shift_jis"))
            if(orderL[2] > 0):
                ser.write("{0} @{1} ￥{2:,}\n".format(menuL[2][1],orderL[2],totalL[2]).encode("shift_jis"))
            if(orderL[3] > 0):
                ser.write("{0} @{1} ￥{2:,}\n".format(menuL[3][1],orderL[3],totalL[3]).encode("shift_jis"))
            if(orderL[4] > 0):
                ser.write("{0} @{1} ￥{2:,}\n".format(menuL[4][1],orderL[4],totalL[4]).encode("shift_jis"))
            if(orderL[5] > 0):
                ser.write("{0} @{1} ￥{2:,}\n".format(menuL[5][1],orderL[5],totalL[5]).encode("shift_jis"))
            if(orderL[7] > 0):
                ser.write("{0}   ￥{1}\n".format(menuL[7][1],totalL[7]).encode("shift_jis"))
            if(orderL[6] > 0):
                ser.write(chr(29).encode("shift_jis"))
                ser.write(chr(33).encode("shift_jis"))
                ser.write(chr(0).encode("shift_jis"))
                ser.write("{}\n".format(note).encode("shift_jis"))
                ser.write(chr(29).encode("shift_jis"))
                ser.write(chr(33).encode("shift_jis"))
                ser.write(chr(16).encode("shift_jis"))
            ser.write("\n合計    ￥{:,}\n".format(total).encode("shift_jis"))
            ser.write("お預り  ￥{:,}\n".format(payment).encode("shift_jis"))
            ser.write("お釣り  ￥{:,}\n".format(payment-total).encode("shift_jis"))

            ser.write(chr(29).encode("shift_jis"))
            ser.write(chr(33).encode("shift_jis"))
            ser.write(chr(86).encode("shift_jis"))
            ser.write(chr(29).encode("shift_jis"))
            ser.write(chr(66).encode("shift_jis"))
            ser.write(chr(1).encode("shift_jis"))            
            ser.write("\n\n {} \n".format(i).encode("shift_jis"))
            ser.write(chr(29).encode("shift_jis"))
            ser.write(chr(66).encode("shift_jis"))
            ser.write(chr(0).encode("shift_jis"))            

            ser.write(chr(29).encode("shift_jis"))
            ser.write("V".encode("shift_jis"))
            ser.write(chr(66).encode("shift_jis"))
            ser.write(chr(45).encode("shift_jis"))

            #厨房伝票
            ser.write(chr(29).encode("shift_jis"))
            ser.write(chr(33).encode("shift_jis"))
            ser.write(chr(49).encode("shift_jis"))
            ser.write(chr(29).encode("shift_jis"))
            ser.write(chr(66).encode("shift_jis"))
            ser.write(chr(1).encode("shift_jis"))
            ser.write("{}\n\n".format(i).encode("shift_jis"))
            ser.write(chr(29).encode("shift_jis"))
            ser.write(chr(66).encode("shift_jis"))
            ser.write(chr(0).encode("shift_jis"))
            ser.write("{0}  {1}\n".format(menuL[0][1],orderL[0]).encode("shift_jis"))
            ser.write("{0}   {1}\n".format(menuL[1][1],orderL[1]).encode("shift_jis"))
            if(orderL[2] > 0):
                ser.write("{0} {1}\n".format(menuL[2][1],orderL[2]).encode("shift_jis"))
            if(orderL[3] > 0):
                ser.write("{0} {1}\n".format(menuL[3][1],orderL[3]).encode("shift_jis"))
            if(orderL[6] > 0):
                ser.write(chr(29).encode("shift_jis"))
                ser.write(chr(33).encode("shift_jis"))
                ser.write(chr(17).encode("shift_jis"))           
                ser.write("\n{}\n".format(note).encode("shift_jis"))

            ser.write(chr(29).encode("shift_jis"))
            ser.write("V".encode("shift_jis"))
            ser.write(chr(66).encode("shift_jis"))
            ser.write(chr(45).encode("shift_jis"))
            ser.close() 
            break
    
#!/usr/bin/env python
#-*-conding:utf-8-*-

import  pika,sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
                host="172.21.129.252"))
channel = connection.channel()
channel.queue_declare(queue="task_q",durable=True)
messgae = ''.join(sys.argv[1:]) or "Hello Word!"

channel.basic_publish(exchang="",
                      routing_key="task_q",
                      property=pika.BasicProperties(
                        delivery_mode = 2,
                      ))
print("[x] Sent %r " %messgae )
connection.close()



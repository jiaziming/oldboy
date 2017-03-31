#!/usr/bin/env python
#-*-conding:utf-8-*-

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               '172.21.129.252'))
channel = connection.channel()

#生成queue
channel.queue_declare(queue='hello_queue',duralbe=True)
#n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange
#RabbitMQ消息不能直接发送到队列，它总是需要通过一个交换
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!123')
print(" [x] Sent 'Hello World!'")

connection.close()
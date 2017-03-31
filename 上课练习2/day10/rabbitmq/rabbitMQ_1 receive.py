#!/usr/bin/env python
#-*-conding:utf-8-*-

import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '172.21.129.252'))
channel = connection.channel()
'''
You may ask why we declare the queue again ‒ we have already declared it in our previous code.
We could avoid that if we were sure that the queue already exists. For example if send.py program
was run before. But we're not yet sure which program to run first. In such cases it's a good
practice to repeat declaring the queue in both programs.
你可能会问为什么我们宣布再排队‒我们已经在我们以前的代码声明。
我们可以避免，如果我们确定队列已经存在。例如，如果send.py程序运行之前。
但我们还不确定先运行哪个程序。在这种情况下，在两个程序中重复声明队列是很好的做法。

'''
channel.queue_declare(queue='hello_queue',durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()



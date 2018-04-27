package main

import (
	"github.com/streadway/amqp"
	"log"
	"io/ioutil"
)

func failOnError(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func main() {
	mq, err := amqp.Dial("amqp://guest:guest@172.16.92.158:5672/")
	failOnError(err)
	defer mq.Close()

	ch, err := mq.Channel()
	failOnError(err)
	defer ch.Close()

	//err = ch.ExchangeDeclare("websocket", "topic", false, false, false, false, nil)
	//failOnError(err)

	body, err := ioutil.ReadFile("mq.json")
	failOnError(err)
	err = ch.Publish("websocket", "", false, false, amqp.Publishing{
		ContentType: "application/json",
		Body:        body,
	})
	failOnError(err)

	//q, err := ch.QueueDeclare("ws_msg.info", false, false, false, false, nil)
	//failOnError(err)
	//err = ch.QueueBind(q.Name, "", "websocket", false, nil)
	//failOnError(err)
	//
	//msgs, err := ch.Consume(q.Name, "", true, false, false, false, nil)
	//failOnError(err)
	//
	//forever := make(chan bool)
	//go func() {
	//	for m := range msgs {
	//		fmt.Println(string(m.Body))
	//	}
	//}()
	//<-forever
}

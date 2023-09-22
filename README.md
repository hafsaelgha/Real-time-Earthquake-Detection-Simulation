# Real-Time-Data-Pipeline-on-AWS-
Simulation of Earthquake Detection by streaming real time data from sensors on your smartphone. 

# Introduction
Following the latest tragedy which affected my country Morocco, I saw several articles and information which promote the role of scientific research in the prediction of **earthquakes** by using AI or machine learning models, but no one has mentioned the role of **data engineer** in collecting information from sensors in different corners of the world to enable the prevention of earthquakes beforehand.

In this project, we will use the movement of the phone as a **simulation of the earthquake**, if the phone moves or vibrates with a certain frequency, the user will be notified of the earthquake (we neglect any external factor which can harm this experience assuming that only the sensor application logger is installed on our phone). 

In order to achieve this at the technical level, we create a streaming data pipeline which collects data from the Sensor Logger application, this data will be produced by the kafka producer (lambda function) and then consumed by the consumer to display the earthquake notification message. 

# Architecture 

![RT-streaming](https://github.com/hafsaelgha/Real-Time-Data-Pipeline-on-AWS-/assets/99973359/2148f98a-91c4-495f-baba-ef2690cfaf89)

## Comments 
1-Sensor Logger : is definetly our data source, we gonna focus on the **Inertial sensor**, on the **Accelerometer** parameter.

2-API Gateway : It serves as a gateway for your backend services, allowing you to expose them as APIs to be accessed by clients such as web and mobile applications.

3-Lambda function : In our use case, lmabda function publish messages received from API Gateway to Kafka Consumer.

4-Layer : It's a .zip file archive that contains supplementary code or data. Layers usually contain library dependencies, a custom runtime, or configuration files. we use it here to reduce the size of your deployment packages. (kafka)

5-EC2 Instance : we will deploy our Kafka cluster here.

6-Apache Kafka : it's a streaming framework used to simpliy the real time data stream pipeline by using his architecture based on : Producer, Topics,Messages, Consumer.

# Steps and Remarks 

## 1-Configuring the Sensor Logger Application on your phone
** The Accelerometer parameter**
![config 1](https://github.com/hafsaelgha/Real-Time-Data-Pipeline-on-AWS-/assets/99973359/55aa693d-9adc-4bdf-99d8-bd88438e9605)

**Enable the HTTP Push**
![config 2](https://github.com/hafsaelgha/Real-Time-Data-Pipeline-on-AWS-/assets/99973359/1a320af0-22fa-49e6-b307-76165c322cc3)

The **Push URL** was modified after creating the API Gateway Route

## 2-API Gateway 
We create an API endpoint and save the invoke URL, then we create a POST Route and integrate it with lambda funtcion

![3](https://github.com/hafsaelgha/Real-Time-Data-Pipeline-on-AWS-/assets/99973359/415065cf-1ab6-4c75-ba5b-75e5b1637fdd)
![1](https://github.com/hafsaelgha/Real-Time-Data-Pipeline-on-AWS-/assets/99973359/bfb8a6ba-aaa3-4739-8648-f8172a706bd5)
![2](https://github.com/hafsaelgha/Real-Time-Data-Pipeline-on-AWS-/assets/99973359/d87cd7c9-5ede-47ca-9a5c-e9cc1def82b1)
this will publish the event captured from the Sensor Logger app.

## 3-Lambda Function for producer
We create a lambda function to deploy the code of our consumer and integrate it with the API Gateway that will trigger it. 

![4](https://github.com/hafsaelgha/Real-Time-Data-Pipeline-on-AWS-/assets/99973359/a02e0ac3-6c68-4d43-b6cf-05d184b4acc4)

We configure it on the code by adding the topic name and the configuration of the Kafka Producer which include the IPv4 adresse of EC2 instance that will run the Kafka cluster. 
This lambda function receive the JSON file from the Sensor Logger app and extract the essential data in order to send it to the consumer.
![5](https://github.com/hafsaelgha/Real-Time-Data-Pipeline-on-AWS-/assets/99973359/340d736c-8d9c-46be-a197-53e5da0971f5)

## 4-EC2 instance configuration
Launching an EC2 instance with this configuration : 

![7](https://github.com/hafsaelgha/Real-Time-Data-Pipeline-on-AWS-/assets/99973359/2a9bd392-8083-4361-94c3-f6c30ed757c1)

## 5-Kafka on EC2 
Installation requirement : 
1-install kafka_2.13-3.4.1
2-install java-1.8.0-openjdk
3-starting the zookeeper
4-modifiying the server.properties file on the "advertised_listeners" variable by adding our IPv4 adress.![8](https://github.com/hafsaelgha/Real-Time-Data-Pipeline-on-AWS-/assets/99973359/c64f3b78-b485-49f0-9fac-4f1fc2ea7349)

### Creating the topic 

![10](https://github.com/hafsaelgha/Real-Time-Data-Pipeline-on-AWS-/assets/99973359/190e04a3-f1c2-4745-a02d-364a0d2a3ff2)

### Start Kafka Consumer 















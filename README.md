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









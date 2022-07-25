# WeatherApp

How to use Micro Service
Note: [This tutorial](https://www.rabbitmq.com/tutorials/tutorial-six-python.html) was used in the design of this message broker and provides a good overview of functionality

REQUEST
- Add MilkshakeRpcClient() class in the main body of your application
- Instantiate MilkshakeRpcClient object in backend
- Use function to cal .call() method of class object or call it directly passing in location string
- String must be city i.e. "Sandiego" or city and state seperated with comma and without spacing i.e. "Sandiego,CA"

RECIEVE
- .call() method returns one of three possible string values 
- Possible string values are
  - "It is Milkshake Weather"
  - "Not Milkshake Weather"
  - "Request Failed"
  
  ![UML Sequence Diagram](https://github.com/Alex-K-Rose/WeatherApp/blob/master/WeatherApp(1).png?raw=true)

# WeatherApp

How to use Micro Service

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

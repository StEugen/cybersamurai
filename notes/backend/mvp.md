<h1>MVP</h1>
Model View Presenter<br>
Model - represents classes that describe the business logic and data.<br>
View - component which interacts with user<br>
Presenter - receives the input from users via View, then process data with the help of Model and passing results back to view. 
 Presenter communicates with view through interface. Interface is defined in presenter class, to which it pass the required data.
In the MVP design pattern, the presenter manipulates the model and also updates the view. In MVP View and Presenter are completely decoupled from each other’s and communicate to each other’s by an interface.

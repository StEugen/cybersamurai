<h1>REST</h1>
REST (Representational State Transfer) is a software architectural style that describes a uniform interface between separate (physically!) components. 
In another words REST is a set of rules how programmers should organize code of server app, so all systems can easily exchange data and size.
<br>
Features of REST:<br>
<ul>
<li> Efficiency: components' interactions of system is a dominant factor of efficiency and effectivity of net </li>
<li>Scalability: for making a lot of components and components' interactions</li></ul>
Roy Fielding describes REST influence on scale:
<ul>
<li>Simplicity of a unified interface</li>
<li>Openness of components to possible changes to meet need (even when app is running)</li>
<li>Transparency of connections between system components for service daemons</li>
<li>portability of system components by moving program code along with data</li>
<li>Reliability, expressed in resistance to failures at the system level in the presence of failures of individual components, connections or data</li>
</ul>
<br>
Requirements to REST architecture:
<ol>
<li>Client-server model: The first limitation applicable to the hybrid model is to bring the architecture to the client-server model. Differentation between needs is a principle. Separation of client's interface needs from server needs, storing data, increases transparation of client code to other platforms, and simplification of server-side increases scalability.The greatest influence on the World Wide Web has the very differentiation that allows individual parts to develop independently of each other, supporting the needs for the development of the Internet from various organizations </li>
<li>No state: Protocol of interaction between client and server should keep next condition: between client requests no info about state kept on server (stateless protocol). All requests should be made so a server receives all the necessary data to complete a request. State of session saves on client side.</li>
 

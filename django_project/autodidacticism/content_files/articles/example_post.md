# Networking Theory
A Private Repository Containing all the code and material that I used to study and learn the concepts of networks and network programming

## Table of Contents
* ### [Reading List](https://github.com/MatthewTe/Networking_Theory_Repo#reading-list-1)
* ### [Network Sockets and Network Socket Programming](https://github.com/MatthewTe/Networking_Theory_Repo#network-sockets-and-network-socket-programming-1)
* ### [Python Socket Applications and P2P Networks](https://github.com/MatthewTe/Networking_Theory_Repo#python-socket-applications-and-p2p-networks-1)

## Reading List
**Networking All-in-One For Dummies**
[Read this](https://www.amazon.com/Networking-All-One-Dummies-Doug/dp/1119471605) for a general overview of networking concepts. Re-read chapters and mini-books as refreshers on specific concepts.

**Foundations of Python Network Programming Second Edition**
[Read this](https://www.amazon.com/Foundations-Python-Network-Programming-comprehensive-ebook/dp/B004VHFX8W/ref=sr_1_2?dchild=1&keywords=Foundations+of+Python+Network+Programming+Second+Edition&qid=1588863681&s=books&sr=1-2) for an in depth look at the theory behind network sockets and programming network sockets in python. Note that all the code examples in the book are written in python 2.7 therefore many of the examples will have to be re-worked for python 3.

## Network Sockets and Network Socket Programming
The basic theory and concepts of how networks transfer data and communicate via network sockets is explained via the use of the Foundations of Python Network Programming Second Edition. These important concepts are summarized in [the following document](https://github.com/MatthewTe/Networking_Theory_Repo/blob/master/python_network_programming/Network_Sockets_Concepts_Summary.md).

## Python Socket Applications and P2P Networks
The same principles when sending data using UDP protocols apply when streaming data with the much more common TCP/IP protocols. The applications of socket streaming with python are nearly endless, as the use of the `pickle` library allows any python object to be streamed over a sockets. I have come to realize that many of the data pipelines and web scraping/data collection and processing applications will require a platform on which to operate and deploy. Given what I understand is possible using network sockets I have decided to undertake the massive project of constructing a distributed P2P network platform on which I can deploy all of my major projects. The progress towards such a network is sure to be slow going and features shall be built in as needed. Actually making use of this network is the secondary goal, the primary goal is to use the process of actually building it to learn core networking concepts. The progress of the network and its functions shall be described in detail in [this folder](https://github.com/MatthewTe/Networking_Theory_Repo/tree/master/entropy_network_documentation).

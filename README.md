# DataComm-FinalProject

# Project 2: Simple File-Transfer System 

# Project Description

This project introduces the concept of client/server architecture using socket programming. Your task is to create a multithreaded file transfer application that sends and receives files from surrounding devices in the network using sockets. The device used for this project are raspberry pi running linux os with each device as part of a mesh network running on openthread. Each device should have running a multithreaded server and a client program which allows for file request and response. Since openthread only permits the use of ipv6, all of the socket communication between devices will have to use ipv6 instead of ipv4 as previously seen in the last project. A pictorial description of the entire system architecture is shown below 


               
# Requirements
Implement the installation of Linux OS and Openthread, and setting up the mesh network on Raspberry Pi using the detailed description listed here
Implement a server and client file transfer application on each device using IPv6  connection. Once connected to the client using telnet, a user should be able to specify the file path of the document being requested from the server. The server on receiving this request should return the file requested by the client. If this file is not found, an appropriate error message should be displayed.
Implement a functionality to display the round trip time of each file request. 
Extra Credit: Create an encryption mechanism between data transfers using AES Symmetric key encryption. That is, data sent is encrypted at the sender’s side and decrypted at the receiver's side using a single key. Hint: refer to a tutorial on an implementation of AES encryption using Python's library (PyCrypto).


# Connecting to the Server via a Client
To establish a connection with the server:
Install  telnet . 
Ensure that your server server program is running on the appropriate device. 
Open a terminal and connect to the client using the command  telnet <ip address> <port #>  

# What to Hand in
All code must be turned in through a version control system (e.g github). Each group will provide a link to their repository in blackboard/classroom.
Program demonstration is required either through a video or an in-person presentation to the instructor. The demo must outline all of the functionalities described in this document.

# Grading
You will be graded as a group based on the functionality of your application--if your application meets the following conditions:
Implements a mesh network using openthread as described here  
Implements the client/server components of the file sharing application (i.e files can be sent and received from every device on the network).
Implements multithreading where multiple files can be sent and received at an instance.
Displays the appropriate round trip time information.



# Additional Resources
Github
Github Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf
A crash course on Github: https://www.youtube.com/watch?v=0fKg7e37bQE

# Python Resource
Python Socket Tutorial
Simple File Transfer Program
Simple File Transfer Tutorial
Somewhat Complex File Transfer Tutorial
Tutorial on Socket programming using IPv6
A Tutorial on Socket Programming using IPv6


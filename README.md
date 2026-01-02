Network File Sharing System Using Flask Framework
Issue: 30 | Nov 2025

AUTHORS
Vishal Kumar¹-2023011085, Tarkeshvar Mani Yadav²-2023011078, Shashwat Srivastava³-2023022159
¹²³Undergraduate Students, Department of Computer Science & Engineering,
Madan Mohan Malaviya University of Technology, Gorakhpur, Uttar Pradesh, India.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ABSTRACT - File sharing is an imperative aspect of contemporary computer networks that enables data exchange
between various devices. The existing file sharing systems like FTP and SMB entail complicated settings and the use of
servers. With the emergence of local area networks and the popularity of web platforms, the demand for a simple, safe,
and transportable file sharing technique has increased.
In this paper, the design and development of the Network File Sharing System using the Flask framework is presented.
Using this system, it is possible to upload and download files over the local network using the web browser. In this
proposed system, the architecture utilized is client-server. The server is denoted by the Flask framework, and the client is
the general browser. Password security is incorporated to limit unauthorized access. In this proposed design, the HTTP
and TCP protocols are used.
This proposed solution is easy to implement, doesn’t require the use of a database, and is practical to implement in
academic labs, classrooms, or small networks.
Key Words: File Sharing, Flask, Client Server Architecture, HTTP, Local Area Network, Web Application


1. INTRODUCTION
Recently, the flow of electronic data has increased substantially between networks owing to the advent of computers
and the use of local area networks. The exchange of files has an important place in teamwork and an educational setup.
The traditional technique for exchanging files between networks includes the use of FTP and SMB. However, the existing
technology has an intricate setup and overhead.
Lightweight frameworks for the web are improving, and as a result, filesharing systems via the web are gaining popularity.
Since Flask is a micro framework for the web developed using the Python language, it is simple, flexible, and easy to
implement. The filesharing system via the web cuts the need for a special client application as files are accessible via the
browser.
In this research paper, we shall discuss the development of a file sharing application on a network using the flask
framework, which shall be able to work on a local area network, possessing the capabilities for login, uploading, and
downloading files.


3. METHODOLOGY
   
2.1 Design Approach
The system is proposed using the client-server concept. The backend server is composed of the flask app acting as the
server in charge of storing files, user authentication, and the transfer of files. The client uses a web browser
communicating with the server using HTTP requests.
The project follows agile development techniques to enable incremental development and testing of functionalities such
as authentication modules, upload modules, as well as download modules.

2.2 System Architecture
The architecture for the proposed system can be broken down into the following components:
• Flask Server, where routing, auth, upload, and download are performed.
• Client (Web Browser): It is the user interface used to access shared files.
• File Directory: This stores the uploaded files on the server side.
• Network Layer: TCP/IP and HTTP protocol checklist Used to transmit data.
The IP address and port on which the server listens (the default is 5000) are based on client requests.

2.3 Working Principle
The sequence of the system's working is thereby performed as follows:
1. The Flask server is started on a local machine or LAN.
2. Accessing the application: The user has to access the server IP and port using a browser.
3. Password: It asks the user to enter a password for authentication.
4. The dashboard allows viewing of all available files upon successful authentication.
5. A user can upload new files to the server.
6. Users can download existing files from the server.
7. All file transfers occur over HTTP using TCP for reliable delivery.

   
3. IMPLEMENTATION DETAILS
   
3.1 Authentication Module
A basic password-based network authentication mechanism is employed to guarantee authorized access. The user needs
to enter the valid password to get access to operations involving files. Unauthorized access prevents access to the files.

3.2 File Upload Module
The upload module is where users can pick their file from their computer and then upload it to the server. The file is
uploaded using HTTP posts, and it is received in a specific directory on the server.

3.3 File Download Module
The download module is responsible for listing all the files hosted on the server. When the user clicks on the file, it is
sent from the server as an attachment for download by the client.


5. TOOL AND TECHNOLOGY USED
• Python 3.x Programming Language for Background/Server
• Flask Framework: Lightweight web framework for building servers
• Name: Flask Framework
• HTML/CSS - Frontend User Interface Design
• HTTP Protocol - File transfer & communication
• TCP/IP: Reliable data transfer
• Web Browser: Interaction on the Client-side


6. FEATURES OF THE PROPOSED SYSTEM
1. Password-protected access
2. Upload and download of files via web page
3. Light weight and easy to deploy
4. No database dependency.
5. LAN-based file sharing support


6. FLOW OF OPERATION
1. Run Flask server
2. User opens browser, types in server URL
3. Authentication check
4. View dashboard
5. Upload or download file
6. File transfer completed successfully
7. Kill session.

   
7. RESULTS AND OBSERVATIONS
The implemented system will be able to facilitate the sharing of files over a local network, with very minimal
configurations. The testing of uploading and downloading different file formats and sizes was performed. The system
performed reliably on a LAN environment and required few resources as compared to traditional file sharing systems.


9. CONCLUSION
This paper presented a Network File Sharing System using Flask, showing the web technologies that can be applied to
local file transfer effectively. The system consequently simplifies file sharing by eliminating the use of any specialized
software or complex configurations. It offers secure, efficient, and user-friendly file transfer capabilities by using some
very basic concepts of networking.
The system would be quite applicable at educational institutions and small organizations. Some of the further
enhancements may be in regards to encryption, user role management, and cloud deployment, where scalability can be
extended quite effectively.


11. FUTURE SCOPE
• Encrypting files for secure transfers
• Access control based on the user
• Integration of databases
• Deployment based on cloud
• Mobile compatibility

13. REFERENCES
1. Flask Official Documentation
2. Python Networking Documentation
3. Computer Networking Textbooks
4. HTTP and TCP/IP Protocol Standards.

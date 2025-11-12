Network File Sharing using Flask

Group - Infinity

Vishal Kumar

Roll No: 2023011085

B. Tech (Computer Science & Engineering), 5th Semester

Email: vkumar26062003@gmail.com | Phone: +91 7800982247

Tarkeshvar Mani Yadav

Roll No: 2023011078

B. Tech (Computer Science & Engineering), 5th Semester Email: tarkeshvarmani@gmail.com | Phone: +91 7880626736

Shashwat Srivastava

Roll No: 2023021159

B. Tech (Computer Science & Engineering), 5th Semester Email: shashwatwrites@gmail.com | Phone: +91 9219325153


🔷 1. Abstract

In the modern digital world, file sharing plays a vital role in communication and data exchange. The Network File Sharing using Flask project is a small-scale implementation of a local file-sharing system that allows users to upload and download files easily through a web interface. This system is designed using the Flask web framework in Python and leverages HTTP and TCP protocols for reliable and secure data transfer.

The application allows users to:
Access a login-protected web interface.
Upload files from their system to the server.
Download any available files hosted by the server.
This project demonstrates the working of a client-server model, where the Flask server acts as the file provider and the user’s browser acts as the client. It serves as a simplified yet practical example of how file transfer happens across networks securely.

🔷 2. Objective

The main objectives of this project are:
To design a simple and secure local file-sharing system using Flask.
To implement upload and download functionality within a web-based interface.
To apply password protection for restricting unauthorized users.
To understand the use of network communication protocols (HTTP and TCP).
To demonstrate client-server communication using a lightweight Python web framework.

🔷 3. Introduction

File sharing is one of the most common operations in computer networks. Traditional systems use FTP (File Transfer Protocol) or SMB (Server Message Block) for sharing data. However, this project uses Flask to create a custom file-sharing system that runs locally or over a LAN network.

Users can:

Open a local web address (like http://127.0.0.1:5000)
Enter a secure password (e.g., 12345).
View the list of available files.
Upload or download files with a single click.
The system can run entirely on one PC or within the same Wi-Fi network — making it a portable and easy-to-demonstrate solution for classroom or lab submissions.

🔷 4. Tools and Technologies Used

🧰 Software & Libraries

Tool	Purpose
Python 3.x	Programming language used to implement backend logic.
Flask	Lightweight web framework for building the server and handling HTTP requests.
HTML / CSS / JavaScript	Frontend technologies to design the web interface.
FPDF (optional)	Used to generate automated project reports.
Browser (Chrome/Edge)	Acts as a client to interact with the Flask server.
🖧 Protocols Used
Protocol	Description
HTTP (HyperText Transfer Protocol)	Used for transferring files and web page data between the server and client.
TCP (Transmission Control Protocol)	Ensures reliable delivery of packets and data transfer.
Socket Layer	Flask internally uses sockets to handle communication between client and server.

🔷 5. Working Principle

The project works on the Client-Server Architecture.
The Server is created using Flask and hosts all files inside a directory (files/).
The Client (browser) connects to the server using an IP address and a port.
Flask listens on the default port 5000 and provides two main routes:

/ → for the homepage and file listing.
/download/<filename> → to download selected files.
/upload → to upload files.
Before accessing these routes, the user must log in using the password “12345”.

Once authenticated, users can perform file operations securely.

🔷 6. Features

1-Password Protected Access
Only authorized users can log in with a correct password (12345) to access the dashboard.

2-File Upload Functionality
Users can upload files directly from their browser, and the Flask server saves them in the files/ folder.

3-File Download Option
All stored files are listed on the page with download links. A user can download any file with one click.

4-Dynamic UI (User Interface)
The interface is built using HTML and CSS to provide a professional look with buttons, cards, and layout.

5-Local Network Access
When hosted on LAN (host="0.0.0.0"), other devices connected to the same Wi-Fi can also access the shared files via the server’s IP.

6-Easy to Deploy & Run
No database or external dependencies are needed. It runs with a single Python script.

🔷 7. Flow of Operation

🔹 Step-by-Step Process

Start the Flask Server
Run python app.py
The Flask application starts and listens for connections.
User Opens the Webpage
Access through http://127.0.0.1:5000 or local IP address.

Login Authentication
The user enters the password.
If password = 12345, access is granted.
If incorrect, error message is shown.

Dashboard Display
The home page lists all the files available for download.
The upload form is also displayed to send new files.
Upload Process
The user selects a file and submits.
Flask receives the file via POST request and saves it in the files/ folder.
Download Process
When a user clicks a file name, Flask sends that file to the browser as an attachment.
End

File transfer completes successfully and the session ends.

🔷 8. Flowchart (Description)
Start
  ↓
User Opens Web App
  ↓
Enter Password
  ↓
 ┌──────────────┐
 │ Password OK? │
 └──────┬───────┘
        │Yes
        ↓
Show Dashboard → Upload / Download
        ↓
Perform Action (File Transfer)
        ↓
Success Message
        ↓
End

🔷 9. Advantages

✅ Simple and lightweight system for LAN file sharing
✅ Password-protected for basic security
✅ Works on any browser and platform
✅ Requires no external software like FTP servers
✅ Easy to extend and customize

🔷 10. Limitations

❌ Not suitable for large-scale or internet-widesharing.
❌ No user account management system.
❌ Files are not encrypted during transfer.
❌ Works only on devices in the same network (unless deployed online).

🔷 11. Future Scope

Add user authentication with multiple accounts.
Implement encryption (SSL / HTTPS) for secure transfer.
Add file size limits and activity logs.
Deploy on cloud servers (Heroku, Render, or AWS) for remote access.
Build a database integration (SQLite / MySQL) for storing user and file info.

🔷 12. Conclusion

The Network File Sharing using Flask project successfully demonstrates how local file sharing can be achieved using Python and basic web technologies. It combines the simplicity of Flask with the practicality of HTTP-based file transfer.
This project is an excellent demonstration of:
Client-Server Architecture
Network Communication
Web-based File Management

It provides a good foundation for understanding how file sharing systems like Google Drive or Dropbox work at a smaller scale. With future improvements, it can evolve into a secure and full-fledged cloud file sharing system.

🔷 13. References

Flask Official Documentation – https://flask.palletsprojects.com
Python Socket Programming Guide – GeeksforGeeks
HTTP and TCP Protocol Notes – Computer Networking Tutorials

Group - Infinity

Vishal Kumar
Roll No: 2023011085
B. Tech (Computer Science & Engineering), 5th Semester 
Email: vkumar26062003@gmail.com | Phone: +91 7800982247

Tarkeshvar Mani Yadav
Roll No: 2023011078
B. Tech (Computer Science & Engineering), 5th Semester Email: tarkeshvarmani@gmail.com | Phone: +91 7880626736

Shashwat Srivastava
Roll No: 2023021159
B. Tech (Computer Science & Engineering), 5th Semester Email: shashwatwrites@gmail.com | Phone: +91 9219325153

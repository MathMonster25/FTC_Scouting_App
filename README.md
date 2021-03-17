# FTC_Scouting_App

I'm not yet sure of my full plan for this project. For now it is a side project with the goal of using it as a scouting app for FTC competitions. Actually, This project will actually contain two apps. One as the host and the other for clients. Using Python and Kivy, the client will be compatible with Android, IOS, Windows, MacOS, and Linux (as long as I can reasonably bug test each platform).

The purpose of the host is:
----------------------------
- To host a bluetooth server (TODO: Check legality of bluetooth during competitions, if illegal this will be replaced by some kind of wired communication)
- To collect scouting data from connected clients
- To display and be able to edit any scouting data in a table-like format
- To save data as either .csv (for reuploading to the app) or .png (for viewing outside of the app) files

The purpose of the client is:
-----------------------------
- To provide an easy way to track multipls teams' scores
- To review and edit old scores
- To connect and send score data to the host

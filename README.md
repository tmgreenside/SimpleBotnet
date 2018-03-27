# SimpleBotnet
I found the source code for this at https://www.cybrary.it/0p3n/python-programming-hackers-part-6-creating-ssh-botnet/ and tested it on my own virtual machines.

To implement: create two virtual machines, one of which will be Command and Control server to send instructions to the underlings. the
second VM will be an underling.  Use the addClient() function to add any VMs or servers you want.  Underlings must be configured to accept
SSH connections.

Set up the Ubuntu Server 16.04 LTS VM:
1. 2048 MB memory, 10 GB storage. Create Virtual Hard Disk Now. Before starting, make sure you set the network setting to a NatNetwork. You may need to create one.
2. Follow on-screen instructions. Use arrows and enter key to navigate prompts. The setup process is self-explanatory. No need to bother encrypting home directory, when this prompt comes up.
3. Partitioning method: use entire disk.
4. HTTP Proxy: leave blank.
5. Enable SSH connections, link: https://help.ubuntu.com/lts/serverguide/openssh-server.html
6. Now install python. $ sudo apt-get install python2.7
7. Set python variable. 
  $ nano ~/.bashrc
  Append this line: alias python=python2.7
8. sudo apt-get install python-pip
9. pip install 'pexpect'
10. Change the information in the call to addClient() to match your target IP address, user, and password.

Now you're ready to rock and roll.

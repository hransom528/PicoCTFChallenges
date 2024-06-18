# Wireshark doo dooo do doo
### Category: Forensics
### Harris A. Ransom

## Challenge
Can you find the flag?
File: shark1.pcapng

## Solution
The file included with this challenge is an example of a **pcap**, or *packet capture*, file. We can open this with a tool called **Wireshark** (as the catchy title suggests) to perform further analysis.
When you open the file, you should see a lot of rows of text highlighted in blue and green. These are **network packets**, with each row representing a packet and each column representing a particular field associated with those packets. By default, you should be able to see fields like the timestamp, source and destination IP addresses, and the protocol used by that packet. 

It would be a little tedious to go through each of the hundreds of packets to try and find a flag. Luckily, Wireshark has a tool to make this analysis much simpler. You'll notice that the majority of the packets are **TCP** and **HTTP** traffic, which means that these packets contain web traffic. In your Wireshark window, if you look at the top menu bar and go to `Analyze -> Follow -> TCP Stream`, you should get a new window. This window will allow you to view and sift through the various TCP *streams* present in this pcap file. A TCP stream is like a conversation between two people (if those people were computers and they spoke binary!)

When you first open the window, you should see a bunch of random characters and gibberish. The text "Encrypted Boundary" at the top of this stream gives us a clue as to what's going on here. We're looking at web traffic that is **encrypted**, which means that we cannot view the **plaintext** information unless we have the encryption *key* for that web session (just like how you cant enter a house without a physical key). 

This encrypted TCP stream isn't the only stream present in this pcap file, though. If you click on the up and down arrows near the box labelled "Stream" in the bottom right, you can scroll through the different TCP streams. One you scroll through them, you should find a stream that isn't encrypted. This stream will contain the text `Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}`.

Weird, right? It almost looks like the flag format, but it's all gibberish. It could be that the letters are rotated around in such a way that we can reverse the process and get the flag. This is an example of a **rotation cipher** (to learn more, go to the Mod 26 challenge in the Cryptography category). We can reverse this rotation cipher to get the flag.

**Flag:** The flag is picoCTF{p33kab00_1_s33_u_deadbeef}
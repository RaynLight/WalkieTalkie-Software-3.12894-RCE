# WalkieTalkie-Software-3.12894-RCE
Guide for exploitation
<br>
<br>
**Clone the Repository**
```
git clone https://github.com/RaynLight/WalkieTalkie-Software-3.12894-RCE.git
```
**Run the following command to exploit a remote server**
```
python3 WalkieTalkie-Software-3.12894-RCE.py --ip <ip> --port <port>
```



**This is not an actual exploit**, this is a demonstration for researching and finding vulnerabilities presented at the DSU Offensive Security Club
  
If **you** want to set this up for example please follow these steps     
1. **Download the binary**
2. **Use socat to redirect and fork traffic to the binary:**
```
socat TCP-LISTEN:4444,fork EXEC:<full binary path>
```
3. **Exploit it!!!**

<meta name="google-site-verification" content="syc5lA8hb4O6pCsGTMIMmgxbhHi4pdPiVOuCHTv9zZI" />

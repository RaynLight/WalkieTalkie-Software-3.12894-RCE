# WalkieTalkie-Software-3.12894-RCE
Remote Code Execution for the WalkieTalkie Software 3.12894 software

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

google-site-verification: googlee3bab511352a1a57.html

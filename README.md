# PCA-Auto-Vote
Auto voter for people's choice awards. A simple application that votes automatically for PCA awards using selenium. Randomizes emails to create new accounts.

As a side note, I tried using requests to do this but after inspecting how PCA calculated votes, I realizes that they used some sort of authentication key which I was unable to replicate/decode. The authentication key was some sort of hash that used the args of the vote request along with a hash of something called `client_version` and `versionCheck`. I could not find the value of `client_version` so I was unable to replicate the javascript used to generate the authentication key. 

After watching Young Sheldon the PCA award voting came out and since I really liked the show I decided to try an make an auto voter for it. It reality PCA probably doesn't count so many duplicate votes becuase they all came from the same IP (mine) by you can probably just use proxies to bypass this. 

> Use this application at your own risk

**Setup**<br>
1. Make sure to have chromium installed. To use it with the program you have to install the chromium browser as well as the package bindings for it (selenium)<br>
2. Set the `vote_url` variable to the vote url of the show/move/actor etc which you want the bot to rate. For example, the one for young sheldon is `https://www.votepca.com/vote/the-comedy-show/young-sheldon`<br>
3. Set the `agents` variable to the amount of instances of chromium you want running at the same time. My computer can only handle around 4 without headless and about 8 with headless. <br>
- If you want to be able to see information about the average time it took for each vote, uncomment all the commented lines. The commented lines help calculate average but will likely slow the program down.
- If you want it to run without headless mode, comment out the line that says `chrome_options.add_argument("--headless=new")` (should be around 57)

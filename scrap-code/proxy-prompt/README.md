# proxy-prompt

This repository is about some prompts for chatGPT and maybe others AI solutions.

Behavior declaration files for different conditions are here. They are used to declare some behaviour rules to achieve better results when writing prompts to chatGPT. 

There are three ways to declare this rules to chatGPT.

### First method
Copy-paste rules inside the chat<br>
<pre>
Here are two rules:
1) use only pure python with no libraries to solve issues
2) write a comments for better human understanding
</pre>
Then, write after rules declaration, write a request you need to accomplish:
<pre>
Here are two rules:
1) use only pure python with no libraries to solve issues
2) write a comments for better human understanding
write a python program according to these rules to find square root from any number
</pre>

### Second method
paste a link to behaviour declaration file, use basic prompt and write your request.
basic prompt: <code>Use this link to learn rules from {name-of-behavior-file}, {your-request} </code>
<pre>
https://github.com/StEugen/proxy-prompt/blob/main/webdevprompts/README.md
Use this link to learn rules from README.md, write a python program according to these rules which will find square root from any number 
</pre>
However, i should say one more thing, at first take i've made with this method, chatGPT generated wrong response, however when i used prompt provided below, chatGPT fixed his answer and in next new conversation, it applyed rules from the begining. Here is the link to both this dialogues:<br> 
<a href='./dialogueIssue.md'>Link to dialogues</a><br>
If it generates wrong response after reading rules, type next prompt:<br>
<code>Have you really read the rules?</code>
<br>

### Third method 
paste a link to raw content.
<pre>
https://raw.githubusercontent.com/StEugen/proxy-prompt/main/webdevprompts/README.md
Use this link to learn rules, write a python program according to these rules which will find square root from any number 
</pre>
Same problem as in second method can appear, fix is the same:<br>
<code>Have you really read the rules?</code>

<h1>Algorithms</h1>
Computer doesn't have "bird's eye view", cannot see what's inside cell of RAM <br>
Running time is O (big O notation, used to describe upper bound); Big omega Ω simbol is used to describe how few steps algorithm take (lower bound); Big theta Θ is used when lower and upper bound are the same; <br>
<br>
Linear search - is when you're checking one element after another. <br>
<pre>
pseudocode (search for zero behind doors): 
for each door from left to right
    if number is behind door
        return True
return False
</pre>
<pre>
for  i from 0 to n-1
    if number behind doors[i]
        return True
return False
</pre>
<br>
The algorithm takes n steps to complete; O and Ω are the same, so running time is Θ <br><br>
Binary search - is when numbers are sorted some way, when you go to middle, then gor to left or right, depends what you're searchin for<br>
<pre>
pseudocode (search for number, organized from left to righ, rising):
if no doors
    return False
if number behind middle door
    return True
elif number < miidle door 
    search left half
elif number > middle door
    search right half 
</pre>
<pre>
if no doors
    return False
if number behind  doors[middle]
    return True
elif number < doors[middle]
    search doors[0] through doors[middle-1]
elif number > doors[middle]
    search doors[middle+1] through doors[n-1]
</pre>





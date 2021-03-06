#Computational Thinking <img src="../../Resources/brain.png" width=50px alt="Tick Sheet">


##Instructions
For this computational thinking challenge you should attempt to find a answer to problem set below. The answer to the problem is only part of your response, ***how*** you found the answer is what matters.

Once you can explain the solution you might try to write a computer program to simulate or model the solution. It might even generalise the problem and provide solutions for ***similar*** problems.

##Grading
|Grade|What must I do?|
|-----|---------------|
|D|I will be able to provide an answer to the problem.|
|C|I will be able to provide an answer to the problem, including an explanation of the algorithm / process.|
|B|I will be able to provide a clear explanation of the algorithm I developed to solve to problem.|
|A/A*|I have been able to demonstrate my understanding of the solution to this problem and represented the algorithm using a computer program.|

##The Problem - Ferrying Soliders
####A detachment of **25** soliders need to cross a deep wide river, with no bridge in sight. They spot two boys playing around in a row boat near the shore. They notice two children playing in a rowboat by the shore.
![Ferrying soldiers](../../Resources/ferrying.png)
####The boat is so tiny, however, that it can only hold the two children *or* one of the soliders. How can the soliders get across the river and leave they children in joint posession of the boat? How many times does the boat need to pass from shore to shore in your solution?

###Rules:
- All 25 soliders must end up on the other side of the river.
- The boat can carry one child by themselves, both children or a single solider.
- At the end both children must be with the boat on either shore.

####How many trips from shore to shore must the boat take?
```
101
```
####Explain you algorithm here:
```
1) 2 children cross the river in the boat
2) 1 goes back and leaves the other on the other side
3) 1 adult crosses by himself and leave the child on the shore
4) 1 child goes back over to the other side
5) It now repeats itself, so i know that it takes 4 steps for 1 adult to cross
6) So you do 4*25 to work out the number of trips each solider will take which is 100
7) However to get both children back into the boat the boat must make an extra trip so we add 1, so the total is 101.
8) You can write this as S=Soldier C=children 4*S + 1C
```

##Extension
Can you represent the algorithm for this problem using a computer program (any language)?
eg you could show each step in the algorithm using text:

```
Step 25       SSSSSScc..............SSSSSSSSSSSSSSSSSSS


c = child
S = solider
```       

For text based programs like pytohn you should create a new file in you repository
![Add new](../../Resources/new.png)

For anything else (eg scratch), email you teacher with the file and say you've done so in the comments.

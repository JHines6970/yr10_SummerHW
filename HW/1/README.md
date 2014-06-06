#Exam Questions <img src="../../Resources/exam.png" width=50px alt="Tick Sheet">

##Instructions
Edit this document and answer the questions in the sections surrounded by ```.

There are 30 marks available and are awarded grades as follows:

|Score|Grade|
|-----|-----|
|<6|U|
|6+|G|
|9+|F|
|12+|E|
|15+|D|
|18+|C|
|21+|B|
|24+|A|
|27+|A*|


##Data Representation

###1 - Why do we represent data using binary when using computers *(1 mark)*

```
As the computer reads it as "on and offs" 
```
###2 - How would we represent the number 147 in binary? *(1 mark)*
```
10010011
```
###3 - Can you convert the hexadecimal number **b5** to denary, there is a mark for you working. *(2 marks)*
```
181
```
###4 - Here is a function written is **pseudocode**.
```
FUNCTION validUser (users , user)
    FOR x <-1 to LEN(users)
        IF users[x] = user
			RETURN True
		ENDIF
	ENDFOR
	RETURN False
ENDFUNCTION
```

(a) What type of data is **users**? **(1 mark)**
```
string(characters)
```

(b) What type of data is returned by this function? **(1 mark)**
```
integer
```

##Errors
###6 - This program is supposed to find the mean of a list of numbers and print it out for the user:
```
line1:		tot <- 0
line2:		nums <- [1,6,4,2,5,3]
line3:		FOR x <- to LEN(nums)
line4:			tot <- nums[x]
line5:		ENDFOR
line6:		mean <- tot
line7:		OUTPT mean
```

(a) On which line is there a **syntax** error? **(1 mark)**
```
7
```

(b) What is meant by a **syntax** error? **(1 mark)**
```
Where this a gramatical error in the code for example a missed speech mark or bracket.(or the example in the code, you missed spelt output on line 7)
```

(c) Identify a logical error in the program and suggest how this might be fixed. **(2 marks)**
```
on line 4 as it needs to have tot = tot <- nums[x]
```

(d) Describe and give an example of the 3rd kind of programming error. **(2 marks)**
```
Another is a runtime error, this is where the code runs but then breaks at a certain point, an example is trying to divide a number by 0
```

##Algortithms
###7 - Write an **algorithm** that if given a list of numbers could find the largest. Try to use [pseudocode](http://filestore2.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF).
```
def play():
    print()
    print("Enter 10 numbers below and have them sorted.")
    print()
    List_of_items = []
    add_num = 10

    while add_num > 0:
        add=int(input( str(add_num) + " Number(s) left:"))
        List_of_items.append(add)
        add_num = add_num - 1

    No_more_swaps = False



    while No_more_swaps == False:
        No_more_swaps = True
        for x in range(len(List_of_items)-1):
            if List_of_items[x] > List_of_items[x+1]:
                No_more_swaps = False
                temp = List_of_items[x]
                List_of_items[x] = List_of_items[x+1]
                List_of_items[x+1] = temp

    print()
    print("Here is your list of sorted numbers")
    print (List_of_items)
    print()
    redo=input("Do you want to go again?(Y/N)")
    if redo == 'Y' or 'y':
        play()
    else:
        exit()
play()

```

##Networking
###8 - Research the following methods (*topologies*) for connecting devices to a network. In each case give a description and at least 1 advantage and 1 disadvantage.

**Bus Topology (6 marks)**
```
Describe:where nodes are connected in a daisy chain by a linear sequence of buses

Advantages:works well for small networks
easy to connect the computer

Disadvantages:entire network becomes down if the main cable is broken
becomes slow when more devices are added to the network
```

**Ring Topology (6 marks)**
```
Describe:This is where computers form a network by going in order through each one, so basicly they form a ring and to pass data around it has to go through all the computers
     ooooo
   oo     oo
  o         o
   oo     oo
     ooooo

Advantages:easy to setup and cheap

Disadvantages:if one computer is down the whole network is down, it is also slow and it has to go through all of the computers
```

**Star Topology (6 marks)**
```
Describe:computers connect to a central one to connect to each other

Advantages:better performance 
no disruptions to the network if there is more computers added

Disadvantages:if central computer is down so is network
if network is hacked do is network
```

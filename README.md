# CS325 Group Project

## To Run :

The main file used to run our implementation is the `tsp-2-opt.py` file. Each test file needs to be set up so that each city is it's own line, and includes the X and Y coordinates. 

Example test file:
```
0 200 800
1 3600 2300
...
49 5400 5750
50 5608 7103
```

Each time you run the algorithm, there is a hard cutoff time of 3 minutes unless otherwise noted. 

To run with a 3-minute time limit:
```python tsp-2-opt.py test-file.txt```

To run with no time limit:
```python tsp-2-opt.py test-file.txt inf```

This will output a file with the same name, with `.tour` appended to the end. This file will contain the length of the tour as the first line, then the actual tour following it. 


## Project Specification
Your group will research at least three different algorithms for solving the TSP problem. Each group member should research a different algorithm and provide pseudocode for that algorithm even if it is not implemented. There is much literature on methods to “solve” TSP please cite any sorces you use. You will design and implement at least one algorithm for finding the best tour you can for the TSP problem. TSP is not a problem for which you will be able to easily find optimal solutions. It is difficult. Your goal is to find the best solution you can in a certain time frame. Use any programming language you want that runs on flip2.engr.oregonstate.edu.

### Your program must:
- [x] Accept problem instances on the command line
- [x] Name the output file as the input file’s name with .tour appended (for example input tsp_example_1.txt will output tsp_example_1.txt.tour)
- [ ] Compile/Execute correctly and without debugging on flip2.engr.oreognstate.edu according to specifications and any documentation you provide.

### Input specifications:
- A problem instance will always be given to you as a text file.
- Each line defines a city and each line has three numbers separated by white space.
  - The first number is the city identifier
  - The second number is the city’s x-coordinate
  - The third number is the city’s y-coordinate.

### Output specifications:
- You must output your solution into another text file with n+1 lines, where n is the number of cities.
- The first line is the length of the tour your program computes.
- The next n lines should contain the city identifiers in the order they are visited by your tour.
  - Each city must be listed exactly once in this list.
  - This is the certificate for your solution and your solutions will be checked. If they are not valid you will not receive credit for them.

### Final Checklist:
- [x] Does your program correctly compute tour lengths for simple cases?
- [x] Does your program read input files and options from the command line?
- [x] Does your program meet the output specifications?
- [x] Did you check that you produce solutions that verify correctly?
- [x] Did you find solutions to the example instances?
- [x] Did you find solutions to the competition instances? Post your results to the competition discussion board to be eligible for extra-credit points.
- [x] Does your code compile/run without issue according to your documentation?
- [ ] Have you submitted your report to Canvas? In the comment section post the onid username of the person who submitted to TEACH.
- [ ] Have you submitted your report, your solutions to the test cases, your source code and README file to TEACH?

# TSP Project Team 6 - CS325 SU17 
Tyler B. McSilva, Sean J. Ng, Benjamin C. Rodarte

### Project Specification
Your group will research at least three different algorithms for solving the TSP problem. Each group member should research a different algorithm and provide pseudocode for that algorithm even if it is not implemented. There is much literature on methods to “solve” TSP please cite any sorces you use. You will design and implement at least one algorithm for finding the best tour you can for the TSP problem. TSP is not a problem for which you will be able to easily find optimal solutions. It is difficult. Your goal is to find the best solution you can in a certain time frame. Use any programming language you want that runs on flip2.engr.oregonstate.edu.

### To Run:
The main file used to run our implementation is the `tsp-2-opt.py` file. Each test file needs to be set up so that each city is it's own line, and includes the X and Y coordinates. 

Example test file:
```
0 200 800
1 3600 2300
...
49 5400 5750
50 5608 7103
```

Each time you run the algorithm, there is a hard cutoff time of 3 minutes unless otherwise noted. If the algorithm gets cut off at 3 minutes, the best tour it has found so far will be printed to the `.tour` file

To run with a 3-minute time limit:
```python tsp-2-opt.py test-file.txt```

To run with no time limit:
```python tsp-2-opt.py test-file.txt inf```

This will output a file with the same name, with `.tour` appended to the end. This file will contain the length of the tour as the first line, then the actual tour following it. 

*Side Note:* The implementation of Held-Karp is included to show our thought process. Currently the file only displays the tour length, but the code iteslf shows we were attempting to also provide the tour path. This file can be tested (with a small test case, less than 10 is optimal) using the command `python held_karp.py test-file.txt` and will print the length of the tour to the command line

### Results
The results of our NN/2-OPT algorithm are included in a folder labeled "2OPTResults"

### Final Checklist:
- [x] Does your program correctly compute tour lengths for simple cases?
- [x] Does your program read input files and options from the command line?
- [x] Does your program meet the output specifications?
- [x] Did you check that you produce solutions that verify correctly?
- [x] Did you find solutions to the example instances?
- [x] Did you find solutions to the competition instances? Post your results to the competition discussion board to be eligible for extra-credit points.
- [x] Does your code compile/run without issue according to your documentation?
- [x] Have you submitted your report to Canvas? In the comment section post the onid username of the person who submitted to TEACH.
- [x] Have you submitted your report, your solutions to the test cases, your source code and README file to TEACH?

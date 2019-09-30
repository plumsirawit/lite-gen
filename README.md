# LiteGen
A lightweight testcase generator application implemented using python.

### Prerequisites
- Python 3

### Installation
    git clone https://github.com/s6007589/lite-gen.git

### Instructions
1. Create sol.py as the problem's main solution.
2. Create gen.py as the testcase generator (retrieve inputs from stdin as a parameter in the input generation process).
3. Create conf.cfg as the testcase configuration. The config file consists of lines, each line describing a test case. In each line it could be anything, but the gen.py will read the only line as input to process.
4. Put sol.py, gen.py and conf.cfg in the same directory with litegen.py
5. Run python litegen.py (or python3 litegen.py)
6. Use the result.zip as the resulting zip (can be immediately imported into Cafe Grader)

### Example
Feel free to look at the "example" folder for example usage

### Contact
Author: Sirawit Pongnakintr

E-mail:
- plurm2545@hotmail.com
- s6007589@mwit.ac.th

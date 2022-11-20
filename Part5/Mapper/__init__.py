# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

def main(line) -> list:

"""
The mapper tokenize the line into words and reduce <word, 1> pairs. It will
take as input <line index,line string> and outputs list of pairs each pair 
<word,1>
"""


    result = list()
    L=line[1].split()
    for word in L:
        result.append((word,1))
    return result

# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

"""
The Reducer will take as input pairs of <word,[1,..,1]> and will give as
output <word,int>
"""

def main(input: dict) -> dict:
    reducer_result = dict()
    for word in input.keys():
        reducer_result[word] = len(input[word])
    return reducer_result

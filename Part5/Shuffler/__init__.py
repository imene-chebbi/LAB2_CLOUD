# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(input) -> dict:
    """
    The shuffler will take as input list of <word,1> and will return as
    output <word,[1,..,1]>
    """
    shuffler_result = dict()
    for word in input :
        if not result.get(word[0]) :
            shuffler_result[word[0]] = list()
        shuffler_result[word[0]].append(word[1])
    return shuffler_result

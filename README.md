# Generative AI Code Reuse Assessment

## Overview

This repository contains a Python script and a JSON file designed to assess the code reuse capabilities of Generative AI models, specifically GPT-3.5-turbo by OpenAI. The primary goal is to generate specific coding problems and automatically evaluate the quality of the code produced by the AI model, focusing on its ability to reuse existing code. Some of the tests are not particularly novel, but the code reuse problem is novel. As a result, our testing shows that ChatGPT passes all tests for functionality, but occasionally fails tests for code reuse (resulting in a score of 7/8 for a particular problem).

## Structure

- `gpt3.5-script.py`: The main Python script that interacts with the OpenAI API to get the generated code and runs the test suite on it.
- `code-reuse-problems-and-tests.json`: JSON file containing a set of auto-generated coding problems and their associated tests that the script uses.

## How It Works

1. The script first loads a set of coding problems from a JSON file. Each problem contains two function descriptions and prototypes—one for a base function and another for a child function that should reuse the code of the base function.

2. For each problem, the script sends a prompt to the OpenAI GPT-3.5-turbo model to generate the Python code for both functions.

3. The generated code is then executed and tested using a test suite that is also part of the problem definition in the JSON file.

4. Each test suite checks the functionality of both the base and child functions and also includes a check for code reuse.

5. Finally, the script calculates and prints out the total score, which serves as the assessment of the AI model's code reuse capabilities.

## Notes about prompting
There are a few interesting things to note about the way that GPT-3.5-turbo is prompted. 

- We explicitly do not mention code reuse in the prompts because we want to test GPT's ability to adhere to good programming practices without explicit instruction (modeling a software engineer using AI to help program in practice). 

- We explicitly instruct GPT not to import any libraries, because many problems could be solved without effort or code reuse using libraries. 

- Lots of work went into finding the best prompt to ensure that GPT only returns executable code without any additional words so that the code can be automatically tested. 

- We include function prototypes in the prompt to ensure that the testing scripts can be run correctly

- When given these specific prompting instructions, our initial results indicated that GPT was very bad at code reuse. However, changing the prompt from "Generate Python code..." to "Generate a Python file..." helped to encourage code reuse by implying that all of the code GPT generated would be included in a single file, allowing code reuse.

## How to Run the Script

1. Install the OpenAI Python package by running `pip install openai`.

2. Replace the `api_key` in `gpt3.5-script.py` with your actual OpenAI API key.

3. Run `python3 gpt3.5-script.py`

4. The script will print the test results and the final total score.

## Dependencies

- Python 3.x
- OpenAI Python package

## Note

The score is out of 8 points for each problem: 4 points for the base function, 3 for the child function, and 1 for code reuse.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

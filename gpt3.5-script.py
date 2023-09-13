import openai
import json

# Your OpenAI API key here
api_key = "Your Key Here"

# Initialize the OpenAI API client
openai.api_key = api_key

# Load the new, more specific set of generated problems
with open("code-reuse-problems-and-tests.json", "r") as f:
    problems = json.load(f)

# Initialize the total score
total_score = 0
total_reuse_score = 0

# Iterate through each problem
for i, problem in enumerate(problems):
    base_function_desc = problem['base_function_desc']
    base_function_prototype = problem['base_function_prototype']
    child_function_desc = problem['child_function_desc']
    child_function_prototype = problem['child_function_prototype']
    test_suite = problem['test_suite']
    
    # Create the prompt for GPT-3.5-turbo
    system_prompt = "You will act as a code generator. Generate Python code based on the function descriptions and prototypes provided. Assume that all functions are located in the same file and do not use any import statements. The output should be executable Python code only, without comments or extra text."
    prompt = f"{base_function_desc}\n\nPrototype: {base_function_prototype}\n\n{child_function_desc}\n\nPrototype: {child_function_prototype}"
    
    # Make the API call to get the code
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}]
    )

    generated_code = completion.choices[0].message['content']

    # Initialize score for this problem
    score = 0
    reuse_score = 0
    
    # Execute the generated code and the test suite
    try:
        exec(generated_code, globals())
        exec(test_suite, globals())
        
        # Call the test function to get the score
        test_function_name = f"test_functions_{i+1}"
        if test_function_name in globals():
            score, reuse_score = globals()[test_function_name]()
        else:
            print(f"Test function {test_function_name} not found.")
    except Exception as e:
        print(f"An error occurred while testing problem {i + 1}: {e}")
    
    # Update the total score
    total_score += score
    total_reuse_score += reuse_score

    print(f"Problem {i + 1} Test Results: Total score is {score}/7, Reuse score is {reuse_score}/1")

# Print the final total score
print(f"Final Score: {total_score}/{7 * len(problems)}")
print(f"Final Reuse Score: {total_reuse_score}/{len(problems)}")

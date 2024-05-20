import replicate
import os

os.environ["REPLICATE_API_TOKEN"]="r8_c8rnecR4e94Q0gOyWvtyxBgwMCVZmgX45ZfQh"

# Prompts
pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
prompt_input = "What is Streamlit?"

# Generate LLM response
output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
                       input={"prompt": f"{pre_prompt} {prompt_input} Assistant: ",
                            "temperature":0.1, "top_p":0.9, "max_length":128, "repetition_penalty":1})

full_response = ""
for item in output:
    full_response += item

print(full_response)
from litellm import completion, supports_function_calling, supports_response_schema
from config import MODEL
print("MODEL:", MODEL)
print("supports function calling:", supports_function_calling(model=MODEL))
print("supports response schema:", supports_response_schema(model=MODEL))

# minimal request
r = completion(model=MODEL, messages=[{"role":"user","content":"Say hi in 3 words"}], max_tokens=20)
print("OK:", r.choices[0].message["content"])

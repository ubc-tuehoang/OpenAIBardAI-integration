from file_reader import read_file
from bardapi import Bard
import requests
import json
import time

# Specify the file path
file_path = 'inputfile1.in'  # Replace 'path_to_your_file.txt' with your file path

# Call the function to read the file and store its contents in a variable
file_contents = read_file(file_path)

##Secure-1PSID
token = 'BARD-AI Token'

bard = Bard(token=token)
#queryString = "PRIME WITH **Core courses for business*** COMM 101 - Business Fundamentals: grade above 90 then move on to COMM 291; grade between 85 and 90 student can move to COMM 291A; grade between 70 and 85 student can move to COMM 291B, else repeat COMM 101* COMM 291 - Application of Statistics in Business: grade above 90 then move on to COMM 292; grade between 85 and 90 student can move to COMM 292A; grade between 70 and 85 student can move to COMM 292B, else repeat COMM 291* COMM 291A - Application of Statistics in Business* COMM 291B - Application of Statistics in Business* COMM 292 - Management and Organizational Behaviour: grade above 70 then move on to ECON 101 or MATH 104; else repeat COMM 291* COMM 292A - Application of Statistics in Business * COMM 292B - Application of Statistics in Business * ECON 101 - Principles of Microeconomics * MATH 104 - Differential Calculus with Applications to Commerce and Social Sciences * OVERALL average of COMM 101, COMM 291 and COMM 292 between 75 and 90, the student can only take MINOR of ECON * OVERALL average of COMM 101, COMM 291 and COMM 292 above 90, the student can move to a quantitative MAJOR in sauder such as Accounting, Finance, BTM, Supply chain and logistics" 
queryString = file_contents

out = bard.get_answer(queryString)['content']
print (out)

##====================
print("=====================================")

time.sleep(5)

url = "https://api.openai.com/v1/chat/completions"

##"model": "gpt-3.5-turbo",

payload = json.dumps({
  "model": "gpt-4",
  "messages": [
    {
      "role": "system",
      "content": "You are a financial advisor."
    },
    {
      "role": "user",
      "content": "Provide recommendation and projection and forecast for the following: "+out
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <OPENAI Token>'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


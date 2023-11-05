from bardapi import Bard
import requests
import json
import time

##Secure-1PSID
token = 'cAiYbRlzRcOtLci8ntX4DbABayA--9V9y8HKQj7T3JALHbJHz3CmcKv6PLmuA3mIYMRRCQ.'
token = 'cAiYbRlzRcOtLci8ntX4DbABayA--9V9y8HKQj7T3JALHbJHz3CmcKv6PLmuA3mIYMRRCQ.'
token = 'cAiYbRlzRcOtLci8ntX4DbABayA--9V9y8HKQj7T3JALHbJHz3CmcKv6PLmuA3mIYMRRCQ.'
token = 'cwiYbbrS82T4J3T8ydjzpcec_YdwRuH7GJD5jHPkB2HrQqdVM-MxtjLRQchAkWnT7Xx6NQ.'
bard = Bard(token=token)
queryString = "PRIME WITH **Core courses for business*** COMM 101 - Business Fundamentals: grade above 90 then move on to COMM 291; grade between 85 and 90 student can move to COMM 291A; grade between 70 and 85 student can move to COMM 291B, else repeat COMM 101* COMM 291 - Application of Statistics in Business: grade above 90 then move on to COMM 292; grade between 85 and 90 student can move to COMM 292A; grade between 70 and 85 student can move to COMM 292B, else repeat COMM 291* COMM 291A - Application of Statistics in Business* COMM 291B - Application of Statistics in Business* COMM 292 - Management and Organizational Behaviour: grade above 70 then move on to ECON 101 or MATH 104; else repeat COMM 291* COMM 292A - Application of Statistics in Business * COMM 292B - Application of Statistics in Business * ECON 101 - Principles of Microeconomics * MATH 104 - Differential Calculus with Applications to Commerce and Social Sciences * OVERALL average of COMM 101, COMM 291 and COMM 292 between 75 and 90, the student can only take MINOR of ECON * OVERALL average of COMM 101, COMM 291 and COMM 292 above 90, the student can move to a quantitative MAJOR in sauder such as Accounting, Finance, BTM, Supply chain and logistics" 

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
      "content": "You are university advisor."
    },
    {
      "role": "user",
      "content": "Provide recommendation for student that got 88 in COMM 101, 89 in COMM 291, 99 in COMM 292 "+out
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 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'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


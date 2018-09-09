import json
import grequests
import jsondiff
def TestGet(url, body, headers):
    unsent_request = [grequests.post(url, data=json.dumps(body), headers=headers)]
    results = grequests.map(unsent_request, gtimeout=(720))
    return results[0]

def validator(res, expected, no):

    if res.status_code == 200:
        response = json.loads(res.content)
        response.pop("_id")
        d = jsondiff.diff(expected, response)
        if d == {}:
            print "Test case passed-{}".format(no)
        else:
            print "Test case failed-{}".format(no)

    elif res.status_code == 400:
        response = json.loads(res.content)
        d = jsondiff.diff(expected, response)
        if d == {}:
            print "Negative test case passed-{}".format(no)
        else:
            print "Negative test case failed-{}".format(no)

if __name__ == "__main__":

    url = "http://localhost:5000/persons/contact/create"

    body = {
        "emailid": "krish@abc.xyz",
        "lastname": "krish",
        "firstname": "krish",
        "phone": ["+91-7674935197"]
    }

    headers =  {
        "Content-Type": "application/json",
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJhbSIsInBhc3N3b3JkIjoicmFtIiwiZXhwIjoxNTM2NTc3NDc1fQ.Y5ePPr6mv_NVYt62CDABqA03RxNwpU-v3kJcJV9QwV8"
    }

    url1 = "http://localhost:5000/persons/contact/create"

    body1 = {
        "emailid": "grish@abc.xyz",
        "lastname": "grish",
        "firstname": "grish",
        "phone": ["+91-7674935197"]
    }

    headers1 = {
        "Content-Type": "application/json",
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJhbSIsInBhc3N3b3JkIjoicmFtIiwiZXhwIjoxNTM2NTc3NDc1fQ.Y5ePPr6mv_NVYt62CDABqA03RxNwpU-v3kJcJV9QwV8"
    }

    res = TestGet(url, body, headers)
    res1 = TestGet(url1, body1, headers1)

    validator(res, body, 1)
    validator(res1, body1, 2)

    expected = {"message":"contact already exist"}

    validator(res, expected, 1)
    validator(res1, expected, 2)



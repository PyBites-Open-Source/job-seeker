import json

#from job_seeker.downloader import JobSeeker

# set parameters

parameters = {
    "where": "All Adelaide SA",
    "keywords": "data analyst",
}

# instantiate class

#js = JobSeeker(params=parameters)

#details = js.get_jobs_detail_json()

# with open("response_details.json", "w+") as fp:
#     json.dump(details, fp=fp)

with open("response_details.json", "r+") as fp:
    details =json.load(fp=fp)

first_forty = details[:40]

# print(len(first_forty))

# print(len(first_forty[:20]))
# print(len(first_forty[20:]))

from pathlib import Path

parent = Path(__file__).absolute().parent.parent


with open( parent / "tests/data/response.json" , "r+") as fp:
    response = json.load(fp)

create_2_pages = list()
for i in range(2):
    response["page"] = i+1
    create_2_pages.append({"page": i+1, "content": response})    

print(len(create_2_pages))


final_response = list()

for i, (job, det) in enumerate(zip(create_2_pages[0]["content"]["data"], first_forty[:20])):
    create_2_pages[0]["content"]["data"][i]["id"] = det["id"]

for i, (job, det) in enumerate(zip(create_2_pages[1]["content"]["data"], first_forty[20:])):
    create_2_pages[1]["content"]["data"][i]["id"] = det["id"]

ids = []
for page in create_2_pages:
    for job in page["content"]["data"]:
        ids.append(job["id"])

ids_det = [i["id"] for i in first_forty]

print(len(ids))
print(len(ids_det))

for i, ie in zip(ids, ids_det):
    assert i in ids_det
        
with open("new_response.json", "w+") as fp:
    json.dump(create_2_pages, fp)

short = {str(i["id"]):i for i in first_forty}
    
with open("response_detail_short.json", "w+") as fp:
    json.dump(short, fp)
    

#print(create_2_pages)


# test20 = [job["id"] for job in response["data"]]

# print(test20)


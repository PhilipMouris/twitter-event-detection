import json
import os

classes = ["Culture", "Finance", "Medical", "Politics", "Religion", "Sports", "Tech"]
sources = ["akhbarona", "arabiya", "khaleej"]

def combine_dataset(x):
    result = []
    for source in sources:
        for c in classes:
            directory = "sanad dataset/" + source + "/" + x + "/" + c
            if os.path.isdir(directory):
                for filename in os.listdir(directory):
                    print(directory + "/" + filename)
                    file = open(directory + "/" + filename,"r")
                    text = file.read()
                    result_class = c
                    if c == "Culture" or c == "Tech":
                        result_class = "Other"
                    result.append({
                        "article": text,
                        "class": result_class
                    })
                    file.close()
    with open("combined_" + x.lower() + "_dataset.json", "w", encoding="utf8") as outfile:
        json.dump(result, outfile, indent=4, ensure_ascii=False)

combine_dataset("Train")
combine_dataset("Test")

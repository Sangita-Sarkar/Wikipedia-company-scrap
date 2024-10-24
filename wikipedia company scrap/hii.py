import json


company_data = {
    "https://www.nvidia.com": {
        "trade name": "NVIDIA",
        "company type": "Public",
        "industry": "Technology",
        "headquarters": "Santa Clara, California",
        "description": "NVIDIA is a technology company known for its graphics processing units (GPUs)."
    },
    "https://www.apple.com": {
        "trade name": "Apple Inc.",
        "company type": "Public",
        "industry": "Technology",
        "headquarters": "Cupertino, California",
        "description": "Apple Inc. is known for its consumer electronics, software, and services."
    },
    "https://www.microsoft.com": {
        "trade name": "Microsoft Corporation",
        "company type": "Public",
        "industry": "Technology",
        "headquarters": "Redmond, Washington",
        "description": "Microsoft is a multinational technology company that develops software, electronics, and personal computers."
    },
    "https://www.samsung.com":{
            "trade name": "Samsung Electronics",
            "company type": "Public",
            "industry": "Technology",
            "headquarters": "Suwon, South Korea",
            "description": "Samsung Electronics is a global leader in consumer electronics and home appliances."
        },
         "https://www.coca-cola.com":{
            "trade name": "Coca-Cola Company",
            "company type": "Public",
            "industry": "Beverages",
            "headquarters": "Atlanta, Georgia, USA",
            "description": "Coca-Cola is a beverage company best known for its flagship product, Coca-Cola, and other soft drinks."

  },
        "https://www.ibm.com": {
            "trade name": "IBM Corporation",
            "company type": "Public",
            "industry": "Technology",
            "headquarters": "Armonk, New York, USA",
            "description": "IBM is a multinational technology company that provides hardware, software, and cloud services."
        },
        "https://www.tesla.com": {
            "trade name": "Tesla, Inc.",
            "company type": "Public",
            "industry": "Automotive",
            "headquarters": "Palo Alto, California, USA",
            "description": "Tesla is an electric vehicle and clean energy company known for its innovation in sustainable transport."
        },
         "https://www.facebook.com":{
            "trade name": "Facebook, Inc.",
            "company type": "Public",
            "industry": "Technology",
            "headquarters": "Menlo Park, California, USA",
            "description": "Facebook is a social media platform that allows users to connect, share content, and communicate online."
        },
        "https://www.amazon.com" : {
            "trade name": "Amazon.com, Inc.",
            "company type": "Public",
            "industry": "E-commerce",
            "headquarters": "Seattle, Washington, USA",
            "description": "Amazon is the largest online retailer in the world, providing a marketplace for goods, digital streaming, and cloud computing services."
        },
       "https://www.google.com" : {
            "trade name": "Google LLC",
            "company type": "Public",
            "industry": "Technology",
            "headquarters": "Mountain View, California, USA",
            "description": "Google is a global technology company that specializes in Internet-related services and products, including search engines, online advertising, cloud computing, and software."
        }}

def get_company_info(url):
    return company_data.get(url, "No data available for the entered URL.")


url_input = input("Enter a URL : ")
result = get_company_info(url_input)


print(json.dumps(result, indent=4))

"""
This script reads the integrations/integrations.js file and generates the list of data collection integrations inside collectors/COLLECTORS.md, with proper links that Learn can replace into Learn links.
"""

import json
import pathlib

# Open integrations/integrations.js and extract the dictionaries
with open('integrations/integrations.js') as dataFile:
    data = dataFile.read()

    categories_str = data.split("export const categories = ")[1].split("export const integrations = ")[0]
    integrations_str = data.split("export const categories = ")[1].split("export const integrations = ")[1]

    categories = json.loads(categories_str)
    integrations = json.loads(integrations_str)

cat_dict = {}
data_col_cat = {}


def recursive(categories):
    for category in categories:
        data_col_cat[category['id']] = category['name']
        if category['children']:
            recursive(category['children'])


recursive(categories[1]['children'])


def construct_dict(array, integration):
    for element in array:
        if element not in cat_dict:
            cat_dict[element] = list()
        cat_dict[element].append(integration)


md = ""

for integration in integrations:
    if integration['integration_type'] == "collector":
        construct_dict(integration['meta']['monitored_instance']['categories'], integration)


for category_id, integrations in sorted(cat_dict.items()):
    heading = '#' * len(category_id.split('.'))

    for cat in data_col_cat:
        if cat == category_id:
            name = data_col_cat[cat]

    md += f'#{heading} {name}\n\n'
    names = []
    for integration in integrations:
        name = integration['meta']['monitored_instance']['name']
        link = integration['edit_link'].replace("metadata.yaml", "") + \
            "integrations/" + name.lower().replace(" ", "_").replace("/", "-").replace("(", "").replace(")", "")+".md"
        names.append(f"[{name}]({link})")
    for integration_name in sorted(names):
        md += "- " + integration_name + "\n\n"


outfile = pathlib.Path("./collectors/COLLECTORS.md")
output = outfile.read_text().split("## Available Data Collection Integrations")[0]
output += "## Available Data Collection Integrations\n<!-- AUTOGENERATED PART BY integrations/gen_doc_collector_page.py SCRIPT, DO NOT EDIT MANUALLY -->\n" + md
outfile.write_text(output.rstrip('\n')+"\n")

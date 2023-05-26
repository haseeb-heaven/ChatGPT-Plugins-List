import json
import sys
from tabulate import tabulate

def check_plugin(name):
    plugins_list = []
    with open('plugins.json', 'r') as f:
        data = json.load(f)
        plugins = data['plugins']
        for plugin in plugins:
            if name.lower() in plugin['Name'].lower() or name.lower() in plugin['Description'].lower():
                plugins_list.append(plugin)
    return plugins_list

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a keyword as an argument.")
    else:
        name = sys.argv[1]
        plugins = check_plugin(name)
        if len(plugins) > 0:
            table_data = [["Name", "Description"]]
            for plugin in plugins:
                table_data.append([plugin['Name'], plugin['Description']])
            print(tabulate(table_data, headers='firstrow', tablefmt='grid'))
        else:
            print(f"No plugins found matching the keyword: {name}")

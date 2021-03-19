import json
import speak

jsonFile = open('./json_data/Periodic_table.json', 'r', encoding='utf8')
values = json.load(jsonFile)
jsonFile.close()

element_object = {}


def el_lookup(chem_element):
    for i in values["elements"]:
        if chem_element == i["name"]:
            speak.jarvis_speak('In summary ' + i["summary"] + ' The appearance is ' + i["appearance"] +
                               '. The category is ' +
                               i["category"] + '. It was discovered by ' + i["discovered_by"])

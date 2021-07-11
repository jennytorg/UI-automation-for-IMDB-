import xml.etree.ElementTree as ET

class get_data_method(object):

    def get_data(self, node_name):
        try:
            ### DEBUG STATUS ONLY - change the path ###
            #root = ET.parse('./TestCases/configuration.xml').getroot()
            
            ### RUN PEYTEST - path in the same directory###
            root = ET.parse('./configuration.xml').getroot()
            return root.find(".//" + node_name).text

        except Exception as e:
            return{
                "result": "error",
                "message" : f"get_data returned {e}" 
            }


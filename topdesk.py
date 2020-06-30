from Tools import tools_v000 as tools
import os
from os.path import dirname


# -7 for the name of this project Topdesk
save_path = dirname(__file__)[ : -7]
propertiesFolder_path = save_path + "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'Topdesk', 'user_text=')
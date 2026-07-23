from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt
from warbreaker_appearance_data_cleanup import WarbreakerAppearanceData



################################################################################################
wb = WarbreakerAppearanceData()
character_apps, character_list = wb.character_apps, wb.character_list

################################################################################################
# raster plot

raster_data = []
for char in character_list:
    raster_data.append(np.array(character_apps[char]))

fig, ax = plt.subplots(figsize=(15, 20))
ax.eventplot(raster_data, linelengths=0.7, orientation='horizontal', linewidths=10)
y_pos = [x for x in range(len(raster_data))]
ax.set_yticks(y_pos)
ax.set_yticklabels(character_list)
plt.show()
# plt.savefig("Warbreaker_raster")





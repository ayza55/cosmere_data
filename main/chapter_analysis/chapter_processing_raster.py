from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt
from appearance_data import AppearanceData



################################################################################################
wb = AppearanceData(Path(__file__).parent / "data_collection_chapter" / "character_freq_data_general_Warbreaker.json")
character_apps, character_list = wb.character_apps, wb.character_list

################################################################################################
# raster plot
maxim = max([sum(character_apps[x]) for x in character_apps.keys()])
raster_data = []
for char in character_list:
    raster_data.append(np.array(character_apps[char]))

label_list = [i if sum(character_apps[i]) > maxim//3 else None for i in character_list]
fig, ax = plt.subplots(figsize=(10, 40))
y_pos = [4*i for i in range(len(character_list))]
ax.eventplot(raster_data, linelengths=3.5, orientation='horizontal', linewidths=7, lineoffsets= y_pos)
ax.set_yticks(y_pos)
ax.set_yticklabels([])
#ax.set_yticklabels(label_list)
plt.savefig("Warbreaker_raster_fin.png")
plt.show()





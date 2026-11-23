import os

JOKE = "At dinner my three kids asked why Dad stands guard at the grill in the rain instead of eating with us, and I said somebody in this family has to keep the steaks high."

os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(JOKE)

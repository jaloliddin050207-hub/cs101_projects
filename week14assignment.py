def catalog_animals(tag_data):
    catalog = {}
    for animal in tag_data:
        catalog[animal['chip_id']] = animal['species']
    return catalog

def process_sightings(animal_catalog, detected_chips):
    catalog_ids = set(animal_catalog.keys())
    detected_ids = set(detected_chips)

    unseen_animals = catalog_ids - detected_ids
    unknown_signals = detected_ids - catalog_ids

    return unseen_animals, unknown_signals

def alert_missing(animal_catalog, unseen_set):
    report = [
        "NOT SEEN: " + animal_catalog[chip] + " (ID: " + chip + ")"
        for chip in unseen_set
    ]
    return sorted(report)

tags = [
    {'chip_id': "WOLF-01", 'species': "Grey Wolf"},
    {'chip_id': "BEAR-09", 'species': "Brown Bear"},
    {'chip_id': "DEER-55", 'species': "Elk"}
]

sightings = ["WOLF-01", "DEER-55", "UFO-99"]

catalog = catalog_animals(tags)
unseen, unknown = process_sightings(catalog, sightings)
report = alert_missing(catalog, unseen)

print("Unseen Animals:", unseen)
print("Unknown Signals:", unknown)
print("Report:", report)
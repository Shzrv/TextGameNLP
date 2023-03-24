def describe(location_descr_path):
    with open(location_descr_path) as d:
        print(d.read())


describe("Locations/Space_Station.txt")
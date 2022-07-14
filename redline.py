red_line_stops = ["Howard", "Jarvis", "Morse", "Loyola", "Granville", "Thorndale", "Bryn Mawr", "Argyle", "Wilson", "Sheridan", "Addison", "Belmont", "Fullerton", "North/Clybourn", "Clark/Division", "Chicago", "Grand", "Lake", "Monroe", "Jackson", "Harrison", "Roosevelt", "Cermak-Chinatown", "Sox-35th", "47th", "Garfield", "63rd", "69th", "79th", "87th", "95th/Dan Ryan"]
def find_position(station,train_line):
    for i in range(len(train_line)):
        if train_line[i]==station:
            return i

find_position("Loyola", red_line_stops)

def distance(station1, station2, train_line):
    return abs(find_position(station2, train_line)-find_position(station1, train_line))


def run(train_line):
    station1 = input("Enter station 1 ")
    print(station1)
    if station1 not in train_line:
        run(train_line)
    station2 = input("Enter station 2 ")
    if station2 not in train_line:
        run(train_line)
    print(station2)
    print(distance(station1,station2,train_line))

run(red_line_stops)



red_line_stops = ["Howard", "Jarvis", "Morse", "Loyola", "Granville", "Thorndale", "Bryn Mawr", "Argyle", "Wilson", "Sheridan", "Addison", "Belmont", "Fullerton", "North/Clybourn", "Clark/Division", "Chicago", "Grand", "Lake", "Monroe", "Jackson", "Harrison", "Roosevelt", "Cermak-Chinatown", "Sox-35th", "47th", "Garfield", "63rd", "69th", "79th", "87th", "95th/Dan Ryan"]
green_line = ["Oak Park (Green)","Harlem/Lake","Ridgeland","Austin (Green)","Central (Green)","Laramie","Cicero (Green)","Pulaski (Green)","Conservatory-Central Park Drive","Kedzie-Green","California-Green","Ashland-Lake","Morgan-Lake","Clinton (Green/Pink)","Clark/Lake","State/Lake","Washington/Wabash","Adams/Wabash","Roosevelt","Cermak-Mccormick Place","35th-Bronzeville-Iit","Indiana","43rd","47th (Green)","51st","Garfield (Green)","King Drive","East 63rd-Cottage Grove"]

def find_idx_of (to_find, lst):
    for i in range(len(lst)):
        if lst[i] == to_find:
            return i
    return None
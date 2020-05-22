import re


def make_states():
    states = []
    file = open("states.txt")
    for line in file:
        states.append(line.strip())
    file.close()

    file = open('insert_states.sql', 'w')
    for state in states:
        cmd = 'insert into state (name) values (\'' + state + '\');\n'
        file.write(cmd)
    file.close()


def make_committees():
    committees = []
    comms_w_date = []
    prefixes = [chamb + ' ' for chamb in ['House', 'Senate', 'Joint']]
    i = 0
    f = open('committees.txt')
    for line in f:
        line = line.strip().split('; ')
        if line == ['']:
            i += 1
        elif len(line) == 1:
            committees.append(prefixes[i] + line[0])
        else:
            comms_w_date.append((prefixes[i] + line[0], line[1]))
    f.close()

    f = open('insert_committees.sql', 'w')
    for comm in committees:
        f.write('insert into committee(name) values (\'' + comm + ' Committee\');\n')
    for comm, date in comms_w_date:
        f.write('insert into committee values(\'' + comm + ' Committee\',  ' + date + ');\n')


def make_house_districts():
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    f = open('./textToParse/current_house.txt')
    f2 = open('./sqlCommands/insert_districts.sql', 'w')
    for rep in f.read().split('|-')[1:]:
        state, dist = rep.split('|')[2:4]
        f2.write('insert into district(state, name, chamber) values(\'' + states[state]
                 + '\',\'HR-' + state + '-' + dist + '\',\'House\');\n')
    f.close()
    f2.close()


def make_house_reps():
    fr = open('./textToParse/current_house.txt', 'r')
    fw = open('./sqlCommands/make_house.sql', 'w')

    for rep in fr.read().split('|-')[1:]:
        try:
            (_, dist, name, _, _, party, _, education, _, _, year_born) = rep.split('| ')
            (_, state, dist, _) = dist.split('|')
            dist = 'HR-' + state + '-' + dist
            i = name.find('"')
            if name.find(',') == -1:
                name = name[i + 1:-2].split(' ')
                if len(name) == 2:
                    last, first = name
                else:
                    _, last, first = name
            else:
                last, first = name[i + 1:-2].split(', ')
            party = party.strip().lower()
            if party == 'democratic':
                party = 'democrat'
            education = re.findall('\[.*?\]', education)
            year_born = year_born.strip()
            if education:
                education = education[0][2:-1].split('|')[0]
                cmd = 'insert into representative(district, congress_number, last, first, party, year_born, education)'\
                      ' values(\'' + dist + '\', ' + str(115) + ', \'' + last + "', '" + first + "', '" + \
                      party + "', " + str(year_born) + ", '" + education + "');\n"
            else:
                cmd = 'insert into representative(district, congress_number, last, first, party, year_born)' + \
                      ' values(\'' + dist + '\', ' + str(115) + ', \'' + last + "', '" + first + "', '" + \
                      party + "', " + str(year_born) + ");\n"
            fw.write(cmd)
        except ValueError:
            pass

    fr.close()
    fw.close()


if __name__ == '__main__':
    # make_states()
    # make_committees()
    # make_house_reps()
    pass

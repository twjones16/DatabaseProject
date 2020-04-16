import psycopg2
import gc
from typing import Tuple, List


def connect():
    try:
        conn = psycopg2.connect(
            dbname='finalproject_tim_jack',  # kwargs
            user='jepatt16',
            host='cs-linuxlab-02.stlawu.local',
            password='  '
        )
        gc.collect()
        return conn
    except psycopg2.Error:
        gc.collect()
        exit()


def enter_votes(fname: str, congress_number: int, bill_number: str, cur):
    def readnames(fn: str) -> Tuple[List[Tuple[str, str]],
                                    List[Tuple[str, str, str]],
                                    List[Tuple[str, str, str]],
                                    List[Tuple[str, str, str, str]]]:
        last_only = []
        first_last = []
        last_state = []
        first_last_state = []
        votes = ['yea', 'nay', 'no vote']
        i = 0
        fr = open(fn, 'r')
        for line in fr:
            if line.strip() == '':
                i += 1
            else:
                line = line.split(', ')
                first = None
                state = None
                if len(line) == 1:
                    last = line[0].strip()
                else:
                    last = line[0].strip()
                    first = line[1].strip()
                j = last.find('(')
                if j != -1:
                    state = last[j + 1:-1].strip()
                    last = last[:j-1].strip()
                if not (first or state):
                    last_only.append((last, votes[i]))
                elif not first:
                    last_state.append((last, state, votes[i]))
                elif not state:
                    first_last.append((first, last, votes[i]))
                else:
                    first_last_state.append((first, last, state, votes[i]))
        return last_only, last_state, first_last, first_last_state

    def match_names_to_rep():
        (last_only, last_state, first_last, first_last_state) = readnames(fname)
        for last, vote in last_only:
            cmd = 'select district from representative where last = \'' \
                  + last + '\' and congress_number = ' + str(congress_number)

            cur.execute(cmd)
            lst = cur.fetchall()
            for line in lst:
                cmd = "insert into vote(district, congress_number, bill_number, vote) values ('" + line[0] \
                    + "', " + str(congress_number) + ", '" + bill_number + "', '" + vote + "')"
                cur.execute(cmd)

    match_names_to_rep()


if __name__ == '__main__':
    connection = connect()
    c = connection.cursor()

    enter_votes('bipartisan_background_checks_votes.txt', 115, 'HR8', c)

    connection.commit()
    connection.close()


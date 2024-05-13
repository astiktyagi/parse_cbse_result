import csv
COLNAMES = ["ROLL NO", "NAME", "SUB-1", "SUB-2", "SUB-3", "SUB-4", "SUB-5", "SUB-6",  "GR1", "GR2", "GR3", "RES", "COMP"]
ALL_DATA = {}




def find_sub_starting_index(row_data):
    for i in range(1, len(row_data)):
        if len(row_data[i]) == 3 and row_data[i].isdigit():
            return i


def parse():
    path = r"C:\Users\Astik Tyagi\Downloads\27263.txt"
    school_name = None
    second_line = False
    print(','.join(COLNAMES))
    with open(r"C:\Users\Astik Tyagi\Downloads\Parsed.csv", 'wt', newline='') as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(COLNAMES)
    
        with open(path) as f:
                for curr_line in f.readlines():
                    if curr_line:

                        if "PAGE:-" in curr_line:
                            school_name = ""

                        if curr_line.startswith("-"):
                            school_name = ""

                        if curr_line.startswith("SCHOOL : -"):
                            school_name = curr_line.replace("SCHOOL : -", "").strip()
                            continue

                        if not school_name:
                            continue

                        row_data = curr_line.split()
                        if row_data:

                            if second_line:
                                # assert len(row_data) == 12
                                temp_second_line = [
                                    "-".join([row_data[i], row_data[i + 1]])
                                    for i in range(0, 12, 2)
                                ]
                                temp_second_line = ["", ""] + temp_second_line
                                print(temp_second_line)
                                writer.writerow(temp_second_line)
                                second_line = False
                            else:
                                roll_no = row_data[0]
                                sub_index = find_sub_starting_index(row_data)
                                name = " ".join(row_data[1:sub_index])
                                sub1 = row_data[sub_index]
                                sub2 = row_data[sub_index + 1]
                                sub3 = row_data[sub_index + 2]
                                sub4 = row_data[sub_index + 3]
                                sub5 = row_data[sub_index + 4]
                                sub6 = row_data[sub_index + 5]
                                gr1 = row_data[sub_index + 6]
                                gr2 = row_data[sub_index + 7]
                                gr3 = row_data[sub_index + 8]

                                res_sub_index = find_sub_starting_index(row_data[sub_index + 9:])
                                if res_sub_index:
                                    res = ' '.join(row_data[sub_index + 9: sub_index + 9 + res_sub_index])
                                    comp = ' '.join(row_data[sub_index + 9 + res_sub_index:])
                                else:
                                    res = ' '.join(row_data[sub_index + 9:])
                                    comp = ''

                                FIRST_LINE = [
                                    roll_no,
                                    name,
                                    sub1,
                                    sub2,
                                    sub3,
                                    sub4,
                                    sub5,
                                    sub6,
                                    gr1,
                                    gr2,
                                    gr3,
                                    res,
                                    comp
                                ]

                                print(FIRST_LINE)
                                writer.writerow(FIRST_LINE)
                                
                                second_line = True


if __name__ == "__main__":
    parse()

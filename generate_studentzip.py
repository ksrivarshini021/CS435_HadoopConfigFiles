# Author: Changsoo Jung
# Date: 2024-01-17
# Description:
#   The machines_and_ports.txt file will contain the machine names & port numbers, 
#   and the machine names & port numbers will be used to update a student's 
#   configuration files for Hadoop and Spark.

import os
import json

def read_csv(csv_file):
    with open(csv_file, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines
    # Error handling
    return None

def read_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        return data
    # Error handling
    return None

def assign_machines_and_ports(student_list, machines, ports):
    # Assign machines and ports to each student
    # Here is the pattern of the machine names and ports when group_size = 3
    # student1: machine1, machine2, machine3, machine4, machine5, machine6, machine7, machine8, portA
    # student2: machine2, machine3, machine4, machine5, machine6, machine7, machine8, machine1, portB
    # student3: machine3, machine4, machine5, machine6, machine7, machine8, machine1, machine2, portC
    # student4: machine9, machine10, machine11, machine12, machine13, machine14, machine15, machine16, portA
    # student5: machine10, machine11, machine12, machine13, machine14, machine15, machine16, machine9, portB
    # student6: machine11, machine12, machine13, machine14, machine15, machine16, machine9, machine10, portC
    student_data = {}
    group_size = len(student_list) // len(machines) + 1
    
    for idx, student in enumerate(student_list):
        student_data[student] = []
        group_idx = idx // group_size
        group_machines = machines[str(group_idx+1)]
        shift = idx % group_size
        for i in range(len(group_machines)):
            student_data[student].append(group_machines[(i + shift) % len(group_machines)])
        student_data[student].append(ports[shift])

    return student_data

if __name__ == '__main__':

    # Macine names and port numbers should be fixed.
    # If you want to change the machine names and port numbers, regenerate the zip files to assigin all zip files to students.
    # Or, please edit this program to assign new machines and ports to one student by username.
    machines = read_json('machines.json') 
    # Available port range
    ports = [i for i in range(30101, 30501, 20)]
    student_list = read_csv('students.csv')

    print('machines: ', machines)
    print('ports: ', ports)
    print('student_list: ', student_list)

    # Give options to user
    # [1] Generate all students' zip files
    # [2] Generate one student's zip file by username
    # [3] Add one student to csv file and generate zip file
    # [4] Add one student to csv file and generate <username>_machines_and_ports.txt
    # [5] Delete one student from csv file and delete zip file and <username>_machines_and_ports.txt
    # [6] Assign new machines and ports to one student by username
    # [7] Assign new ports to one student by username

    # Ask user to input the option
    print('Please select the option:')
    print('[1] Generate all students\' zip files')
    print('[2] Generate one student\'s zip file by username')
    print('[3] Add one student to csv file and generate zip file')
    print('[4] Add one student to csv file and generate <username>_machines_and_ports.txt')
    print('[5] Delete one student from csv file and delete zip file and <username>_machines_and_ports.txt')
    print('[6] Assign new machines and ports to one student by username')
    print('[7] Assign new ports to one student by username')
    option = input('Please input the option: ')

    # Get the current directory
    current_dir = os.getcwd()

    if option == '1':
        # Generate all students' zip files
        student_data = assign_machines_and_ports(student_list, machines, ports)
        # student_data = json.dumps(student_data, indent=4, sort_keys=False)
        # print('student_data: ', student_data)
        config_dir = 'bigdata_configs'
        mp_file = 'bigdata_configs/machines_and_ports.txt'
        for s in student_data:
            print('s: ', s)
            # If mp_file exists, delete it
            if os.path.exists(mp_file):
                os.remove(mp_file)
            # create a .txt file for each student
            with open(mp_file, 'w') as f:
                for i in student_data[s]:
                    f.write('%s\n' % i)
            # create a zip file for each student
            zip_file = '%s.zip' % s
            os.system('zip -r %s %s' % (zip_file, config_dir))
    else:
        print('Not implemented yet')
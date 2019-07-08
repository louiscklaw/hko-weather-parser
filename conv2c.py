#!/usr/bin/env python3

import os,sys


str_temp = ''

output_c = """const char* $$varname$$ =
$$my_str_content$$
"""

list_file_to_process=[]

for _root, _dir, _files in os.walk('./dummy-html'):
    for _file in _files:
        # print(_file)
        list_file_to_process.append('./dummy-html/'+_file)

for _file in list_file_to_process:
    input_file = _file
    output_file = input_file.replace('.xml','.c')
    filename = os.path.basename(input_file)
    varname = filename.replace('.','_')

    output = []
    temp = output_c

    with open(input_file,'r') as f:
    # with open('./dummy-html/test.xml','r') as f:
        # str_temp = ''.join(f.readlines())
        for line in f.readlines():
            # line = line.strip()
            line = line.replace('\n','\\n')
            line = line.replace('\"','\\"')
            line = '"'+line+'"'

            output.append(line)

    output = '\n'.join(output)+';'

    temp = temp.replace("$$my_str_content$$", output)
    temp = temp.replace("$$varname$$",varname)

    print(temp)

    with open(output_file,'w') as f:
        f.write(temp)

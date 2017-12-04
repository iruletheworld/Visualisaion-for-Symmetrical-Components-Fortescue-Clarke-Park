#import csv

import numpy as np

import gsyIO

time = np.arange(0, 1, 0.05)

data1 = np.arange(21, 20, -0.05)

data2 = np.arange(38, 39, 0.05)

#print(len(time))
#
#print(len(data))

temp_list = [time, data1, data2]

name_list = ['time', 'data1', 'data2']

#print(len(temp_list) == len(name_list))
#
#print(all(len(x) == len(temp_list[0]) for x in temp_list))

temp_zip_list = list(zip(*temp_list))

temp_zip_list.insert(0, ('time', 'data'))

# =============================================================================
# def save_csv(list_header, list_data, str_file_path):
#     
#     
#     str_err_msg_header_mismatch = ('The number of data headers'
#                                    + ' must match the number of data sets')
#     
#     str_err_msg_data_len_mismatch = ('The length of each data set'
#                                      + ' must be all the same')
#     
#     if len(list_header) != len(list_data):
#         
#         raise ValueError(str_err_msg_header_mismatch)
#         
#     else:
#         
#         pass
#     
#     bool_data_len = all( len(x) == len(list_data[0]) for x in list_data )
#     
#     if bool_data_len == False:
#         
#         raise ValueError(str_err_msg_data_len_mismatch)
#         
#     else:
#         
#         pass
#     
#     # Ref : https://goo.gl/SknzT8
#     temp_data = list(zip(*list_data))
#     
#     # add the header string to the first element
#     temp_data.insert(0, list_header)
#     
#     try:
#         
#         with open(str_file_path, 'w', newline='') as csv_file:
#             
#             writer = csv.writer(csv_file)
#             
#             for item in temp_data:
#                 
#                 writer.writerow(item)
#                 
#         return True
#         
#     except:
#             
#         raise OSError('Error when writing CSV file ' + str_file_path)
#         
#         return False
# =============================================================================


aaa = gsyIO.save_csv_gui(name_list, temp_list)

print('Done')
# =============================================================================
# with open(r'C:\Users\306235\Documents\_Temp\CSV\test.csv', 'w', newline='') as f:
#     
#     writer = csv.writer(f)
#     
#     for item in temp_zip_list:
#         
#         writer.writerow(item)
# =============================================================================


# =============================================================================
# output = open(r'C:\Users\306235\Documents\_Temp\CSV\test.csv', 'w', newline='')
# 
# fieldnames = ['time', 'data']
# 
# dataToWrite = [time, data]
# 
# writer = csv.DictWriter(output, fieldnames=fieldnames)
# 
# writer.writeheader()
# 
# dictToWriter = {}
# 
# listOfDict = []
# =============================================================================

# for item in range(len(fieldnames)):

#     for j in range(len(dataToWrite[item])):

#         dictToWriter[fieldnames[item]] = dataToWrite[j]

#         listOfDict.append({fieldnames[item]: dataToWrite[item][j]})

# print(listOfDict)

# for item in range(len(listOfDict)):

#     writer.writerow(listOfDict[item])

# =============================================================================
# output.close()
# 
# print('Done')
# 
# =============================================================================
# writer.writerow(dictToWriter)

# for item in range(len(fieldnames)):

#     print('item=' + str(item))

#     for j in range(len(toWrite[item])):

#         writer.writerow({fieldnames[item]: toWrite[item][j]})

#         print('j=' + str(j))


# for item in range(len(time)):

#     writer.writerow({fieldnames[0]: time[item], 'data': data[item]})

# output.close()

# print('Done')
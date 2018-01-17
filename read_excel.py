#####################################################################################
#   Pratyush Raunak								    #
#   Python Automation								    #
#										    #
#                                                                                   #
#####################################################################################

from selenium import webdriver         #importing selenium module
import csv			       #importing csv module to work with csv file format
import time 


def read_write():			#Function body
	file = open('text.csv')		#file opening 
	reader = csv.reader(file)	#csv.reader reads each lines
	data = list(reader)		#data contains the list of lists
	browser = webdriver.Firefox() 	#calling firefox webdriver
	browser.get('http://localhost/FeedBack/addFeedback.php')	#opening the url
	row_count = 0			#initialize the row_count
	for list0 in data:		#list0 contains the first list inside the data list
			col_count = 0	#initialize the column count
			for row in list0:
        			if (row_count == 0 and col_count == 0) or (row_count == 1 and col_count == 0) or (row_count == 2 and col_count == 0) or (row_count == 3 and col_count == 0): #True only if the column count is 0, row will keep changing 
        	        	                        Name = browser.find_element_by_id('fullname')
                	        	                Name.send_keys(data[row_count][col_count])
							col_count += 1
				if (row_count == 0 and col_count == 1) or (row_count == 1 and col_count == 1) or (row_count == 2 and col_count == 1) or (row_count == 3 and col_count == 1): #True only if the column count is 1  
							Name = browser.find_element_by_id('username')
                                                        Name.send_keys(data[row_count][col_count])
							col_count += 1
				if (row_count == 0 and col_count == 2) or (row_count == 1 and col_count == 2) or (row_count == 2 and col_count == 2) or (row_count == 3 and col_count == 2): #True for third col
							Name = browser.find_element_by_id('teamname')
                                                        Name.send_keys(data[row_count][col_count])
							col_count += 1
				if (row_count == 0 and col_count == 3) or (row_count == 1 and col_count == 3) or (row_count == 2 and col_count == 3) or (row_count == 3 and col_count == 3): #True for 4th column 
							Name = browser.find_element_by_id('descr')
                                                        Name.send_keys(data[row_count][col_count])
							col_count += 1
				if col_count >= 4: #check for col_count
							row_count += 1 #increment row_count
							break

				if row_count == 1:
						break
									
			Name.submit() #click the submit button on the webpage
			time.sleep(2)
			browser.get('http://localhost/FeedBack/addFeedback.php')
read_write()

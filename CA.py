file = "ap_docs.txt"    #Import text file
import string   #Import string library
input_file=open(file,"r")   #Opens the file as read only

def create_dict():  #This function in checks every if every word is in the dictionary and stores it's document number
    doc_no=0
    count_dict={}   #Initiates dictionary
    for line in input_file:     #Increments through every line in document
        for word in line.strip().split():   #Increments through every word in line
            if word == "<NEW":  #If line is <NEW DOCUMENT> line move onto the next line and increment doc number
                doc_no+=1
                break #Next line
            else:
                if word in count_dict:  #If the word is in the dictionary already
                    if doc_no not in count_dict[word]: #And the same document number is not in the dictionary value
                        count_dict[word].append(doc_no) #Add doc number to key
                else:
                    count_dict[word] = [doc_no] #Create key and value pair for word and doc number
    return count_dict   #return entire dictionary

def search_option(count_dict):  #This function searches the dictionary for the words inputted
        search_str=input("Enter search term(s)")
        i=0
        search_set={}   #Initiates search dictionary
        for word in search_str.strip().split(): #Increments through words in the input string
                search_set['term_%s'%i]=set(count_dict[word])   #The term will now have a new dictionary with value being a set of it's document numbers
                i += 1
        i=1
        search_range=len(search_str.strip().split()) #Range for index at line 33
        if len(search_str.strip().split()) > 1: #More than one search term
            i=1
            search_set['term_intersection'] = (search_set['term_%s' % i].intersection(search_set['term_%s' % (i - 1)])) #Gets the intersection of first pair of terms
            for i in range (2,search_range):
                search_set['term_intersection'] = (search_set['term_intersection'].intersection(search_set['term_%s'%(i)])) #Gets intersection of new term and search set
            if search_set['term_intersection']==set():
                print("Word combination not found in any document")
            else:
                print(search_set['term_intersection']) #Print intersection set, which is the doc number of doc with all search terms
        else:
            print(search_set['term_0']) #Only one search term so print it's doc number

def doc_list(index):
    file = "ap_docs.txt"    #The file has to be input and read again or else running this function more than once will give an error
    input_file = open(file, "r")
    doc_str=""
    list_doc=[]
    for line_str in input_file: #Increments through every line in file
        if "<N" in line_str:    #Append list and clear doc string when a new document is hit
            list_doc.append(doc_str)
            doc_str=""
        else:
            doc_str += line_str #Writes document text to doc string
    print("Document number %d"%index) #Nice output to cmd line
    print("-"*17)
    print(list_doc[index]) #Prints the document in the string at list element 'index'

count=create_dict() #Creates dictionary

while(1): #Menu display
    try:
        menu=int(input("What would you like to do?\n1. Search for documents\n2. Read Document\n3. Quit Program\n"))
        if menu == 1:   #Search terms in file
            search_option(count)    #Passes dictionary to search function so that it's the values can be ordered in a set and intersection document printed
        if menu == 2:   #Input document to view
            doc_list(int(input("Enter document to view")))
        if menu == 3:   #Quit program
            input_file.close()
            quit()
    except ValueError:  #Error check user input
        print("Invalid input")
    except KeyError:    #Error check user input
        print("Invalid input")
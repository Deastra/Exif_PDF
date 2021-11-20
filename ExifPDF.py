

from PyPDF2 import PdfFileReader #  These libraries have to be installed
from datetime import timedelta,date,datetime
from time import mktime, strptime
from warnings import filterwarnings
filterwarnings("ignore")


# return dictionary with metadata
# precondion: if impossible to read or exif doesn't exist, None will be returned

'''
Create or add 3 example pdf files to the source file folder
or instead write the file path for example1/2/3
'''
f1=open("example1.pdf","rb")
f2=open("example2.pdf","rb")
f3=open("example3.pdf","rb")

def get_exif(f):

    dct={}   # metadata will be stored here
    
    try:
        pdf_toread = PdfFileReader(f)
        pdf_info = pdf_toread.getDocumentInfo() # dictionary of all possible metadata
            
        for a in pdf_info:
            if(a=="/Creator" or a=="/CreationDate" or a=="/Producer"): # requested keys
                if(a == "/CreationDate"):
                    
                    datestring = pdf_info[a][2:16]
                    
                    # converting date object to readable string
                    ts = strptime(datestring, "%Y%m%d%H%M%S")
                    dt = datetime.fromtimestamp(mktime(ts))
                    dct[a.strip("/")] = dt.strftime("%m/%d/%Y %H:%M:%S")  
                else:   
                    dct[a.strip("/")] = pdf_info[a]
        
        if len(dct)==0:
            return None #no metadata
    except:
        return None  #no metadata
    
    dct=dict(sorted(dct.items())) # sorting by keys
    return dct


print(get_exif(f1))
print(get_exif(f2))
print(get_exif(f3))



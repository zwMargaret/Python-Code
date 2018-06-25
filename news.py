import pandas as pd
import numpy as np
from urllib import request
import json
import time
import pickle
import os

    
#################################################
# Here are functions for loading and combining json and txt files.

#-----------------------------------------------

def collectFilename(filepath_files,filetype='csv'):
    '''
    Collect names of files in specific dirs.
    
    Args:
        filepath(str): Filepath we want to collect stock tickers.
        
    Returns:
        file_list(list): List of tickers that have CSV in specific filepath.
    '''
    filename_list=[]
    for root, dirs, files in os.walk(filepath_files):
        if files:
            for f in files:
                if filetype in f:
                    filename_list.append(f.split('.'+filetype)[0])
    return filename_list


#-------------------------------------------------

def loadJson(filepath_json,filename):
    '''
    Load contents of a json file.

    Args:
    filepath(str): filepath where the json file is in
    filename(str): filename of json file like 'AAPL_2014-01-01'

    Returns:
    contents(str): contents of json file
    '''
    with open(filepath_json+filename+'.json','r',encoding='utf-8') as json_file:
        contents=json.load(json_file)
    return contents

#------------------------------------------------

def saveContentsAsJson(contents,filepath,filename):
    with open(filepath+filename+'.json','w',encoding='utf-8') as json_file:
        json.dump(contents,json_file,ensure_ascii=False)
        
#---------------------------------------------------

def saveJsonAsPickle(filepath_json,pickle_json_full_name,delete_repeated=True):
    '''
    This function is to collect all news of json files in "filepath_json" and save all news in the pickle file "pickle_json_full_name".

    Args:
    filepath_json(str): The filepath with json files we want to collect news from.
    pickle_json_full_name(str): The name of pickle file where news is saved in.
    delete_repeated(bool): If this is set as "True", then news with repeated "doc_id" would be deleted.

    Returns: All news of json files in "filepath_json"  would be saved in the pickle file "pickle_json_full_name".
    '''

    filename_list = collectFilename(filepath_json,'json')
    dict_list = []

    f = open(pickle_json_full_name,'wb')
    
    if not delete_repeated:
        for filename in filename_list:
            contents = loadJson(filepath_json,filename)
            last_update = contents['last_update']
            time_zone = contents['timezone']
            news = contents['data']
            
            symbol = filename[:-11]
            event_date = filename[-10:]
            contents_dict_new = {"symbol":symbol,"event_date":event_date,"last_update":last_update,"time_zone":time_zone,"data":news}
            pickle.dump(contents_dict_new,f)
    
    else:
        id_list = []
        
        for filename in filename_list:
            contents = loadJson(filepath_json,filename)
            
            last_update = contents['last_update']
            time_zone = contents['timezone']

            data = contents['data']
            
            symbol = filename[:-11]
            event_date = filename[-10:]

            news_list = []

            for i in range(len(data)):
                news = data[i]
                id = news['doc_id']

                if id not in id_list:
                    id_list.append(id)
                    news_list.append(news)
            
            contents_dict_new = {"symbol":symbol,"event_date":event_date,"last_update":last_update,"time_zone":time_zone,"data":news_list}
            pickle.dump(contents_dict_new,f)
    f.close()

    print('All json files have been saved in pickle file.')



##################################################
# Here are functions off downloading News from API

#----------------------------------------------------

def downloadNewsFromApi(stock_id,
                        start_date,
                        end_date,
                        api_link,
                        time_zone):

    '''
    This function is to automaticaly download news with period [start_date,end_date] from api.

    Args:
    stock_id(str or int):Symbol id of US stocks.
    start_date(str): The start date when getting news.
    end_date(str): The end date when getting news.
    api_link(str): Prefix of api.
    time_zone(str): Time zone of "start_date" and "end_date".

    Returns:
    news(dict): Dict of news including keys ['last_updated','timezone' and 'data'].
                Exact news is in list of dict news['data'][i]['teaser'] , i can be in [0:len(news['data])].

    '''
    
    stock_id = str(int(stock_id))
    start_date = str(pd.to_datetime(start_date))[:10]
    end_date = str(pd.to_datetime(end_date))[:10]
    
    full_link = api_link+stock_id+'&start_date='+end_date+'&end_date='+start_date
    
    if time_zone:
        full_link = full_link+'&timezone='+time_zone
        
    with request.urlopen(full_link) as f:
        data = f.read()
    news = json.loads(str(data, encoding='utf-8'))
    
    return news

#----------------------------------------------------

def getAllNews(input_df,filepath_output):

    '''
    This fucntion is to download all news of symbols in "input_df" and save news as json files to "filepath_output".

    Args:
    input_df(DataFrame): DataFrame with columns[['Symbol','company_id','Start_Date','Ene_Date','Date']]
    filepath_output(str): The filepath json files are saved in.

    Returns: News for specific symbols in specific time periods (samples in "input_df") 
             are downloaded from API and saved as json files to "filepath_output".
    
    
    '''
    k = np.arange(0,len(input_df))


    for i in k:      

        stock_id = input_df.iloc[i]['company_id']
        stock_name = input_df.iloc[i]['Symbol']
        start_date = input_df.iloc[i]['Start_Date']
        
        end_date = input_df.iloc[i]['End_Date']
        event_date = input_df.iloc[i]['Date']
        
        news = downloadNewsFromApi(stock_id,start_date,end_date)
        
        if len(news['data']) != 0 and news['data'] != 0:

            filename = stock_name+'_'+str(pd.to_datetime(event_date))[:10]
            saveContentsAsJson(news,filepath_output,filename)

        time.sleep(3)


    print ('*********ALL DONE**********')



############################################################################   


def main():

    input_df_1 = pd.read_csv('/data/input/downloadNews.py_input/10car.csv')
    input_df_2 = pd.read_csv('/data/input/downloadNews.py_input/20car.csv')

    filepath_json_1 = '/data/output_news/news_10car/'
    filepath_json_2 = '/data/output_news/news_20car/'

    pickle_json_full_name_1 = '/data/output_news/raw_news_10car.pickle'
    pickle_json_full_name_2 = '/data/output_news/raw_news_20car.pickle'


    getAllNews(input_df_1,filepath_json_1)   
    getAllNews(input_df_2,filepath_json_2)

    saveJsonAsPickle(filepath_json_1,pickle_json_full_name_1,delete_repeated=True)
    saveJsonAsPickle(filepath_json_2,pickle_json_full_name_2,delete_repeated=True)

if __name__ == '__main__':
    main()


import requests
url='https://www.youtube.com/watch?v=x7X9w_GIm1s'
from urllib.request import urlopen
def get_heatmap(url):
    ''''
    parameter -> url :str
    returns a json response with 
    {start_time in ms,end_time in ms,re-wind relative}
    re-wind relation can be used to infer mose replayed part of a video
    re-wind relative =1 -->most replayed part of the video
    '''
    html = str(urlopen(url).read())
    str_ind=html.index('{"heatMarkerRenderer":')
    end_ind=html.index('heatMarkersDecorations')
    text_html='{'+html[str_ind+22:end_ind-3]
    text_html=text_html.replace('"timeRangeStartMillis":','')
    text_html=text_html.replace('"markerDurationMillis":','')
    text_html=text_html.replace('"heatMarkerIntensityScoreNormalized":','')
    text_html=text_html.replace('{"heatMarkerRenderer":','')
    text_html=text_html.replace('},',',\n')
    
    #uncomment to save the file also as txt file
#     with open("heatmap.txt",'w',encoding = 'utf-8') as f:
#        f.write(text_html)
    
    
    return text_html

# print(get_heatmap(url))

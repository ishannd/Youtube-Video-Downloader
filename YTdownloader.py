import pytube

from tk_file import video_res,video_url

youtube_obj = pytube.YouTube(video_url)

def get_video_in_res(streams,video_res):
    stream = list(filter(lambda x : x.resolution == video_res , streams))
    return stream

req_stream_obj = get_video_in_res(youtube_obj.streams,video_res)[0]

req_stream_obj.download()

if(req_stream_obj):
    print("\n video downloaded")

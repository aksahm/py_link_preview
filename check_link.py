import link_preview
import time

if __name__ == "__main__":
    try:
        t1 = time.time()
        p = link_preview.generate_dict("https://richpreview.com")
        print('Time taken:- ' + str(time.time() - t1) + 's')
        
        print('Title: ' + p['title'])
        print('Description: ' + p['description'])
        print('Image: ' + p['image'])
        print('Website: ' + p['website'])
        
    except Exception as e:
        print(repr(e))
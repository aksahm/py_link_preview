'''
    Created on Feb 3, 2017
    
    @author: Akash
    
    link_preview is now a fashionable way of sharing links
    in social media. The contents of what the preview is 
    made up are:-
        1. og.title:-
            Title of the preview. 
            In HTML: <meta property="og.title" content="XYZ">
            Value: XYZ
            
        2. og.description:-
            Description of the preview.
            In HTML: <meta property="og.description" content="XYZ">
            Value: XYZ
            
        3. og.image:-
            Image of the preview.
            In HTML: <meta property="og.image" content="XYZ">
            Value: XYZ
            
        4. title:-
            if 'og:title' is not found, this becomes the Title.
            In HTML: <title>XYZ</title>
            Value: XYZ
            
        5. meta description:-
            if 'og:description' is not found, this becomes the Description.
            In HTML: <meta name="description" content="XYZ">
            Value: XYZ
            
        6. favicon:-
            if 'og:image' is not found, this becomes the Image.
            In HTML: <link rel="shortcut icon" href="XYZ" type="image/x-icon">
            Value: XYZ
            
        7. website:-
            Host website for the link.
            
    Reference:- https://richpreview.com/ (from where I learned)
    
    This module fetches all these data and combines those into 
    a dictionary.
    
    A sample WhatsApp link_preview:
    
        #######################################
        #   I    #    Title                   #
        #   M    #    Description             #
        #   A    #                            #
        #   G    #    website                 #
        #   E    #                            #
        #######################################
    
    Usage:-
        from link_preview import link_preview
        dict_elem = link_preview.generate_dict(url) # this is a dict()
        
        # Access values
        title = dict_elem['title']
        description = dict_elem['description']
        image = dict_elem['image']
        website = dict_elem['website']
'''

import urllib.request as req
import re

def generate_dict(url):
    '''
        returns dictionary containing elements of link_preview:
            dict_keys :
                'title' : '',
                'description': '',
                'image': '',
                'website': ''
        if Exception occurs, it raises Exception of urllib.request module.
    '''
    return_dict = {}
    try:
        html = req.urlopen(url).read().decode('utf-8')
        meta_elems = re.findall('<[\s]*meta[^<>]+og:(?:title|image|description)(?!:)[^<>]+>', html)
        og_map = map(return_og, meta_elems)
        og_dict = dict(list(og_map))
    
    #     title
        try:
            return_dict['title'] = og_dict['og.title']
        except KeyError:
            return_dict['title'] = find_title(html)
    
    #     description
        try:
            return_dict['description'] = og_dict['og.description']
        except KeyError:
            return_dict['description'] = find_meta_desc(html)
    
    #     website
        return_dict['website'] = find_host_website(url)
    
    #     Image
        try:
            return_dict['image'] = og_dict['og.image']
        except KeyError:
            image_path = find_image(html)
            if 'http' not in image_path:
                image_path = 'http://' + return_dict['website'] + image_path
            return_dict['image'] = image_path
        
        return return_dict
    
    except Exception as e:
        'Raises Occurred Exception'
        raise e

def return_og(elem):
    '''
        returns content of og_elements
    '''
    content = re.findall('content[\s]*=[\s]*"[^<>"]+"', elem)[0]
    p = re.findall('"[^<>]+"', content)[0][1:-1]
    if 'og:title' in elem:
        return ("og.title", p)
    elif 'og:image' in elem and 'og:image:' not in elem:
        return ("og.image", p)
    elif 'og:description' in elem:
        return ("og.description", p)
    
def find_title(html):
    '''
        returns the <title> of html
    '''
    try:
        title_elem = re.findall('<[\s]*title[\s]*>[^<>]+<[\s]*/[\s]*title[\s]*>', html)[0]
        title = re.findall('>[^<>]+<', title_elem)[0][1:-1]
    except:
        title = ''
    return title

def find_meta_desc(html):
    '''
        returns the description (<meta name="description") of html
    '''
    try:
        meta_elem = re.findall('<[\s]*meta[^<>]+name[\s]*=[\s]*"[\s]*description[\s]*"[^<>]*>', html)[0]
        content = re.findall('content[\s]*=[\s]*"[^<>"]+"', meta_elem)[0]
        description = re.findall('"[^<>]+"', content)[0][1:-1]
    except:
        description = ''
    return description

def find_image(html):
    '''
        returns the favicon of html
    '''
    try:
        favicon_elem = re.findall('<[\s]*link[^<>]+rel[\s]*=[\s]*"[\s]*shortcut icon[\s]*"[^<>]*>', html)[0]
        href = re.findall('href[\s]*=[\s]*"[^<>"]+"', favicon_elem)[0]
        image = re.findall('"[^<>]+"', href)[0][1:-1]
    except:
        image = ''
    return image

def find_host_website(url):
    '''
        returns host website from the url
    '''
    return list(filter(lambda x: '.' in x, url.split('/')))[0]
